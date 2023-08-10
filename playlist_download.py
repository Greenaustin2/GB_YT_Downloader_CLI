from main import *
import argparse


if __name__ == "__main__":
    descStr = "This program downloads a Youtube playlist when given a playlist URL"
    parser = argparse.ArgumentParser(description=descStr)
    parser.add_argument('--playlist_url', dest='playlist_url', required=True)

    args = parser.parse_args()

    playlist_download(args)

