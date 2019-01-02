# Downloadify
Download any Spotify playlist to your local storage (and google drive) </br> </br>
This python script takes two parameters, the Spotify link and an optional directory path to work on. If a path is not provided, it will work in the current directory. 

```
python Downloadify.py [https://open.spotify.com/playlist/ID] [/optional/path/to/work/on]

```

I am assuming there is a google drive storage mounted virtually to your device. The script will first download the songs on the working path and then copy the files to the google drive folder. This has been done to improve overall speed. I am also assuming that there is a cronjob command to execute this script at an appropriate time (so that we can update the local list as the spotify list is updated)

On my Android phone, I have installed FolderSync which will sync the google drive folder to the phone's local storage. It is preferable to do this at a time when the internet usage is minimal. (Around 03:00 in my case)

<b>Conclusion:</b></br>
Using this script, I was able to download my favorite songs from a Spotify playlist, and store them on my laptop's and phone's local storage, as well as on google drive to access them online.
