import sys
import holyroller
import subprocess
import random

language_codes = ['en-US', 'en-GB', 'fr', 'de', 'pl', 'nl', 'fi', 'sv', 'it', 'es', 'pt', 'ru' 'zh-CN', 'ja', 'ko']
#language_codes = ['en-US', 'en-GB', 'fr', 'de', 'pl', 'nl', 'fi', 'sv', 'it', 'es', 'pt', 'ru']


def make_rollers(num_rollers):
    for i in range(min(int(num_rollers), len(language_codes))):
        if i == 0:
            language = 'en-US'
        else:
            language = random.choice(language_codes)
        language_codes.remove(language)
        subprocess.Popen(['python', 'holyroller.py', language])

if __name__ == "__main__":
    make_rollers(sys.argv[1] if len(sys.argv) > 1 else 1)
