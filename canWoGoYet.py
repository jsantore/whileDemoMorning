import time
import gtts
from playsound import playsound

good_answers = ["yes", "yup", "ok", "yeah"]
did_you_do_the_right_thing = False
while not did_you_do_the_right_thing:
    right_thing  = input("Can I have Candy now?")
    right_thing = right_thing.lower()
    if right_thing in good_answers:
        did_you_do_the_right_thing = True
to_say = "Hooray! I can eat candy!"
language = 'en'
speech_object = gtts.gTTS(text=to_say, lang=language, slow=False)
speech_object.save("candy.mp3")
for repeat in range(10):
    playsound("candy.mp3")
    time.sleep(1)
