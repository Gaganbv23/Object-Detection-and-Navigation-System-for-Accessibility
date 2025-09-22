# Step 1: Install required libraries
# Run this in your terminal or command prompt:
# pip install transformers torch pillow gtts gradio opencv-python

# Step 2: Import libraries
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from gtts import gTTS
import cv2
import time
import gradio as gr
import os
import threading

# Step 3: Load the BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Step 4: Function to generate a caption and convert it to speech
def image_to_voice(image):
    # Generate a textual description
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)

    # Convert the caption to speech
    tts = gTTS(caption, lang='en')
    audio_file = "output.mp3"
    tts.save(audio_file)

    # Return the caption and audio file path
    return caption, audio_file

# Step 5: Function to capture images from the camera
def capture_frame():
    # Initialize the camera
    cap = cv2.VideoCapture(0)  # 0 is the default camera

    if not cap.isOpened():
        return None, "Error: Could not open camera."

    # Capture an image from the camera
    ret, frame = cap.read()
    if not ret:
        return None, "Error: Could not capture image."

    # Convert the frame to a PIL image
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Release the camera
    cap.release()

    return image, None

# Step 6: Function to periodically capture and process frames
def periodic_capture():
    while True:
        # Capture and process a frame
        image, error = capture_frame()
        if not error:
            caption, audio_file = image_to_voice(image)
            print("Generated Caption:", caption)
            os.system(f"start {audio_file}")  # Play the audio (Windows)
            # os.system(f"afplay {audio_file}")  # Play the audio (macOS)
            # os.system(f"mpg321 {audio_file}")  # Play the audio (Linux)

        # Wait for 10 seconds
        time.sleep(10)

# Step 7: Gradio interface for real-time camera feed and voice output
def gradio_interface():
    def process_frame():
        # Capture a frame from the camera
        image, error = capture_frame()
        if error:
            return error, None

        # Generate a caption and voice output
        caption, audio_file = image_to_voice(image)
        return caption, audio_file

    # Gradio interface
    with gr.Blocks() as demo:
        gr.Markdown("# Image to Voice for Blind People")
        gr.Markdown("This app captures images from your camera every 10 seconds, describes them, and provides voice output.")

        with gr.Row():
            caption_output = gr.Textbox(label="Generated Caption")
            audio_output = gr.Audio(label="Audio Output", type="filepath")

        # Add a button to manually trigger frame capture
        capture_button = gr.Button("Capture and Describe")

        # Set up the button click event
        capture_button.click(
            fn=process_frame,
            outputs=[caption_output, audio_output],
        )

    # Launch the Gradio app
    demo.launch()

# Step 8: Start the periodic capture thread
thread = threading.Thread(target=periodic_capture, daemon=True)
thread.start()

# Step 9: Run the Gradio interface
if _name_ == "_main_":
    gradio_interface()
