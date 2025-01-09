import speech_recognition as sr  # For speech-to-text
import pyttsx3  # For text-to-speech
import wikipedia  # To fetch Wikipedia summaries
import pywhatkit  # To play YouTube videos or perform other tasks
import datetime  # To get the current time or date

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (range: 0.0 to 1.0)

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture audio from the microphone and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)  # Listen to the microphone
            command = recognizer.recognize_google(audio)  # Convert to text
            print(f"You said: {command}")
            return command.lower()  # Convert text to lowercase
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Network error. Please check your connection.")
            return ""

def handle_command(command):
    """Process and execute the given command."""
    if "time" in command:
        # Get the current time
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")
    elif "date" in command:
        # Get today's date
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {date}")
    elif "search" in command:
        # Search Wikipedia
        topic = command.replace("search", "").strip()
        speak(f"Searching Wikipedia for {topic}")
        try:
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)
        except wikipedia.exceptions.DisambiguationError:
            speak("Multiple results found. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("No results found.")
    elif "play" in command:
        # Play music on YouTube
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
    elif "stop" in command:
        # Stop the assistant
        speak("Goodbye!")
        return False
    else:
        speak("I didn't understand that. Please try again.")
    return True

def main():
    """Main function to run the assistant."""
    speak("Hello! How can I assist you today?")
    running = True
    while running:
        command = listen()  # Listen to the user's command
        if command:
            running = handle_command(command)  # Process the command

if __name__ == "__main__":
    main()

