from main import *
import argparse


if __name__ == "__main__":
    descStr = "This program download youtube videos at random"
    parser = argparse.ArgumentParser(description=descStr)
    parser.add_argument('--output_path', dest='output_path', required=True)
    parser.add_argument('--formats', dest='formats', required=False, default=["mp4", "wmv", "avi", "mov", "img"])
    parser.add_argument('--video_def', dest='video_def', required=False, default="any")
    parser.add_argument('--format', dest='format', required=False)
    parser.add_argument('--max_results', dest='max_results', required=False, default=50)
    parser.add_argument('--title_chars', dest='title_chars', required=False, default=18)
    parser.add_argument('--video_duration', dest='video_duration', required=False, default="any")
    parser.add_argument('--embed', dest='embed', required=False, default="any")
    parser.add_argument('--video_limit', dest='video_limit', required=False, default=100)
    parser.add_argument('--file_size', dest='file_size', required=False, default=2e8)
    parser.add_argument('--random', dest='random', required=False, default="yes")
    parser.add_argument('--published_before', dest='published_before', required=False, default=current_time())
    parser.add_argument('--published_after', dest='published_after', required=False, default='2015-04-23T00:00:00Z')
    parser.add_argument('--number', dest='number', required=False)
    parser.add_argument('--search_query', dest='search_query', required=False)
    parser.add_argument('--order', dest='order', required=False, default="relevance")
    parser.add_argument('--type', dest='type', required=False, default="video")

    args = parser.parse_args()

    download(args)

