import tkinter as tk
from tkinter import messagebox
from main import recognize_speech_live, compare_pronunciation

# Initialize the Tkinter window
root = tk.Tk()
root.title("Pronunciation Assessment")
root.geometry("600x400")  # Set window size

# Function to process real-time speech recognition and update UI
def check_pronunciation():
    target_text = text_target.get("1.0", "end-1c").strip()  # Retrieve sentence from Text widget
    if not target_text:
        messagebox.showinfo("Input Error", "Please enter a sentence.")
        return
    
    # Set label_feedback text to "Listening..."
    label_feedback.config(text="Listening...", fg="blue")

    # Recognize speech in real-time and update the transcription
    def on_transcription_complete(transcribed_text):
        update_transcription(transcribed_text)

    recognize_speech_live(on_transcription_complete)

def update_transcription(transcribed_text):
    """Callback function to update the transcription box in real time"""
    text_transcription.delete("1.0", "end")  # Clear previous transcription
    text_transcription.insert("1.0", transcribed_text)  # Insert transcribed text
    
    # Fetch target text for comparison
    target_text = text_target.get("1.0", "end-1c").strip()

    # Compare pronunciation and provide feedback
    feedback = compare_pronunciation(transcribed_text, target_text)
    label_feedback.config(text=feedback, fg="red")  # Update feedback after listening

# UI Components

# Instruction Label
label_instruction = tk.Label(root, text="Enter a sentence, press Record, and check your pronunciation.", font=("Helvetica", 12))
label_instruction.pack(pady=10)

# Target Sentence Label
label_target = tk.Label(root, text="Target Sentence:", font=("Helvetica", 10))
label_target.pack()

# Target Sentence Text Box (multi-line input)
text_target = tk.Text(root, height=10, width=80, font=("Helvetica", 12))
text_target.pack(pady=10)

# Transcription Label
label_transcription = tk.Label(root, text="Real-Time Transcription:", font=("Helvetica", 10))
label_transcription.pack()

# Transcription Output Text Box (display recognized text in real time)
text_transcription = tk.Text(root, height=10, width=80, font=("Helvetica", 12), state="normal")
text_transcription.pack(pady=10)

# Record Button
button_record = tk.Button(root, text="Record", command=check_pronunciation, bg="#4CAF50", fg="white", font=("Helvetica", 12), height=2, width=20)
button_record.pack(pady=10)

# Feedback Label (provides pronunciation correctness and "Listening" status)
label_feedback = tk.Label(root, text="", font=("Helvetica", 14), fg="red")
label_feedback.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
