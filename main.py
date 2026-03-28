from gtts import gTTS
import playsound
import os
import random
import time

def cwd():
    return os.getcwd()

def speak(text, lang="en"):
    speech = gTTS(text=text, lang=lang)
    speech.save(f"{text}.mp3")
    playsound.playsound(f"{cwd()}/{text}.mp3")
    os.remove(f"{cwd()}/{text}.mp3")

def clr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

# test speak function
# speak(input("what would you like to read: "))


# set to "tasks.txt" for simpler challenges for debugging
def new_task(file_path="challenges.txt"):
    try:
        with open(file_path, "r") as chall:
            line = next(chall)
            for num, aline in enumerate(chall, 2):
                if random.randrange(num):
                    continue
                line = aline
            return line
    except FileNotFoundError:
        return "File not found."
    except StopIteration:
        return "File is empty."

def nicetime(oseconds):
    minutes = oseconds // 60
    nseconds = oseconds % 60
    return f"{minutes}:{nseconds:02}"

def main_loop_a():
    timer = 300
    challenge = new_task()
    clr()
    print(f"Time: {nicetime(timer)}")
    print(f"Challenge: {challenge}")
    print(f"Completed: no")
    speak(f"your challenge is to {challenge}")
    try:
        complete = False
        while complete == False:
            try:
                if timer >= 1:
                    timer = timer - 1
                    time.sleep(1)
                else:
                    speak("TIME IS UP! CHALLENGE FAILED!")
                    break
                clr()
                print(f"Time: {nicetime(timer)}")
                print(f"Challenge: {challenge}")
                print(f"Completed: no")
            except KeyboardInterrupt:
                complete = True
                clr()
                print("Challenge complete!")
                speak("Challenge complete")
        while complete == True:
            if timer >= 1:
                timer = timer - 1
                time.sleep(1)
            else:
                speak("Time is up! Challenge completed successfully!")
                main_loop_a()
            clr()
            print(f"Time: {nicetime(timer)}")
            print(f"Challenge: {challenge}")
            print(f"Completed: yes")
    except KeyboardInterrupt:
        speak("aaaaa you keyed too hard oh dear")

main_loop_a()

# ORIGINAL MAIN LOOP CODE
# (if edited properly this could probably be more efficient and shorter
# but im too lazy to figure out how to use this approach)

#try:
#    while True:
#        if timer >= 1:
#            timer = timer - 1
#            time.sleep(1)
#        else:
#            timer = 300
#            time.sleep(1)
#except KeyboardInterrupt:
#    print("task complete!")
