# Diabetic Retinopathy Detection System

A modern web-based application for detecting diabetic retinopathy from retinal fundus images using deep learning and computer vision. This system uses a pre-trained Xception neural network model to classify diabetic retinopathy severity levels with high accuracy.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Model Information](#model-information)
- [Database Integration](#database-integration)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)
- [License](#license)

## 🏥 Overview

Diabetic Retinopathy is a serious diabetic complication that can lead to vision loss if not detected and treated early. This application leverages deep learning to automate the detection and classification of diabetic retinopathy severity levels, making screening more accessible and efficient.

The system can classify retinal images into 5 categories:
- **No DR**: No signs of diabetic retinopathy
- **Mild**: Mild diabetic retinopathy
- **Moderate**: Moderate diabetic retinopathy  
- **Severe**: Severe diabetic retinopathy
- **Proliferative DR**: Proliferative diabetic retinopathy (most advanced stage)

## ✨ Features

### Core Functionality
- 🖼️ **Image Upload and Analysis**: Upload retinal fundus images in PNG, JPG, or JPEG format
- 🧠 **Deep Learning Prediction**: Uses Xception convolutional neural network for accurate classification
- 📊 **Confidence Scores**: Displays prediction confidence percentage for transparency
- 👤 **User Authentication**: Secure login and registration system
- 📈 **Prediction History**: Track all previous predictions with timestamps
- 💾 **Database Integration**: Optional IBM Cloudant integration for secure data storage

### User Interface
- Modern, responsive web interface
- Real-time image preview
- Intuitive prediction results display
- User profile management
- About section with system information

### Security Features
- Session-based authentication
- File upload validation
- Secure filename handling
- Maximum upload file size limit (16MB)

## 🏗️ System Architecture

```
┌─────────────────┐
│   Web Browser   │
└────────┬────────┘
         │
    HTTP/HTTPS
         │
┌────────▼────────────────────┐
│   Flask Web Application     │
│  - Authentication           │
│  - Route Handling           │
│  - File Upload Processing   │
└────────┬────────────────────┘
         │
    ┌────▼────────────────┐
    │                     │
    ▼                     ▼
┌─────────┐      ┌──────────────┐
│  Model  │      │  Cloudant DB │
│Prediction│      │  (Optional)  │
└─────────┘      └──────────────┘
```

## 📁 Project Structure

```
SmartinterProject/
├── app.py                          # Main Flask application
├── inception-diabetic.h5           # Pre-trained Xception model
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
│
├── static/                         # Static assets
│   ├── css/
│   │   └── style.css              # Styling for the application
│   └── images/                    # Image assets
│
├── templates/                      # HTML templates
│   ├── index.html                 # Home page
│   ├── login.html                 # Login page
│   ├── register.html              # Registration page
│   ├── prediction.html            # Prediction results page
│   ├── history.html               # Prediction history page
│   ├── about.html                 # About page
│   ├── 404.html                   # 404 error page
│   └── 500.html                   # 500 error page
│
├── model/                          # Model-related files
│   └── Xception_Diabetic_retinopathy.ipynb  # Model training notebook
│
├── uploads/                        # User-uploaded images (created at runtime)
│
└── Project documentation/          # Documentation files
```

## 🛠️ Tech Stack

### Backend Framework
- **Flask 2.3.0**: Lightweight Python web framework
- **Python 3.8+**: Programming language

### Machine Learning & Image Processing
- **TensorFlow 2.20.0**: Deep learning framework
- **Keras**: Neural network API (built into TensorFlow)
- **NumPy 2.1.3**: Numerical computing library
- **Pandas 2.2.0**: Data manipulation library
- **Pillow 11.0.0**: Image processing library

### Database (Optional)
- **IBM Cloudant**: NoSQL cloud database
- **Cloudant Python Client 2.15.0**: Database connector

### Utilities
- **Werkzeug 2.3.0**: WSGI utilities for file handling
- **python-dateutil 2.8.2**: Date/time utilities
- **requests 2.31.0**: HTTP library
- **python-dotenv 0.19.2**: Environment variable management

### Frontend
- **HTML5**: Page structure
- **CSS3**: Styling with modern features
- **Font Awesome 6.5.0**: Icon library
- **Google Fonts**: Inter & JetBrains Mono fonts

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/manishankarb22/-Diabetic-Retinopathy-Detection-System.git
cd SmartinterProject
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create Uploads Directory
```bash
mkdir uploads
```

### Step 5: Run the Application
```bash
python app.py
```

The application will start at `http://localhost:5000`

## ⚙️ Configuration

### Flask Configuration
Edit the following in `app.py` to customize:

```python
# Change secret key for production
app.secret_key = 'your-secret-key-here'

# Upload settings
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

# Model settings
MODEL_PATH = 'inception-diabetic.h5'
IMG_HEIGHT = 224
IMG_WIDTH = 224

# Class names
CLASS_NAMES = ['No DR', 'Mild', 'Moderate', 'Severe', 'Proliferative DR']
```

### Environment Variables (Optional)
Create a `.env` file for Cloudant credentials:
```
CLOUDANT_USERNAME=your_username
CLOUDANT_API_KEY=your_api_key
CLOUDANT_URL=your_cloudant_url
```

### GPU Support (Optional)
For GPU acceleration with CUDA:
```bash
pip install tensorflow[and-cuda]
```

## 💻 Usage

### 1. Register an Account
- Navigate to the Register page
- Fill in username, email, and password
- Click "Register" to create account

### 2. Login
- Enter your credentials
- Click "Login" button

### 3. Upload Image for Prediction
- Click on "Predict" from the navigation menu
- Select a retinal fundus image (PNG, JPG, or JPEG)
- Click "Upload and Predict"
- View the prediction result with confidence score

### 4. View Prediction History
- Click on "History" to see all previous predictions
- Results are sorted by most recent first
- (Requires Cloudant database to be configured)

### 5. Logout
- Click the "Logout" button to end your session

## 📡 API Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|------------------|
| GET | `/` | Home page | Required |
| GET/POST | `/login` | User login | Not required |
| GET/POST | `/register` | User registration | Not required |
| GET | `/logout` | User logout | Required |
| GET/POST | `/predict` | Upload image & get prediction | Required |
| GET | `/history` | View prediction history | Required |
| GET | `/about` | About page | Not required |
| GET | `/uploads/<filename>` | Serve uploaded image | Required |

## 🧠 Model Information

### Model Architecture
- **Model Type**: Xception (Modified Aligned Xception)
- **Input Size**: 224 × 224 × 3 (RGB images)
- **Output Classes**: 5 (DR severity levels)
- **File**: `inception-diabetic.h5`

### Model Training
- **Framework**: TensorFlow/Keras
- **Training Notebook**: `model/Xception_Diabetic_retinopathy.ipynb`
- **Preprocessing**: Image normalization (0-255 → 0-1)
- **Prediction Method**: Softmax activation with argmax selection

### Model Performance Metrics
(Add your specific metrics here after training)
- Accuracy: TBD
- Sensitivity: TBD
- Specificity: TBD

## 💾 Database Integration

### IBM Cloudant Setup (Optional)

To enable database functionality for storing predictions:

1. **Create Cloudant Instance**
   - Sign up for [IBM Cloud](https://cloud.ibm.com)
   - Create a Cloudant service instance
   - Note your credentials

2. **Update Configuration**
   ```python
   # In app.py, update:
   CLOUDANT_USERNAME = "your-username"
   CLOUDANT_API_KEY = "your-api-key"
   CLOUDANT_URL = "your-url"
   ```

3. **Enable in Code**
   ```python
   # Uncomment in app.py main block:
   init_cloudant()
   ```

### Document Structure
```json
{
  "_id": "auto-generated",
  "username": "user123",
  "image_name": "20260220_085312_image.jpg",
  "prediction": "Moderate",
  "confidence": 0.9234,
  "timestamp": "2026-02-20T08:53:12.123456",
  "type": "prediction"
}
```

## 📄 File Descriptions

### Core Application
- **app.py**: Main Flask application containing:
  - Route definitions
  - Image prediction logic
  - User authentication
  - Database integration
  - Error handlers

### Templates
- **index.html**: Home page with navigation and modern UI
- **login.html**: User login form
- **register.html**: User registration form
- **prediction.html**: Displays prediction results with confidence
- **history.html**: Shows prediction history from database
- **about.html**: Project information and details

### Static Assets
- **style.css**: Complete UI styling with responsive design
- **images/**: Logo and icon assets

### Model Files
- **inception-diabetic.h5**: Pre-trained Xception model (weights + architecture)
- **model/Xception_Diabetic_retinopathy.ipynb**: Jupyter notebook with:
  - Dataset loading
  - Model architecture definition
  - Training process
  - Evaluation metrics
  - Model export

### Configuration
- **requirements.txt**: All Python package dependencies
- **.gitignore**: Git ignore patterns for Python projects

## 🔒 Security Considerations

### Current Implementation
- Basic session-based authentication
- File upload validation (extension checking)
- Secure filename handling via werkzeug
- Maximum file size limits

### Recommendations for Production
1. **Password Security**
   - Hash passwords using werkzeug.security or bcrypt
   - Implement password strength validation
   - Add password reset functionality

2. **Database Security**
   - Use environment variables for credentials
   - Enable Cloudant CORS restrictions
   - Implement fine-grained access control

3. **Web Application**
   - Use HTTPS/TLS encryption
   - Implement CSRF protection
   - Add rate limiting for API endpoints
   - Enable input sanitization

4. **Model Security**
   - Validate image format before processing
   - Implement antivirus scanning for uploads
   - Monitor model performance for drift

## 🧪 Testing

### Test Image Requirements
- Format: PNG, JPG, or JPEG
- Size: Recommended 500×500px or larger
- Content: Fundus photography (retinal images)
- File size: Under 16MB

### Manual Testing Steps
1. Register a new account
2. Upload test retinal image
3. Verify prediction output
4. Check image is saved in uploads folder
5. View prediction in history

## 🐛 Troubleshooting

### Model Loading Error
```
Error loading model: inception-diabetic.h5
```
**Solution**: Ensure `inception-diabetic.h5` is in the project root directory with proper TensorFlow version

### File Upload Failed
```
No file uploaded! or Invalid file type!
```
**Solution**: Check file format (must be PNG, JPG, JPEG) and size (< 16MB)

### Cloudant Connection Error
```
Cloudant connection error
```
**Solution**: Verify credentials in `app.py` or disable Cloudant features (app works without DB)

### Port Already in Use
```
Address already in use
```
**Solution**: Change port in `app.py` or kill process using port 5000

## 📚 References & Resources

### Medical Background
- [Diabetic Retinopathy - WHO](https://www.who.int/health-topics/diabetic-retinopathy)
- [DR Classification System](https://www.aao.org/)

### Deep Learning & Implementation
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Xception Architecture Paper](https://arxiv.org/abs/1610.02357)
- [Flask Documentation](https://flask.palletsprojects.com/)

### Datasets
- [Kaggle: Diabetic Retinopathy Detection](https://www.kaggle.com/c/diabetic-retinopathy-detection)
- [APTOS 2019: Blindness Detection](https://www.kaggle.com/c/aptos2019-blindness-detection)

## 👥 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License - see LICENSE file for details.

## 👨‍💻 Author

**Manisha Nkarb**
- GitHub: [@manishankarb22](https://github.com/manishankarb22)
- Email: manishankarb22@example.com

## ⚠️ Disclaimer

**IMPORTANT**: This system is intended for educational and research purposes only. It should NOT be used for clinical diagnosis or treatment decisions without proper medical supervision and validation by licensed healthcare professionals. Always consult with an ophthalmologist or qualified medical professional for diabetic retinopathy screening and diagnosis.

## 🙏 Acknowledgments

- Deep learning community and frameworks (TensorFlow, Keras)
- IBM Cloud for database services
- Open-source contributors and researchers
- Medical imaging datasets providers

## 📧 Contact & Support

For questions, issues, or suggestions, please:
- Open an issue on GitHub
- Contact the developer directly
- Check project documentation

---

**Last Updated**: February 20, 2026  
**Version**: 1.0.0  
**Status**: Active Development
