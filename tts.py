import os
import time
from gtts import gTTS
import pygame

class TTS:
    def __init__(self):
        pass

    @staticmethod
    def read(text, language="it"):
        try:
            tts = gTTS(text=text, lang=language)
            tts.save("tts_output_audio.mp3")
           # print(text + " audio created")
            if os.path.exists("tts_output_audio.mp3"):
                # Initialize pygame mixer
                pygame.mixer.init()

                # Load and play the audio file
                pygame.mixer.music.load("tts_output_audio.mp3")
                pygame.mixer.music.play()

                # Keep the program running while the audio is playing
                while pygame.mixer.music.get_busy():
                    time.sleep(1)

                pygame.mixer.quit()
                os.remove("tts_output_audio.mp3")
            #    subprocess.run(["audacious", "tts_output_audio.mp3"])
            else:
                print("Error: Audio file was not created.")

        except Exception as e:
            print(f"An error occurred: {e}")