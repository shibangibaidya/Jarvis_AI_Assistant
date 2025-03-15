# Jarvis AI Assistant

**Jarvis AI Assistant** is a voice-controlled personal assistant that performs various tasks such as opening web browsers, playing random music, fetching news updates, providing AI-powered responses, telling the current date and time, and much more. It combines speech recognition, text-to-speech, and intelligent command processing to provide a hands-free interactive experience.

## Features

1. **Voice Command Recognition**:
   - Activates when the user says the wake word "Jarvis".
   - Understands and processes spoken commands.

2. **Web Operations**:
   - Opens popular websites like Google, YouTube, Facebook, Instagram, and LinkedIn via voice commands.

3. **Music Playback**:
   - Plays random music from the local music directory.

4. **News Updates**:
   - Fetches and reads out the latest news headlines using the News API.

5. **Time and Date**:
   - Tells the current time and date upon request.

6. **AI-Powered Responses**:
   - Uses the Gemini API to provide intelligent and context-aware responses to user queries.

## Workflow

1. **Initialization**:
   - Loads the speech recognition engine, text-to-speech module, and local music library.

2. **Command Detection**:
   - Activates on hearing the wake word "Jarvis".
   - Listens for and processes voice commands.

3. **Action Execution**:
   - Executes commands such as opening websites, playing music, fetching news, or generating AI-powered responses.

## Tech Stack

**Languages and Tools**:  
- `Python`

**APIs and Libraries**:
- `speech_recognition`: For recognizing and interpreting speech input.
- `pyttsx3`: For text-to-speech conversion.
- `webbrowser`: For opening web URLs.
- `requests`: For fetching data from APIs.
- `datetime`: For handling date and time.
- `musicLibrary`: For managing and playing music.
- **Gemini API**: For generating AI-powered responses.
- **News API**: For fetching the latest news headlines.

## Usage

1. **Initialization**:
   - Run the script to start Jarvis AI Assistant.
   - Jarvis will greet you and await your commands.

2. **Wake Word**:
   - Say the word **"Jarvis"** to activate the assistant.

3. **Commands**:
   - Examples of supported commands:
     - "Open Google"  
     - "Start playing music"  
     - "What is the news?"  
     - "What time is it?"  
     - "Stop playing music"  

4. **Extending the Assistant**:
   - Additional functionalities can be integrated, such as more APIs or custom commands.

## How It Works

1. **Speech Recognition**:
   - Listens to user input through the microphone.
   - Recognizes spoken words using the Google Speech API.

2. **Command Processing**:
   - Analyzes the command to determine the appropriate action.
   - Handles specific tasks like playing random music or fetching the news.

3. **AI-Powered Interaction**:
   - Uses the Gemini API to provide intelligent and conversational responses.

4. **Text-to-Speech**:
   - Provides audible feedback by converting text responses into speech.

## Authors

- [@shibangibaidya](https://www.github.com/shibangibaidya)

## Deployment

To clone and run this project, use the following commands:

```bash
git clone https://github.com/shibangibaidya/Jarvis_AI_Assistant.git
cd Jarvis_AI_Assistant
python jarvis.py
