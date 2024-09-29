import tkinter as tk
from tkinter import messagebox
from main import recognize_speech_live, compare_pronunciation

# Initialize the Tkinter window
root = tk.Tk()
root.title("Pronunciation Assessment")
root.geometry("600x400")

def check_pronunciation():
    target_text = text_target.get("1.0", "end-1c").strip()  
    if not target_text:
        messagebox.showinfo("Input Error", "Please enter a sentence.")
        return

    # Recognize speech in real-time and update the transcription
    def on_transcription_complete(transcribed_text):
        update_transcription(transcribed_text)

    recognize_speech_live(on_transcription_complete)

def update_transcription(transcribed_text):
    """Callback function to update the transcription box in real time"""
    text_transcription.delete("1.0", "end")  # Clear previous transcription
    text_transcription.insert("1.0", transcribed_text)  # Insert transcribed text
    
    target_text = text_target.get("1.0", "end-1c").strip()
    feedback, incorrect_words = compare_pronunciation(transcribed_text, target_text)

    # Update feedback message
    label_feedback.config(text=feedback, fg="red")  

    # Highlight incorrect words in the target text
    highlight_incorrect_words(target_text, incorrect_words)

def highlight_incorrect_words(target_text, incorrect_words):
    """Highlight incorrect words in the target text"""
    text_target.delete("1.0", "end")  # Clear previous target text
    text_target.insert("1.0", target_text)  # Insert original target text

    # Apply red underline to incorrect words
    for word in incorrect_words:
        start_idx = target_text.lower().find(word.lower())
        end_idx = start_idx + len(word)

        if start_idx != -1:
            text_target.tag_add("incorrect", "1.0 + {} chars".format(start_idx), "1.0 + {} chars".format(end_idx))

    # Configure the tag to have a red underline
    text_target.tag_config("incorrect", underline=True, foreground="red")

# UI Components
label_instruction = tk.Label(root, text="Enter a sentence, press Record, and check your pronunciation.", font=("Helvetica", 12))
label_instruction.pack(pady=10)

label_target = tk.Label(root, text="Target Sentence:", font=("Helvetica", 10))
label_target.pack()

text_target = tk.Text(root, height=10, width=80, font=("Helvetica", 12))
text_target.pack(pady=10)

label_transcription = tk.Label(root, text="Real-Time Transcription:", font=("Helvetica", 10))
label_transcription.pack()

text_transcription = tk.Text(root, height=10, width=80, font=("Helvetica", 12), state="normal")
text_transcription.pack(pady=10)

button_record = tk.Button(root, text="Record", command=check_pronunciation, bg="#4CAF50", fg="white", font=("Helvetica", 12), height=2, width=20)
button_record.pack(pady=10)

label_feedback = tk.Label(root, text="", font=("Helvetica", 14), fg="red")
label_feedback.pack(pady=10)

root.mainloop()
