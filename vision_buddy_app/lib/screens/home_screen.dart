import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  CameraController? _cameraController;
  FlutterTts _tts = FlutterTts();
  bool _isAnalyzing = false;
  String _lastDescription = "Point camera at something and tap the button";
  String _selectedMode = "general";

  final List<Map<String, dynamic>> _modes = [
    {"key": "general",    "label": "🌍 General",   "color": Colors.blue},
    {"key": "medicine",   "label": "💊 Medicine",  "color": Colors.red},
    {"key": "navigation", "label": "🚶 Navigate",  "color": Colors.green},
    {"key": "text",       "label": "📄 Read Text", "color": Colors.orange},
    {"key": "money",      "label": "💵 Money",     "color": Colors.purple},
  ];

  @override
  void initState() {
    super.initState();
    _initTTS();
    _initCamera();
  }

  Future<void> _initTTS() async {
    await _tts.setLanguage("en-US");
    await _tts.setSpeechRate(0.45);
    await _tts.setVolume(1.0);
    await _tts.setPitch(1.0);
    await _tts.speak("VisionBuddy is ready. Tap the green button to analyze your surroundings.");
  }

  Future<void> _speak(String text) async {
    await _tts.stop();
    await _tts.speak(text);
  }

  Future<void> _initCamera() async {
    final cameras = await availableCameras();
    if (cameras.isEmpty) return;
    _cameraController = CameraController(
      cameras.first,
      ResolutionPreset.medium,
      enableAudio: false,
    );
    await _cameraController!.initialize();
    if (mounted) setState(() {});
  }

  Future<void> _captureAndAnalyze() async {
    if (_isAnalyzing || _cameraController == null) return;
    setState(() => _isAnalyzing = true);
    await _speak("Analyzing...");
    try {
      final image = await _cameraController!.takePicture();
      final bytes = await image.readAsBytes();
      final base64Image = base64Encode(bytes);
      final response = await http.post(
        Uri.parse('http://localhost:8000/analyze'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'image': base64Image,
          'mode': _selectedMode,
        }),
      ).timeout(Duration(seconds: 15));
      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        final description = data['description'];
        setState(() => _lastDescription = description);
        await _speak(description);
      } else {
        await _speak("Sorry, I could not analyze the image. Please try again.");
      }
    } catch (e) {
      await _speak("Connection error. Please check your connection.");
      setState(() => _lastDescription = "Error: $e");
    } finally {
      setState(() => _isAnalyzing = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: SafeArea(
        child: Column(
          children: [
            Padding(
              padding: EdgeInsets.all(12),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(Icons.visibility, color: Colors.green, size: 28),
                  SizedBox(width: 8),
                  Text("VisionBuddy",
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 24,
                      fontWeight: FontWeight.bold
                    ),
                  ),
                ],
              ),
            ),
            Expanded(
              flex: 5,
              child: _cameraController?.value.isInitialized == true
                ? ClipRRect(
                    borderRadius: BorderRadius.circular(16),
                    child: CameraPreview(_cameraController!),
                  )
                : Center(child: CircularProgressIndicator(color: Colors.green)),
            ),
            Container(
              height: 50,
              margin: EdgeInsets.symmetric(vertical: 8),
              child: ListView.builder(
                scrollDirection: Axis.horizontal,
                padding: EdgeInsets.symmetric(horizontal: 12),
                itemCount: _modes.length,
                itemBuilder: (ctx, i) {
                  final mode = _modes[i];
                  final selected = _selectedMode == mode["key"];
                  return GestureDetector(
                    onTap: () {
                      setState(() => _selectedMode = mode["key"]);
                      _speak("${mode["label"]} mode selected");
                    },
                    child: Container(
                      margin: EdgeInsets.only(right: 8),
                      padding: EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                      decoration: BoxDecoration(
                        color: selected ? mode["color"] : Colors.grey[800],
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: Text(
                        mode["label"],
                        style: TextStyle(
                          color: Colors.white,
                          fontWeight: selected ? FontWeight.bold : FontWeight.normal,
                        ),
                      ),
                    ),
                  );
                },
              ),
            ),
            Container(
              margin: EdgeInsets.symmetric(horizontal: 16),
              padding: EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Colors.grey[900],
                borderRadius: BorderRadius.circular(12),
              ),
              child: Row(
                children: [
                  Expanded(
                    child: Text(
                      _lastDescription,
                      style: TextStyle(color: Colors.white, fontSize: 14),
                      maxLines: 4,
                      overflow: TextOverflow.ellipsis,
                    ),
                  ),
                  IconButton(
                    icon: Icon(Icons.volume_up, color: Colors.green),
                    onPressed: () => _speak(_lastDescription),
                  )
                ],
              ),
            ),
            GestureDetector(
              onTap: _captureAndAnalyze,
              child: Container(
                margin: EdgeInsets.all(20),
                width: 90,
                height: 90,
                decoration: BoxDecoration(
                  color: _isAnalyzing ? Colors.grey : Colors.green,
                  shape: BoxShape.circle,
                  boxShadow: [
                    BoxShadow(
                      color: Colors.green.withOpacity(0.4),
                      blurRadius: 20,
                      spreadRadius: 5,
                    )
                  ],
                ),
                child: Icon(
                  _isAnalyzing ? Icons.hourglass_top : Icons.camera_alt,
                  color: Colors.white,
                  size: 40,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _cameraController?.dispose();
    _tts.stop();
    super.dispose();
  }
}

