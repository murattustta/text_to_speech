import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
def speak_with_settings(text, voice_index, rate, volume):
    if voice_index < len(voices):
        engine.setProperty('voice', voices[voice_index].id)
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        engine.say(text)
        engine.runAndWait()
    else:
        print("Invalid voice index")

characters = [
    {"name": "Emily", "voice_index": 1, "rate": 150, "volume": 0.9},
    {"name": "Matt", "voice_index": 2, "rate": 120, "volume": 0.8},
    {"name": "Diane", "voice_index": 3, "rate": 180, "volume": 0.7},
    {"name": "Helen", "voice_index": 0, "rate": 100, "volume": 1.0},
    {"name": "Eva", "voice_index": 4, "rate": 200, "volume": 0.6},
    {"name": "Emma", "voice_index": 1, "rate": 140, "volume": 0.5},
    {"name": "Daniel", "voice_index": 2, "rate": 160, "volume": 0.4},
    {"name": "Marlene", "voice_index": 3, "rate": 130, "volume": 0.3},
    {"name": "Meryl", "voice_index": 0, "rate": 170, "volume": 0.2},
    {"name": "Lea", "voice_index": 4, "rate": 110, "volume": 0.1},
]

def show_characters():
    print("Available characters:")
    for i, char in enumerate(characters, 1):
        print(f"{i}. {char['name']}")

while True:
    answer = input("Enter what you want the robot to say (type 'exit', 'bye', or 'quit' to quit): \n")

    if answer.lower() in ['exit', 'bye', 'quit']:
        print("Exiting the program.")
        break

    show_characters()

    char_index = input("Enter character number (1-10): ")
    try:
        char_index = int(char_index) - 1
        if 0 <= char_index < 10:
            char_settings = characters[char_index]
            speak_with_settings(answer, char_settings["voice_index"], char_settings["rate"], char_settings["volume"])
        else:
            print("Invalid character number. Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")
