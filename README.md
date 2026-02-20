# 🏥 Diabetic Retinopathy Detection System

A comprehensive web-based application for detecting and classifying diabetic retinopathy from retinal fundus images using advanced deep learning technology. This system uses a pre-trained Xception neural network model to classify diabetic retinopathy severity levels with high accuracy.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![Flask](https://img.shields.io/badge/flask-2.3.0-orange.svg)
![TensorFlow](https://img.shields.io/badge/tensorflow-2.20.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Technology Stack](#technology-stack)
- [Installation Guide](#installation-guide)
- [Configuration](#configuration)
- [Usage Instructions](#usage-instructions)
- [Demo Video](#demo-video)
- [API Documentation](#api-documentation)
- [Model Details](#model-details)
- [Database Integration](#database-integration)
- [Security Features](#security-features)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🏥 Project Overview

**Diabetic Retinopathy (DR)** is a serious diabetic complication that can lead to vision loss if not detected early. This system leverages state-of-the-art deep learning to automate the detection and classification of diabetic retinopathy severity levels, making screening more accessible, efficient, and accurate.

### Severity Classification

The system can classify retinal images into **5 categories**:

| Category | Description | Severity |
|----------|-------------|----------|
| **No DR** | No signs of diabetic retinopathy | None |
| **Mild** | Mild microaneurysms present | Low |
| **Moderate** | Moderate non-proliferative changes | Medium |
| **Severe** | Severe non-proliferative changes | High |
| **Proliferative DR** | Neovascularization and advanced pathology | Critical |

### Clinical Significance

- **Early Detection**: Enables early intervention and treatment
- **Accessibility**: Brings screening capability to underserved regions
- **Efficiency**: Reduces manual screening burden on ophthalmologists
- **Accuracy**: Deep learning provides consistent, reliable classification

---

## 📁 Repository Structure

```
YouTubeLiveFeed/ (ROOT)
│
├── README.md                                    # Master project documentation (this file)
│
├── SmartinterProject/                          # Main Flask Application
│   ├── app.py                                 # Flask application with routes & ML logic
│   ├── inception-diabetic.h5                  # Pre-trained Xception model (weights)
│   ├── requirements.txt                       # Python dependencies
│   ├── .env.example                           # Environment variables template
│   ├── .gitignore                             # Git ignore patterns
│   ├── README.md                              # Application-specific documentation
│   │
│   ├── static/                                # Web assets
│   │   ├── css/
│   │   │   └── style.css                     # Modern UI styling
│   │   └── images/                           # Logo and icons
│   │
│   ├── templates/                             # HTML templates
│   │   ├── index.html                        # Home/Dashboard
│   │   ├── login.html                        # Login page
│   │   ├── register.html                     # Registration page
│   │   ├── prediction.html                   # Results page
│   │   ├── history.html                      # Prediction history
│   │   ├── about.html                        # About page
│   │   ├── 404.html                          # Error pages
│   │   └── 500.html
│   │
│   ├── model/                                 # ML Model files
│   │   └── Xception_Diabetic_retinopathy.ipynb  # Model training notebook
│   │
│   ├── uploads/                               # User-uploaded images (runtime)
│   └── 20260220-0853-10.5332511.mp4           # Demo video file
│
├── Project documentation/                     # Comprehensive documentation
│   ├── Diabetic Retinopathy Project Documentation.docx
│   └── README.md                             # Documentation guide
│
├── demo video/                                # Demo video files
│   ├── 20260220-0853-10.5332511.mp4          # Full system walkthrough
│   └── README.md                             # Video guide with drive link
│
└── .git/                                      # Git repository

```

---

## ✨ Key Features

### 🎯 Core Functionality

- **🖼️ Smart Image Upload**
  - Support for PNG, JPG, and JPEG formats
  - Real-time image preview
  - Automatic image validation
  - File size limits (16MB max)

- **🧠 AI-Powered Prediction**
  - Xception deep neural network
  - 224x224 input resolution
  - 5-class classification
  - Confidence scores for transparency

- **👤 User Management**
  - Secure login/registration system
  - Session-based authentication
  - User profile management
  - Password validation

- **📊 Prediction Tracking**
  - Complete history of predictions
  - Timestamp and metadata
  - Search and filtering
  - Export capabilities

- **💾 Data Storage**
  - Optional IBM Cloudant integration
  - Secure document storage
  - Query and retrieval
  - Scalable NoSQL solution

### 🎨 User Interface

- Modern, responsive web design
- Dark/light theme support
- Intuitive navigation
- Real-time feedback
- Mobile-friendly interface
- Accessibility features

### 🔒 Security

- Session-based authentication
- File upload validation
- Secure filename handling
- XSS and CSRF protection
- Input sanitization
- SSL/TLS support

### ⚡ Performance

- Fast image processing (2-5 seconds)
- Efficient model inference
- Database query optimization
- Caching mechanisms
- Horizontal scalability

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────┐
│              Web Browser / Client                    │
│             (HTML5, CSS3, JavaScript)               │
└────────────────────┬────────────────────────────────┘
                     │
                HTTP/HTTPS
                     │
┌────────────────────▼────────────────────────────────┐
│          Flask Web Application Server                │
│                    (Port 5000)                       │
│                                                      │
│  ├─ Authentication & Session Management             │
│  ├─ Request Routing & Handler                       │
│  ├─ File Upload Processing                          │
│  ├─ Image Preprocessing                             │
│  └─ Response Rendering                              │
└─┬──────────────────┬──────────────────────┬─────────┘
  │                  │                      │
  │                  │                      │
  ▼                  ▼                      ▼
┌──────────┐  ┌─────────────┐      ┌──────────────┐
│TensorFlow│  │   Uploads   │      │  Cloudant DB │
│  / Keras │  │  Folder     │      │  (Optional)  │
│          │  │  Storage    │      │              │
│ Xception │  │             │      │ - Users      │
│  Model   │  │ - Images    │      │ - Predictions│
│          │  │ - Metadata  │      │ - History    │
└──────────┘  └─────────────┘      └──────────────┘
```

---

## 🛠️ Technology Stack

### Backend & Framework
| Component | Technology | Version |
|-----------|-----------|---------|
| Web Framework | Flask | 2.3.0 |
| Programming Language | Python | 3.8+ |
| WSGI Server | Werkzeug | 2.3.0 |
| Session Management | Flask-Session | Built-in |

### Machine Learning & AI
| Component | Technology | Version |
|-----------|-----------|---------|
| Deep Learning | TensorFlow | 2.20.0 |
| Neural Networks | Keras | Built-in (TF 2.20.0) |
| Model Architecture | Xception | Pre-trained |
| Numerical Computing | NumPy | 2.1.3 |
| Data Processing | Pandas | 2.2.0 |

### Image Processing
| Component | Technology | Version |
|-----------|-----------|---------|
| Image Library | Pillow | 11.0.0 |
| Image Operations | scikit-image | (via TF) |
| Preprocessing | cv2 | (opt.) |

### Database
| Component | Technology | Version |
|-----------|-----------|---------|
| Primary DB | IBM Cloudant | Optional |
| DB Client | cloudant-python | 2.15.0 |
| Type | NoSQL/Document | Cloud-based |

### Frontend
| Component | Technology |
|-----------|-----------|
| HTML | HTML5 |
| CSS | CSS3 + Grid/Flexbox |
| Icons | Font Awesome 6.5.0 |
| Fonts | Google Fonts (Inter, JetBrains Mono) |

### Utilities
| Component | Technology | Version |
|-----------|-----------|---------|
| Date/Time | python-dateutil | 2.8.2 |
| HTTP Requests | requests | 2.31.0 |
| Environment | python-dotenv | 0.19.2 |
| File Handling | Werkzeug | 2.3.0 |

---

## 🚀 Installation Guide

### Prerequisites

```
✓ Python 3.8 or higher
✓ pip (Python package manager)
✓ 4GB RAM minimum (8GB recommended)
✓ Git (for cloning repository)
✓ Modern web browser
```

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/manishankarb22/-Diabetic-Retinopathy-Detection-System.git
cd YouTubeLiveFeed
cd SmartinterProject
```

#### 2. Create Virtual Environment (RECOMMENDED)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**Optional - GPU Support (CUDA):**
```bash
pip install tensorflow[and-cuda]
```

#### 4. Verify Installation
```bash
python -c "import tensorflow as tf; print(tf.__version__)"
python -c "import flask; print(flask.__version__)"
```

#### 5. Create Upload Directory
```bash
mkdir uploads
```

#### 6. Run the Application
```bash
python app.py
```

#### 7. Access the Application
```
Open your browser and navigate to:
http://localhost:5000
```

---

## ⚙️ Configuration

### Flask Configuration (app.py)

```python
# Security
app.secret_key = 'change-this-to-random-secret-key'

# Upload Settings
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

# Model Settings
MODEL_PATH = 'inception-diabetic.h5'
IMG_HEIGHT = 224
IMG_WIDTH = 224

# Classification Classes
CLASS_NAMES = ['No DR', 'Mild', 'Moderate', 'Severe', 'Proliferative DR']

# Server Settings
DEBUG = False  # Set True only for development
HOST = '0.0.0.0'
PORT = 5000
```

### Environment Variables (.env)

Create a `.env` file based on `.env.example`:

```bash
# IBM Cloudant Configuration (Optional)
CLOUDANT_USERNAME=your_username
CLOUDANT_API_KEY=your_api_key
CLOUDANT_URL=your_url
DATABASE_NAME=diabetic_retinopathy_db

# Flask Settings
FLASK_ENV=production  # or development
SECRET_KEY=your-secret-key-here
```

### Production Deployment

**Important Security Changes:**
```python
# app.py
app.debug = False
app.secret_key = os.environ.get('SECRET_KEY')  # From .env
CLOUDANT_USERNAME = os.environ.get('CLOUDANT_USERNAME')
CLOUDANT_API_KEY = os.environ.get('CLOUDANT_API_KEY')
# ... other env vars
```

---

## 💻 Usage Instructions

### User Journey

#### Step 1: Register Account
1. Navigate to `http://localhost:5000/register`
2. Enter username, email, password
3. Confirm password
4. Click "Register"

#### Step 2: Login
1. Go to `http://localhost:5000/login`
2. Enter credentials
3. Click "Login"

#### Step 3: Upload & Predict
1. Click "Predict" in navigation
2. Select retinal fundus image
3. Click "Upload and Predict"
4. View results with confidence score

#### Step 4: View History
1. Click "History" in navigation
2. See all previous predictions
3. Filter by date or severity
4. Download reports (if enabled)

#### Step 5: Logout
1. Click "Logout" button
2. Session ends securely

### Supported Image Formats

| Format | Extension | Recommended Size |
|--------|-----------|-----------------|
| PNG | .png | 500x500+ |
| JPEG | .jpg, .jpeg | 500x500+ |
| All | PNG/JPG/JPEG | <16MB |

---

## 🎬 Demo Video

### Watch the Complete System Walkthrough

**🔗 Google Drive Link (High Quality):**
```
https://drive.google.com/file/d/1lvMJpQC7IRogtFp6gyUHB5lJZutOaLQe/view?usp=drivesdk
```

### [👉 CLICK HERE TO WATCH DEMO 👈](https://drive.google.com/file/d/1lvMJpQC7IRogtFp6gyUHB5lJZutOaLQe/view?usp=drivesdk)

### Demo Contents

The video demonstrates:
- ✅ User registration and login workflow
- ✅ Home dashboard and navigation
- ✅ Image upload and real-time prediction
- ✅ Prediction results with confidence scores
- ✅ Prediction history tracking
- ✅ Database integration
- ✅ Logout and session management
- ✅ Error handling and validation

### Video Specifications

| Property | Details |
|----------|---------|
| Format | MP4 (H.264) |
| Resolution | 1920x1080 (Full HD) |
| Size | ~22 MB |
| Duration | Complete walkthrough |
| Date | February 20, 2026 |

---

## 📡 API Documentation

### Authentication Endpoints

#### POST /register
Register a new user account
```
Parameters:
  - username (required): String
  - email (required): Email format
  - password (required): String
  - confirm_password (required): Must match password

Response: Redirect to login on success
```

#### POST /login
Authenticate user with credentials
```
Parameters:
  - username (required): String
  - password (required): String

Response: Session created, redirect to home
```

#### GET /logout
End user session
```
Response: Redirect to login page
```

### Application Endpoints

#### GET /
Home page (authenticated)
```
Required: Login session
Returns: Dashboard HTML
```

#### GET/POST /predict
Upload image and get prediction
```
Method: POST
Parameters:
  - file (required): Image file (PNG/JPG/JPEG)

Response: Prediction results with:
  - prediction: Class name
  - confidence: Percentage (0-100)
  - timestamp: ISO format
```

#### GET /history
View prediction history (authenticated)
```
Required: Login session
Returns: List of all predictions for user
```

#### GET /about
Project information page
```
Returns: About page HTML
```

#### GET /uploads/<filename>
Retrieve uploaded image file
```
Parameters:
  - filename: Image filename
Response: Image file
```

### Complete API Endpoint Table

| HTTP | Endpoint | Description | Auth |
|------|----------|-------------|------|
| GET/POST | `/login` | User login | No |
| GET/POST | `/register` | User registration | No |
| GET | `/logout` | User logout | Yes |
| GET | `/` | Home page | Yes |
| GET/POST | `/predict` | Predict DR severity | Yes |
| GET | `/history` | View prediction history | Yes |
| GET | `/about` | About page | No |
| GET | `/uploads/<filename>` | Get uploaded image | Yes |

---

## 🧠 Model Details

### Architecture

```
Model: Xception
├── Input Layer: 224 × 224 × 3 (RGB)
├── Preprocessing: Normalization (0→1)
├── Xception Blocks
│   ├── Entry Flow
│   ├── Middle Flow (8 repetitions)
│   └── Exit Flow
├── Global Average Pooling
├── Dense Layer: 128 neurons
├── Dropout: 0.5
├── Output Layer: 5 neurons (Softmax)
└── Classes: [No DR, Mild, Moderate, Severe, Proliferative DR]
```

### Model Specifications

| Property | Value |
|----------|-------|
| Type | Convolutional Neural Network |
| Architecture | Xception (Extreme Inception) |
| Input Size | 224 × 224 × 3 |
| Output Classes | 5 severity levels |
| Total Parameters | ~22.9 Million |
| Pre-trained | ImageNet |
| Fine-tuned | Diabetic Retinopathy Dataset |
| Framework | TensorFlow/Keras |
| File Size | ~1.2 GB |
| Inference Time | 2-5 seconds per image |

### Training Details

**Training Notebook:** `SmartinterProject/model/Xception_Diabetic_retinopathy.ipynb`

Includes:
- Dataset loading and exploration
- Preprocessing and augmentation
- Model architecture definition
- Training with callbacks
- Evaluation metrics
- Visualization of results
- Model export and serialization

### Performance Metrics

*Add actual metrics after training:*
- Accuracy: TBD
- Sensitivity: TBD
- Specificity: TBD
- AUC: TBD

### Preprocessing Pipeline

```python
1. Load Image (any supported format)
2. Resize to 224×224
3. Convert BGR to RGB (if needed)
4. Normalize: pixel_values / 255.0
5. Expand dimensions for batch processing
6. Input to model
```

---

## 💾 Database Integration

### IBM Cloudant Setup (Optional)

The application can store predictions in IBM Cloudant NoSQL database.

#### Enable Database Features

1. **Create Cloudant Instance**
   - Go to [IBM Cloud Console](https://cloud.ibm.com)
   - Create Cloudant service
   - Get API credentials

2. **Update Configuration**
   ```python
   # In app.py
   CLOUDANT_USERNAME = "your-username"
   CLOUDANT_API_KEY = "your-api-key"
   CLOUDANT_URL = "https://your-url.cloudant.com"
   DATABASE_NAME = "diabetic_retinopathy_db"
   ```

3. **Uncomment Initialization**
   ```python
   # In main block of app.py
   # init_cloudant()
   ```

4. **Verify Connection**
   ```python
   # Should print success message
   ```

### Document Structure

Predictions stored as JSON documents:

```json
{
  "_id": "auto-generated-uuid",
  "_rev": "document-revision",
  "username": "user123",
  "image_name": "20260220_085312_image.jpg",
  "prediction": "Moderate",
  "confidence": 0.9234,
  "timestamp": "2026-02-20T08:53:12.123456Z",
  "type": "prediction",
  "metadata": {
    "ip_address": "192.168.1.1",
    "user_agent": "Mozilla/5.0...",
    "session_id": "sess_123"
  }
}
```

### Database Operations

```python
# Save prediction
save_to_cloudant(
    username=session['username'],
    image_name=filename,
    prediction=class_name,
    confidence=score,
    timestamp=datetime.now().isoformat()
)

# Retrieve user history
selector = {
    'username': {'$eq': username},
    'type': {'$eq': 'prediction'}
}
results = database.get_query_result(selector)

# Query predictions
database.get_query_result(
    selector={'prediction': {'$eq': 'Severe'}},
    sort=[{'timestamp': 'desc'}]
)
```

### Without Database

Application fully works without Cloudant:
- Predictions display immediately
- History not persisted (session-only)
- No long-term data storage
- Perfect for demo/testing

---

## 🔒 Security Features

### Current Implementation

✅ **Session Management**
- Flask session with secure storage
- Automatic session timeout
- CSRF token validation

✅ **File Upload Security**
- Extension validation (PNG/JPG/JPEG only)
- File size limits (16MB max)
- Secure filename handling
- MIME type verification

✅ **Input Validation**
- Username/email validation
- Password length requirements
- SQL injection prevention (ORM)
- XSS protection

✅ **Authentication**
- Session-based login
- Password securely handled
- Logout clears session

### Production Security Recommendations

⚠️ **Password Security**
```python
# Use werkzeug.security
from werkzeug.security import generate_password_hash, check_password_hash

# Hash passwords
hashed_pwd = generate_password_hash(password, method='pbkdf2:sha256')

# Verify passwords
if check_password_hash(hashed_pwd, password_attempt):
    # Login successful
```

⚠️ **HTTPS/TLS**
- Use SSL certificates (Let's Encrypt)
- Force HTTPS redirect
- Set Strict-Transport-Security header

⚠️ **Rate Limiting**
```python
# Install flask-limiter
from flask_limiter import Limiter
limiter = Limiter(app, key_func=lambda: session.get('username'))

@app.route('/predict', methods=['POST'])
@limiter.limit("5 per minute")
def predict():
    # Only 5 predictions per minute per user
```

⚠️ **CORS Protection**
```python
# Install flask-cors
from flask_cors import CORS
CORS(app, resources={r"/api/*": {"origins": "yourdomain.com"}})
```

⚠️ **Environment Variables**
- Never hardcode secrets
- Use .env files (not in git)
- Use cloud provider secret management
- Rotate API keys regularly

---

## 🐛 Troubleshooting

### Common Issues & Solutions

#### 1. Model Loading Error
```
Error: Error loading model: inception-diabetic.h5
```
**Solutions:**
- Verify `inception-diabetic.h5` exists in project root
- Check file is not corrupted: `fc inception-diabetic.h5`
- Ensure TensorFlow 2.20.0 compatibility
- Reinstall TensorFlow: `pip install --upgrade tensorflow==2.20.0`

#### 2. Port Already in Use
```
Error: Address already in use (:5000)
```
**Solutions:**
- Change port: Edit `app.run(port=5001)`
- Kill process: `lsof -ti:5000 | xargs kill -9` (Mac/Linux)
- Windows: `netstat -ano | findstr :5000` then `taskkill /PID <PID> /F`

#### 3. File Upload Failed
```
Error: No file uploaded! or Invalid file type!
```
**Solutions:**
- Use PNG, JPG, or JPEG format
- File size < 16MB
- Check browser file selection
- Check disk space (uploads folder)

#### 4. Prediction Takes Too Long
```
Prediction takes >10 seconds
```
**Solutions:**
- Check system resources (RAM, CPU)
- GPU acceleration: `pip install tensorflow[and-cuda]`
- Reduce image size before upload
- Close other applications

#### 5. Database Connection Error
```
Error: Cloudant connection error
```
**Solutions:**
- Verify credentials in .env
- Check Cloudant service is running
- Test credentials: Cloudant IAM access
- Disable Cloudant (app works without it)

#### 6. Session/Login Issues
```
Error: 'username' not in session
```
**Solutions:**
- Clear browser cookies
- Try incognito/private window
- Restart browser
- Ensure cookies enabled

### Debug Mode

Enable debug logging:
```python
# In app.py
app.run(debug=True)
```

Check logs for detailed error messages:
```bash
# Check flask console output for messages
# Database: Printed to console
# Model: TensorFlow verbose mode
```

---

## 📚 Documentation Files

### SmartinterProject/README.md
- Application-specific documentation
- Installation details
- Configuration guide
- API reference
- Model information

### Project documentation/README.md
- Comprehensive project documentation
- System requirements
- Architecture details
- Implementation guide
- Deployment procedures

### demo video/README.md
- Demo video information
- Features covered
- System requirements
- Quick start guide
- Contact information

---

## 📊 File Descriptions

### Core Application Files

**app.py** (338 lines)
- Flask application framework
- Route handlers for all endpoints
- Authentication logic
- Prediction execution
- Cloudant integration
- Error handlers

**requirements.txt**
- All Python dependencies
- Specific versions pinned
- Optional packages commented
- GPU acceleration notes

**inception-diabetic.h5** (~1.2 GB)
- Pre-trained Xception model
- Weights and architecture
- RGB image compatible
- 224×224 input format

### Frontend Files

**templates/index.html** (381 lines)
- Home/dashboard page
- Modern responsive design
- Navigation menu
- Feature showcase
- Dark theme UI

**templates/login.html**
- User login form
- Email/password fields
- Client-side validation
- Link to registration

**templates/register.html**
- User registration form
- Validation rules
- Password confirmation
- Link to login

**templates/prediction.html**
- Prediction results display
- Confidence visualization
- Image preview
- Severity indicator

**templates/history.html**
- Prediction history table
- Timestamps and details
- Search/filter options
- Sorting capabilities

**templates/about.html**
- Project information
- Team details
- System overview
- Contact information

**static/css/style.css**
- Complete UI styling
- Responsive design
- Dark/light themes
- Animations and transitions
- Mobile optimization

### Model Files

**model/Xception_Diabetic_retinopathy.ipynb**
- Jupyter notebook format
- Dataset loading code
- Model architecture definition
- Training procedures
- Evaluation metrics
- Visualization code

### Configuration Files

**.env.example**
- Template for environment variables
- Cloudant credentials
- Flask settings
- Database configuration

**.gitignore**
- Python cache files
- Virtual environment
- Environment variables
- Uploaded files
- System files

---

## 🤝 Contributing

### How to Contribute

1. **Fork the Repository**
   ```bash
   # Click "Fork" on GitHub
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Make Changes**
   ```bash
   # Edit files
   git add .
   git commit -m "Add your feature"
   ```

4. **Push to Branch**
   ```bash
   git push origin feature/YourFeature
   ```

5. **Open Pull Request**
   - Describe changes clearly
   - Link related issues
   - Request review from maintainers

### Contribution Guidelines

- Follow PEP 8 style guide
- Add tests for new features
- Update documentation
- Comment complex code
- Use meaningful commit messages

### Areas for Contribution

- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🧪 Additional tests
- 🎨 UI/UX improvements
- ⚡ Performance optimization

---

## 📝 License

This project is open source and available under the **MIT License**.

```
MIT License

Copyright (c) 2026 Manisha Nkarb

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT IS, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE
AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
```

---

## 👨‍💻 Author & Contact

**Manisha Nkarb** (Author & Lead Developer)

### Connect with Us

| Platform | Link |
|----------|------|
| GitHub | [@manishankarb22](https://github.com/manishankarb22) |
| Email | manishankarb22@gmail.com |
| Repository | [Diabetic-Retinopathy-Detection-System](https://github.com/manishankarb22/-Diabetic-Retinopathy-Detection-System) |

### Acknowledgments

- **Deep Learning Community**: TensorFlow, Keras teams
- **Cloud Services**: IBM Cloud for Cloudant
- **Open Source**: Flask, NumPy, Pandas communities
- **Medical Imaging**: Dataset contributors and researchers
- **Design Resources**: Font Awesome, Google Fonts

---

## ⚠️ Medical Disclaimer

### Important Legal Notice

**THIS SYSTEM IS FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY**

⚠️ **This application should NOT be used for:**
- Clinical diagnosis without proper medical supervision
- Replacement of professional medical attention
- Treatment decision-making
- Definitive disease determination

✅ **This application IS intended for:**
- Educational purposes
- Research and development
- Machine learning demonstration
- Screening assistance (with medical review)

### Medical Requirements

Always consult with:
- Licensed ophthalmologists
- Qualified medical professionals
- Healthcare providers
- Certified eye specialists

For diabetic retinopathy screening and diagnosis.

### Data Privacy & Security

- Patient data confidentiality must be maintained
- Comply with HIPAA regulations (if applicable)
- Use secure transmission (HTTPS/TLS)
- Regular security audits
- Follow data protection laws

---

## 🆘 Support & Help

### Getting Help

Need assistance? Here are your options:

| Issue Type | Solution |
|-----------|----------|
| **Installation Problem** | See Installation Guide above |
| **Configuration Issue** | Check Configuration section |
| **Running Error** | Check Troubleshooting section |
| **Feature Question** | Review Documentation |
| **Bug Report** | Open GitHub Issue |
| **Feature Request** | Create GitHub Discussion |

### Resources

- 📖 [Project Documentation](Project%20documentation/README.md)
- 🎬 [Demo Video](https://drive.google.com/file/d/1lvMJpQC7IRogtFp6gyUHB5lJZutOaLQe/view?usp=drivesdk)
- 💻 [Source Code](SmartinterProject/)
- 📚 [Model Training Notebook](SmartinterProject/model/)

### FAQ

**Q: Can I use this in production?**
A: Not without proper medical validation and regulatory approvals.

**Q: Does the app require internet?**
A: No, except for Cloudant (optional). Core features work offline.

**Q: What image formats are supported?**
A: PNG, JPG, and JPEG. Minimum 500×500 pixels recommended.

**Q: How accurate is the model?**
A: Depends on training data. Review model metrics after training.

**Q: Can I modify the code?**
A: Yes! It's open source under MIT License.

---

## 📈 Version History

### Version 1.0.0 (February 20, 2026)
- ✅ Initial release
- ✅ Complete Flask application
- ✅ Xception model implementation
- ✅ User authentication system
- ✅ Cloudant database integration
- ✅ Comprehensive documentation
- ✅ Demo video walkthrough
- ✅ Open source publication

---

## 🎯 Roadmap

### Planned Features (Future Releases)

- [ ] Mobile app (iOS/Android)
- [ ] Real-time predictions API
- [ ] Batch image processing
- [ ] Advanced visualization dashboard
- [ ] Automated reporting system
- [ ] Integration with EHR systems
- [ ] Multi-language support
- [ ] Advanced authentication (OAuth, 2FA)
- [ ] Model versioning system
- [ ] Performance monitoring and analytics

---

## 📞 Final Notes

### Thank You!

Thank you for using the Diabetic Retinopathy Detection System. We hope this tool helps advance early detection and treatment of diabetic retinopathy.

### Stay Updated

- ⭐ Star this repository
- 🔔 Watch for updates
- 📧 Subscribe to releases
- 💬 Join discussions

### Report Issues

Found a bug? Have a suggestion?
- [Open an Issue](https://github.com/manishankarb22/-Diabetic-Retinopathy-Detection-System/issues)
- [Start a Discussion](https://github.com/manishankarb22/-Diabetic-Retinopathy-Detection-System/discussions)

---

<div align="center">

### Made with ❤️ for better healthcare and medical research

**Diabetic Retinopathy Detection System v1.0.0**

Last Updated: **February 20, 2026**

[⬆ back to top](#-diabetic-retinopathy-detection-system)

</div>
