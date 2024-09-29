
import speech_recognition as sr
from fuzzywuzzy import fuzz
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import cmudict
import os
from difflib import SequenceMatcher

def ensure_nltk_resources():
    """Ensure all required NLTK resources are downloaded"""
    resources = ['punkt', 'cmudict']
    for resource in resources:
        try:
            nltk.data.find(f'tokenizers/{resource}')
            print(f"{resource} is already downloaded.")
        except LookupError:
            print(f"Downloading {resource}...")
            nltk.download(resource, quiet=True)
    
    # Explicitly download punkt_tab
    try:
        nltk.data.find('tokenizers/punkt_tab')
        print("punkt_tab is already downloaded.")
    except LookupError:
        print("Downloading punkt_tab...")
        nltk.download('punkt_tab', quiet=True)
    
    print("All required NLTK resources are available.")

# Set NLTK data path
nltk.data.path.append(os.path.join(os.getcwd(), 'nltk_data'))

# Ensure NLTK resources are available before proceeding
ensure_nltk_resources()

recognizer = sr.Recognizer()
mic = sr.Microphone()

# Load CMU Pronouncing Dictionary
try:
    pronouncing_dict = cmudict.dict()
except LookupError:
    print("Error: CMU Pronouncing Dictionary not found. Please ensure it's downloaded.")
    pronouncing_dict = {}

def recognize_speech_live(callback):
    """Listen to speech and transcribe it in real time"""
    with mic as source:
        print("Listening for live transcription...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("No speech detected")
            callback("No speech detected. Please try again.")
            return

    try:
        # Use Google's speech recognition
        recognized_text = recognizer.recognize_google(audio)
        print(f"Recognized: {recognized_text}")
        callback(recognized_text)
    except sr.UnknownValueError:
        print("Speech not understood")
        callback("Speech not understood. Please try again.")
    except sr.RequestError as e:
        print(f"API error: {e}")
        callback(f"Error: {e}")

def compare_pronunciation(user_text, target_text):
    if user_text is None or user_text.startswith("No speech detected") or user_text.startswith("Speech not understood"):
        return user_text, []

    try:
        # Tokenize the texts
        user_words = word_tokenize(user_text.lower())
        target_words = word_tokenize(target_text.lower())
        
        # Calculate similarity ratio using fuzzy matching
        similarity = fuzz.token_sort_ratio(user_text.lower(), target_text.lower()) / 100

        incorrect_words = []

        for i, target_word in enumerate(target_words):
            if i < len(user_words):
                user_word = user_words[i]
                
                # Check exact pronunciation with CMU dictionary
                if target_word in pronouncing_dict and user_word in pronouncing_dict:
                    target_phonemes = pronouncing_dict[target_word][0]
                    user_phonemes = pronouncing_dict[user_word][0]
                    
                    if target_phonemes != user_phonemes:
                        incorrect_words.append(target_word)
                # Apply fuzzy matching for non-exact words
                elif fuzz.ratio(target_word, user_word) < 80:
                    incorrect_words.append(target_word)
                else:
                    # If the words are close enough, consider them correct
                    similarity_score = SequenceMatcher(None, target_word, user_word).ratio()
                    if similarity_score < 0.85:  # Adjust the similarity threshold for tolerance
                        incorrect_words.append(target_word)
            else:
                incorrect_words.append(target_word)  # Remaining target words that aren't in the user speech

        # Adjust feedback based on similarity threshold
        if similarity == 1.0:
            return "Good pronunciation!", incorrect_words
        elif 0.8 < similarity < 1.0:
            return "Improvement required. Focus on the highlighted words.", incorrect_words
        else:
            return "Pronunciation was incorrect. Need improvement", incorrect_words
    except Exception as e:
        print(f"Error in compare_pronunciation: {e}")
        return "Error in pronunciation comparison.", []
    
if __name__ == "__main__":
    print("NLTK resources checked and downloaded if necessary.")
    print("You can now run the UI script to start the application.")