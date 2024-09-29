# Pronunciation Assessment Application

Welcome to the **Pronunciation Assessment Application**! This project is designed to help users improve their pronunciation skills through real-time speech recognition and feedback. Built using Python and Tkinter, it provides an interactive way for users to practice speaking sentences and receive instant feedback on their pronunciation accuracy.

## Features

- **Real-Time Transcription**: The application listens as the user speaks and transcribes their speech into text immediately.
- **Pronunciation Feedback**: Users receive detailed feedback comparing their speech to a target sentence, helping them identify areas for improvement.
- **User-Friendly Interface**: The intuitive design ensures that users can easily navigate the application and focus on their practice.

## Technologies Used

- **Python**: The core programming language for implementing the application logic.
- **Tkinter**: A powerful GUI toolkit for creating a responsive desktop application.
- **SpeechRecognition**: A library for enabling speech recognition functionality.
- **Difflib**: A library used for comparing the recognized speech with the target sentence to assess pronunciation accuracy.

## Installation

Follow these steps to set up the project on your local machine:

### Prerequisites

- **Python**: Ensure you have Python 3.x installed. Download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

1. Open your terminal or command prompt.
2. Clone the repository using the following command:

   ```bash
   git clone https://github.com/arjun988/Voice-Pronouce.git
   ```

### Install Required Dependencies

1. Navigate to the project directory:

   ```bash
   cd Voice-Pronouce
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   * On Windows:
     ```bash
     venv\Scripts\activate
     ```
   * On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the Application

After installing the dependencies, start the application using the following command:

```bash
python ui.py
```

## Usage

1. Open the application, and enter a target sentence in the designated input box.
2. Click the **Record** button to start listening and transcribing your speech.
3. Receive immediate feedback on your pronunciation accuracy compared to the target sentence.

## Code Structure

```
Voice-Pronouce/
│
├── main.py            # Core logic for speech recognition and pronunciation assessment
├── ui.py              # Tkinter UI implementation
├── requirements.txt   # List of required libraries
├── .gitignore         # Git ignore file
└── README.md          # This README file
```

## Troubleshooting

* If you encounter issues with speech recognition, ensure your microphone is set as the default recording device.
* Check the console for any error messages that may help diagnose problems with the application.

## Contributing

Contributions to improve the Pronunciation Assessment Application are welcome. Please feel free to submit a Pull Request.


