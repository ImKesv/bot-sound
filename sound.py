import pyttsx3
import os
os.system('cls')

speaker = pyttsx3.init()

"""u can change it
must be inside speaker.say() function"""

speaker.say("""BOOM HEADSHOT!!!!!!!!!""")
speaker.runAndWait()
