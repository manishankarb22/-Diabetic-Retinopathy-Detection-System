"""
Diabetic Retinopathy Detection Flask Application
Uses Xception model for image classification
Integrates with IBM Cloudant for data storage
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from datetime import datetime
import json

# Cloudant DB imports (optional - will work without it)
try:
    from cloudant.client import Cloudant
    from cloudant.error import CloudantException
    CLOUDANT_AVAILABLE = True
except ImportError:
    CLOUDANT_AVAILABLE = False
    print("Warning: Cloudant not installed. Database features disabled.")

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

# Configuration
UPLOAD_FOLDER = 'uploads'
MODEL_PATH = 'inception-diabetic.h5'  # Using Inception model
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
IMG_HEIGHT = 224
IMG_WIDTH = 224

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Class names - Update these based on your dataset classes
CLASS_NAMES = ['No DR', 'Mild', 'Moderate', 'Severe', 'Proliferative DR']

# IBM Cloudant Configuration
# Replace these with your actual Cloudant credentials
CLOUDANT_USERNAME = "your-cloudant-username"
CLOUDANT_API_KEY = "your-cloudant-api-key"
CLOUDANT_URL = "your-cloudant-url"
DATABASE_NAME = "diabetic_retinopathy_db"

# Initialize Cloudant client (will be set up when credentials are provided)
cloudant_client = None
database = None


def init_cloudant():
    """Initialize Cloudant database connection"""
    if not CLOUDANT_AVAILABLE:
        print("Cloudant not available. Database features disabled.")
        return False
    
    global cloudant_client, database
    try:
        cloudant_client = Cloudant.iam(
            CLOUDANT_USERNAME,
            CLOUDANT_API_KEY,
            connect=True,
            url=CLOUDANT_URL
        )
        
        # Create database if it doesn't exist
        if DATABASE_NAME not in cloudant_client.all_dbs():
            database = cloudant_client.create_database(DATABASE_NAME)
            print(f"Database '{DATABASE_NAME}' created successfully")
        else:
            database = cloudant_client[DATABASE_NAME]
            print(f"Connected to existing database '{DATABASE_NAME}'")
        
        return True
    except CloudantException as e:
        print(f"Cloudant connection error: {e}")
        return False
    except Exception as e:
        print(f"Error initializing Cloudant: {e}")
        return False


def save_to_cloudant(username, image_name, prediction, confidence, timestamp):
    """Save prediction results to Cloudant database"""
    try:
        if database is None:
            print("Database not initialized")
            return False
        
        document = {
            "username": username,
            "image_name": image_name,
            "prediction": prediction,
            "confidence": float(confidence),
            "timestamp": timestamp,
            "type": "prediction"
        }
        
        # Create document in database
        new_document = database.create_document(document)
        
        if new_document.exists():
            print(f"Document saved with ID: {new_document['_id']}")
            return True
        else:
            print("Failed to save document")
            return False
    except Exception as e:
        print(f"Error saving to Cloudant: {e}")
        return False


# Load the trained model
try:
    model = load_model(MODEL_PATH)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def preprocess_image(img_path):
    """Preprocess image for model prediction"""
    img = image.load_img(img_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array


def predict_diabetic_retinopathy(img_path):
    """Make prediction on image"""
    if model is None:
        return None, 0
    
    try:
        # Preprocess image
        processed_img = preprocess_image(img_path)
        
        # Make prediction
        prediction = model.predict(processed_img)
        predicted_class_index = np.argmax(prediction)
        confidence = np.max(prediction) * 100
        
        # Get class name
        if predicted_class_index < len(CLASS_NAMES):
            predicted_class = CLASS_NAMES[predicted_class_index]
        else:
            predicted_class = f"Class {predicted_class_index}"
        
        return predicted_class, confidence
    except Exception as e:
        print(f"Prediction error: {e}")
        return None, 0


@app.route('/')
def index():
    """Home page"""
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Simple authentication (In production, use proper authentication)
        # You can integrate with Cloudant to store and verify user credentials
        if username and password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials!', 'error')
    
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration page"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not all([username, email, password, confirm_password]):
            flash('All fields are required!', 'error')
        elif password != confirm_password:
            flash('Passwords do not match!', 'error')
        else:
            # In production, save user to Cloudant database
            # Hash password before storing
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/logout')
def logout():
    """Logout user"""
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Prediction page - upload image and get prediction"""
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Check if file is uploaded
        if 'file' not in request.files:
            flash('No file uploaded!', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        
        # Check if file is selected
        if file.filename == '':
            flash('No file selected!', 'error')
            return redirect(request.url)
        
        # Check if file is allowed
        if file and allowed_file(file.filename):
            # Secure filename and save
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            unique_filename = f"{timestamp}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(filepath)
            
            # Make prediction
            predicted_class, confidence = predict_diabetic_retinopathy(filepath)
            
            if predicted_class:
                # Save to Cloudant
                save_to_cloudant(
                    username=session['username'],
                    image_name=unique_filename,
                    prediction=predicted_class,
                    confidence=confidence,
                    timestamp=datetime.now().isoformat()
                )
                
                return render_template(
                    'prediction.html',
                    prediction=predicted_class,
                    confidence=round(confidence, 2),
                    image_path=unique_filename,
                    username=session['username']
                )
            else:
                flash('Error making prediction. Please try again.', 'error')
                return redirect(request.url)
        else:
            flash('Invalid file type! Only PNG, JPG, and JPEG are allowed.', 'error')
            return redirect(request.url)
    
    return render_template('index.html', username=session['username'])


@app.route('/history')
def history():
    """View prediction history from Cloudant"""
    if 'username' not in session:
        return redirect(url_for('login'))
    
    try:
        if database:
            # Query all documents for the user
            selector = {
                'username': {'$eq': session['username']},
                'type': {'$eq': 'prediction'}
            }
            results = database.get_query_result(selector, sort=[{'timestamp': 'desc'}])
            predictions = [doc for doc in results]
            return render_template('history.html', predictions=predictions, username=session['username'])
        else:
            flash('Database not connected', 'error')
            return redirect(url_for('index'))
    except Exception as e:
        print(f"Error fetching history: {e}")
        flash('Error fetching history', 'error')
        return redirect(url_for('index'))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded files"""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html', username=session.get('username'))


# Error handlers
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    # Initialize Cloudant connection
    # Uncomment the following line after adding your Cloudant credentials
    # init_cloudant()
    
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5000)
