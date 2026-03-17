import 'dart:convert';
import 'package:http/http.dart' as http;

class VisionService {
  // ⚠️ CHANGE THIS to your laptop IP at hackathon
  // Run: ipconfig (Windows) or ifconfig (Mac) to find it
<<<<<<< HEAD
  static const String baseUrl = 'http://localhost:8000';
=======
  static const String baseUrl = 'http://192.168.1.100:8000';
>>>>>>> origin/main

  static Future<String> analyzeImage({
    required String base64Image,
    String mode = 'general',
  }) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/analyze'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'image': base64Image,
          'mode': mode,
        }),
      ).timeout(Duration(seconds: 15));

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        return data['description'];
      } else {
        return 'Sorry, I could not analyze the image. Please try again.';
      }
    } catch (e) {
      return 'Connection error. Please check your internet connection.';
    }
  }
}