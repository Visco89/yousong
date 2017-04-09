from __future__ import unicode_literals
import youtube_dl
import re



def youtube_validation(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    return re.match(youtube_regex, url)


urllist = []
url = input("Paste the youtube link to download: ")
while not url == "stop":
    print("To stop type \"stop\"")
    if youtube_validation(url):
        urllist.append(url)
        url = input("Paste the youtube link to download: ")
    else:
        url = input("Youtube link is not valid, please retry: ")



ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urllist)