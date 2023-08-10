from main import *
import argparse


if __name__ == "__main__":
    descStr = "This program returns the length of a Youtube channel when provided a Youtube Video ID"
    parser = argparse.ArgumentParser(description=descStr)
    parser.add_argument('--video_id', dest='video_id', required=True)

    args = parser.parse_args()

    channel_length(args)

