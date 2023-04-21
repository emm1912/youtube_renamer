# youtube_renamer  (simple coding exercise)
Rename a list of youtube videos from a list generated by yt-dlp

1.-Here you will find main.py, this is the piece of code to make this happen
2.-An example of how the .txt should be

Generally I use this type of syntax with yt-dlp (to download playlists)
yt-dlp -f 'bv*[height=1080]+ba' --download-archive videos.txt  https://www.youtube.com/playlist?list=PLlVlyGVtvuVnUjA4d6gHKCSrLAAm2n1e6 -o '%(channel_id)s/%(playlist_id)s/%(id)s.%(ext)s'

This will download the videos with part of the URL as name and, also will generate a videos.txt file where part of this info is saved also (check videos.txt added here as an example)

What the code is doing is reading every line from the videos.txt make a request to the URL, download the html as text an then parse it to find the name of the video with the help at the end of the regex in "pattern".

Then we move to the directory where the actual files are (the videos) and make a list of the files names (including extension) inside that path, we separate the names with the extension by "file_nameOld" and "file_ext", then we search the new name of the video with the help of the "file_nameOld" variable inside the dictionary and we join the "new_name" with the "file_ext", finally we write the new file name to the video.

Thats all to it.
