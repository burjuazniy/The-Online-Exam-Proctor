import os

BASE_DIR = os.getcwd()
STATIC_PATH = os.path.join(BASE_DIR, 'static')
OUTPUT_AUDIOS_PATH = os.path.join(STATIC_PATH, 'OutputAudios')
OUTPUT_VIDEOS_PATH = os.path.join(STATIC_PATH, 'OutputVideos')
PROFILES_PATH = os.path.join(STATIC_PATH, 'Profiles')

FFMPEG_PATH = "C:/ffmpeg/bin/ffmpeg.exe"  # Make sure that there your FFmpeg

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DB = 'examproctordb'
