# Minecraft Random Challenges
## About
The Minecraft Random Chllenges (MRC) is a challenge mod(ish) that gives the user a task every 5 minutes and the user must complete it to move on. To mark a task as complete, use the `ctrl + C` keybind. If you want to stop the challenge, mark it as complete then use `ctrl + C` for a second time.
## Requirements
MRC requires the python libraries
- gTTS (Google text to speech)
- playsound (to play gTTS audio files)<br>
All other libraries are preinstalled with python
## Files
- challenges.txt | The primary challenges, used in the video. This file is a set of 100 challenges that all should be relatively completable in 5 minutes. This code contains some challenges that are intended to be used with a friend, so if you plan to not use them remove lines 59 to 64. If you would like to do these challenges but you arent friends with binugs man, change every reference of `bingus_man` or `bingus man` to your friends name
- tasks.txt      | Similar to challenges.txt, but contains challenges completable in 2 minutes, and all singleplayer. This was just meant for debugging but if you want to try it you can.
- main.py        | The primary code for the challenge. This randomly selects challenges from either `challenges.txt` or `tasks.txt`. If you keep the file set to `challenges.txt` as is used in the video, set `timer` in line 47 to `300`. This value is default so if you don't plan to change anything, don't worry about it. If you choose to use `tasks.txt` instead, set `file_path` on line 27 to `"tasks.txt"` and set time in line 47 to `120`
