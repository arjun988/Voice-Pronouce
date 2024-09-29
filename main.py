import speech_recognition as sr
import difflib

recognizer = sr.Recognizer()
mic = sr.Microphone()

def recognize_speech_live(callback):
    """Listen to speech and transcribe it in real time"""
    with mic as source:
        print("Listening for live transcription...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio)
        print(f"Recognized: {recognized_text}")
        callback(recognized_text)  # Call the callback to update UI in real-time
    except sr.UnknownValueError:
        print("Speech not understood")
        callback("Speech not understood")
    except sr.RequestError as e:
        print(f"API error: {e}")
        callback(f"Error: {e}")

def compare_pronunciation(user_text, target_text):
    if user_text is None:
        return "No input received."
    
    # Calculate similarity ratio between the recognized text and the target text
    similarity = difflib.SequenceMatcher(None, user_text.lower(), target_text.lower()).ratio()
    if similarity > 0.8:
        return "Good pronunciation!"
    else:
        return "Incorrect pronunciation. Try again."
