from main import *
import argparse


if __name__ == "__main__":
    descStr = "Loops through folder of videos and downloads entirety of each videos respective channel"

    parser = argparse.ArgumentParser(description=descStr)
    parser.add_argument('--origin_directory', dest='origin_directory', required=True)
    parser.add_argument('--destination_directory', dest='destination_directory', required=True)

    args = parser.parse_args()

    channel_download(args)

