# Downloadify
Downloadify is a python and bash script which downloads any Spotify album onto your local storage

### Installation

Dowloadify requires youtube-dl (a command line program) and Beautiful soup

To run the script, run the command below in bash

```sh
$ python Downloadify.py [spotify_playlist_url] [optional_download_location] [optional_extra_download_path]
```
The reason why I included the options of two paths is because, I wanted to store the Sotify playlist on my local device as well as on the cloud (a virtual Google Drive folder is mounted to my device). If a optional_download_location is provided, then it will download the songs to the specified directory. If its not provided then it will download the songs to the current directory. If optional_extra_download_path is provided, it will ONLY copy the downloaded songs to the specified path, else it will do nothing.

### How does it work?

--> Check if the song exists in the local music folder (or the optional_download_location)
--> If the songs EXISTS, do not download the song
--> If the song DOESN'T EXIST, then get the first link from Youtube for that song and download the .mp3 of it
--> If a optional_extra_download_path is provided, then copy the song to the path

### Todos

 - Make it 'installable' from the terminal
 - Add a progress bar

License
----
MIT
