from pytube import Playlist
import youtube_dl
import pytube

### Convert Youtube Playlist -> Youtube List URL(File Type: MP3) -> Download All ###

def parseLink(link):
    pl = Playlist(link)
    return pl.parse_links()

def downloadAudio(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

if __name__ == "__main__":
    url = raw_input("Link URL(playlist)> ")
    for sublink in parseLink(url):
        downloadAudio("https://www.youtube.com" + sublink)
        # print sublink