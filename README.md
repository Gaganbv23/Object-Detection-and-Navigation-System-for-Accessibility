# Object Detection and Navigation System for Accessibility

This project is a real-time accessibility tool designed to assist visually impaired users. It captures images through a camera, generates descriptive captions using BLIP (Bootstrapped Language-Image Pretraining), and converts those captions into speech with gTTS (Google Text-to-Speech). The system provides automated audio feedback every few seconds, enabling users to better perceive their surroundings.

---

## ✨ Features

* **Real-time Image Captioning**: Uses BLIP for generating human-readable captions from live camera feed.
* **Voice Assistance**: Captions are converted to speech with gTTS and played automatically.
* **Periodic Capture**: Continuously captures frames at set intervals (default: 10 seconds).
* **Manual Control**: Users can trigger a capture and description through a simple Gradio web interface.
* **Cross-platform Audio Support**: Compatible with Windows, macOS, and Linux.

---

## 🛠️ Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/object-detection-accessibility.git
   cd object-detection-accessibility
   ```

2. Install required dependencies:

   ```bash
   pip install transformers torch pillow gtts gradio opencv-python
   ```

---

## 🚀 Usage

1. Run the Python script:

   ```bash
   python main.py
   ```

2. The system will:

   * Capture images from your camera.
   * Generate descriptive captions.
   * Convert them to speech and play audio.
   * Provide a Gradio interface to manually capture frames.

---

## 📂 Project Structure

* **main.py** → Core application (camera input, captioning, speech).
* **requirements.txt** → List of required Python libraries.

---

## 🌍 Future Enhancements

* Object detection for obstacle avoidance.
* Navigation assistance with direction indicators.
* Support for multiple languages.

---

## 📜 License

This project is licensed under the MIT License.

---
