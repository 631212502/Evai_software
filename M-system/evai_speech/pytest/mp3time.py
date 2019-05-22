from mutagen.mp3 import MP3

audio = MP3("/home/evai/下载/M-system/evai_speech/resources/wozai.mp3")
print(audio.info.length)