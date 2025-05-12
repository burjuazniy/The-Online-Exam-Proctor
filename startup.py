import os
from flask import Flask
from flask_mysqldb import MySQL

from db import db_init
from config import (
    OUTPUT_AUDIOS_PATH,
    OUTPUT_VIDEOS_PATH,
    PROFILES_PATH,
    FFMPEG_PATH
)


MUST_HAVE_STATIC_DIRS = (
    OUTPUT_AUDIOS_PATH,
    OUTPUT_VIDEOS_PATH,
    PROFILES_PATH
)

def before_startup(app: Flask, mysql: MySQL):
    """ Running the necessary checks to launch the project """

    with app.app_context():
        print("Checking the configuration before startup...")

        _check_ffmpeg()
        _check_static_folders_existance()
        db_init(mysql)

        print("Configuration is ok!")

def _check_static_folders_existance(must_have_static_dirs: str = MUST_HAVE_STATIC_DIRS):
    # Profiles, OutputVideos, OutputAudios must be in the static folder
    for dir_path in must_have_static_dirs:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

def _check_ffmpeg(ffmpeg_path: str = FFMPEG_PATH):
    if not os.path.exists(ffmpeg_path):
        print("Error. Provided path to 'ffmpeg.exe' does not exist on this system. Download FFmpeg on https://ffmpeg.org/download.html and set it in config.py FFMPEG_PATH")
        exit(1)
