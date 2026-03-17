# VisionBuddy 

An AI-powered vision assistance app that helps visually impaired users navigate the world through voice descriptions. VisionBuddy uses NVIDIA's AI models to analyze images and provide conversational audio descriptions.

##  Project Overview

VisionBuddy is a cross-platform accessibility app consisting of:
- **Flutter Mobile App**: Captures photos and provides text-to-speech functionality
- **FastAPI Backend**: Processes images using NVIDIA AI models
- **NVIDIA AI Integration**: Leverages NVIDIA NIMs for computer vision and language processing

##  Architecture

```
VisionBuddy/
├── vision_buddy_app/          # Flutter mobile application
│   ├── lib/
│   │   ├── screens/           # UI screens
│   │   ├── services/          # Business logic
│   │   └── widgets/           # Reusable UI components
│   └── android/               # Android-specific configurations
├── backend/                   # FastAPI server
│   ├── main.py               # API endpoints
│   ├── vision.py             # NVIDIA AI integration
│   ├── utils.py              # Utility functions
│   └── test_nvidia.py        # API testing
└── .env                      # Environment variables
```

##  Technology Stack

### Mobile App (Flutter)
- **Framework**: Flutter 3.11.1
- **Language**: Dart
- **Key Dependencies**:
  - `camera: ^0.10.5+9` - Camera functionality
  - `flutter_tts: ^3.8.5` - Text-to-speech
  - `http: ^1.1.0` - API communication
  - `permission_handler: ^11.0.1` - Device permissions
  - `image: ^4.1.3` - Image processing

### Backend (Python)
- **Framework**: FastAPI
- **Language**: Python 3.14.3
- **Key Dependencies**:
  - `fastapi` - Web framework
  - `uvicorn` - ASGI server
  - `openai` - NVIDIA API client
  - `pillow` - Image processing
  - `python-multipart` - File upload support

### AI Integration
- **NVIDIA NIMs**: Computer vision and language models
- **Models Used**:
  - `nvidia/nemotron-mini-4b-instruct` - Text generation
  - Vision models for image analysis

##  Features

### Current Features
- **Camera Integration**: Capture photos using device camera
- **Image Analysis**: Process images with NVIDIA AI models
- **Text-to-Speech**: Convert descriptions to audio
- **Multiple Analysis Modes**:
  - General description
  - Medical assistance
  - Navigation help
  - Text reading
  - Money identification
- **RESTful API**: FastAPI backend with CORS support
- **Cross-Platform**: Flutter app for iOS/Android

### API Endpoints
- `GET /` - Health check
- `GET /health` - Service status
- `POST /analyze` - Full image analysis with enhanced descriptions
- `POST /analyze/quick` - Fast image analysis (no enhancement)

## Mobile App Features

### Permissions Required
- **Camera**: Capture photos for analysis
- **Internet**: Communicate with backend API
- **Audio Recording**: For voice commands (future feature)

### UI Components
- Dark theme optimized for accessibility
- Large, accessible buttons
- Voice feedback for all interactions
- Camera preview with capture functionality

## Setup Instructions

### Prerequisites
- Python 3.14+ with virtual environment
- Flutter SDK 3.11.1+
- NVIDIA API key
- Android Studio (for Android development)
- Xcode (for iOS development, macOS only)

### Backend Setup

1. **Clone and navigate to project**:
   ```bash
   cd /path/to/visionbuddy/backend
   ```

2. **Activate virtual environment**:
   ```bash
   source ../.venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn openai pillow python-multipart
   ```

4. **Set up environment variables**:
   Create `.env` file in project root:
   ```
   NVIDIA_API_KEY=your_nvidia_api_key_here
   ```

5. **Run the server**:
   ```bash
   python main.py
   ```
   Server runs on `http://localhost:8000`

### Flutter App Setup

1. **Navigate to Flutter project**:
   ```bash
   cd /path/to/visionbuddy/vision_buddy_app
   ```

2. **Install dependencies**:
   ```bash
   flutter pub get
   ```

3. **Run on device/emulator**:
   ```bash
   flutter run
   ```

## Testing

### Backend Testing
- `test_nvidia.py` - Tests NVIDIA API integration
- `simple_test.py` - Basic API connectivity tests
- `debug_test.py` - Environment and dependency validation

### Test NVIDIA Integration
```bash
cd backend
python test_nvidia.py
```

Expected output: AI-generated response from NVIDIA model

## Environment Configuration

### Required Environment Variables
```bash
# .env file
NVIDIA_API_KEY=nvapi-xxxxxxxxxxxxxxxx
```

### Virtual Environment Setup
The project uses Python virtual environment located at:
- Main environment: `.venv/`
- Legacy environment: `venv/`

## Project Structure Details

### Backend (`/backend/`)
- **`main.py`**: FastAPI application with CORS middleware
- **`vision.py`**: NVIDIA AI model integration (currently empty - needs implementation)
- **`utils.py`**: Image processing utilities (base64 conversion, compression)
- **`test_nvidia.py`**: NVIDIA API testing and validation

### Flutter App (`/vision_buddy_app/`)
- **`lib/main.dart`**: App entry point with dark theme
- **`lib/screens/home_screen.dart`**: Main user interface
- **`lib/services/`**: Business logic services
  - `vision_service.dart`: Backend API communication
  - `tts_service.dart`: Text-to-speech functionality
- **`android/app/src/main/AndroidManifest.xml`**: Android permissions and configuration

##  Current Status

###  Completed
- [x] FastAPI backend with image analysis endpoints
- [x] Flutter app with camera integration
- [x] NVIDIA API integration setup
- [x] Text-to-speech functionality
- [x] Cross-platform mobile app structure
- [x] Environment configuration
- [x] Basic image processing utilities

###  In Progress
- [ ] Complete NVIDIA vision model integration in `vision.py`
- [ ] Implement enhanced description generation
- [ ] Add error handling and user feedback
- [ ] UI/UX improvements for accessibility

###  TODO
- [ ] Complete image analysis pipeline
- [ ] Add offline mode capabilities
- [ ] Implement user preferences
- [ ] Add multiple language support
- [ ] Performance optimizations
- [ ] Comprehensive testing suite
- [ ] App store deployment preparation

##  Contributing

This is an accessibility-focused project. Contributions should prioritize:
1. **Accessibility**: Voice feedback, large UI elements, screen reader compatibility
2. **Performance**: Fast image processing and response times
3. **Reliability**: Robust error handling and offline capabilities
4. **Privacy**: Minimal data collection, local processing where possible

##  License

This project is developed as an accessibility tool. Please ensure any usage complies with NVIDIA's API terms of service.

##  Support

For issues or questions:
1. Check the test files for API connectivity
2. Verify environment variables are set correctly
3. Ensure all dependencies are installed in the virtual environment
4. Test NVIDIA API access with `test_nvidia.py`

---

**Last Updated**: March 16, 2026
**Version**: 1.0.0
**Status**: Development Phase
