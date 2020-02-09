from gtts import gTTS
import os
import sys
import random
from playsound import playsound


def run(language):
    prayer_filenames = [f for f in os.listdir('prayers')]
    iteration = 0
    while True:
        random.shuffle(prayer_filenames)
        for filename in prayer_filenames:
            with open('prayers\\' + filename) as prayer_file:
                prayer = prayer_file.read()
            print(prayer)
            key = language + str(iteration)
            gTTS(prayer, language).save("sound_files_dump\\temp" + key + ".mp3")
            playsound("sound_files_dump\\temp" + key + ".mp3")
            iteration += 1

if __name__ == "__main__":
    language = sys.argv[1] if len(sys.argv) > 1 else 'en-US'
    run(language)
