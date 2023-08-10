from main import *
import argparse


if __name__ == "__main__":
    descStr = "loops through directory of videos and pulls up each video's respective channel in a web browser"
    parser = argparse.ArgumentParser(description=descStr)
    parser.add_argument('--origin_directory', dest='origin_directory', required=True)

    args = parser.parse_args()

    channel_browser(args)


