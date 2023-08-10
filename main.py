from googleapiclient.discovery import build
import os
import random
from pytube import YouTube
from pytube import Channel
from pytube import Playlist
import argparse
import webbrowser
import datetime
from dotenv import load_dotenv
import shutil


load_dotenv()
YOUTUBE = build('youtube', 'v3', developerKey=os.environ["API_KEY"])


def current_time():
    utc_now = datetime.datetime.utcnow()
    return utc_now.strftime('%Y-%m-%dT%H:%M:%SZ')


def query(args):
    """Outputs 4-digit number formatted with randomly chosen file type from file type list. takes number as input"""
    args.number = str(random.randint(1, 10 ** 4)).zfill(4)
    args.format = random.choice(args.formats)
    if args.format == "gopr":
        return f"{args.format}{args.number}"
    elif args.format == "mov" or args.format == "img":
        return f"{args.format} {args.number}"
    else:
        return f"{args.number}.{args.format}"


def api_request(args):
    """Conducts search as per search criteria. A list of video ID's are compiled in a list, chosen at random"""
    # API search criteria
    while True:
        videos = []
        query_value = query(args)
        request = YOUTUBE.search().list(
            part='snippet',
            q=query_value,
            order=args.order,
            type=args.type,
            maxResults=args.max_results,
            videoDefinition=args.video_def,
            videoEmbeddable=args.embed,
            videoDuration=args.video_duration,
            publishedBefore=args.published_before,
            publishedAfter=args.published_after,
        )
        response = request.execute()
        files = response["items"]
        for v_id in files:
            # title of video as a string
            title = str(v_id["snippet"]["title"]).lower()
            # check if search query is in video title before appending to video ID list
            if str(args.number) in title and args.format in title:
                if len(title) <= args.title_chars:
                    videos.append(v_id["id"]["videoId"])
                else:
                    pass
        if len(videos) > 1:
            return videos, query_value
        else:
            continue


def download(args):
    """Downloads videos from Youtube at random via a randomly generated search query"""
    x = 1
    y = 0
    print(args.formats)
    if args.random == 'yes':
        for _ in range(0, args.video_limit):
            print('_')
            videos, query_value = api_request(args)
            print('__')
            video_id = random.choice(videos)
            print('___')
            yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
            print('____')
            vid_info = f"{video_id}_{yt.author}_{yt.channel_id}_{yt.publish_date.date()}_{yt.views}_"
            print('_____')
            yt = yt.streams.get_highest_resolution()
            print('______')
            if yt.filesize < args.file_size:
                print(f"({x}) downloading {query_value}")
                x += 1
                yt.download(output_path=args.output_path, filename_prefix=vid_info)
            else:
                print("file too large")
                continue
    elif args.random == 'no':
        video_id = api_request(args)
        print(f"downloading {video_id}...")
        for _ in range(0, args.video_limit):
            yt = YouTube(f"https://www.youtube.com/watch?v={video_id[_]}")
            vid_info = f"{video_id[_]}_{yt.publish_date.date()}_{yt.views}_"
            yt = yt.streams.get_highest_resolution()
            if yt.filesize < args.file_size:
                yt.download(output_path=args.output_path, filename_prefix=vid_info)
            else:
                pass


def channel_browser(args):
    """loops through directory of videos and pulls up each video's respective channel in a web browser"""
    directory = os.listdir(args.origin_directory)
    print(len(directory))
    if len(directory) > 10:
        counter = 1
        for file in directory:
            if file.endswith('.mp4'):
                video_id = file[:11]
                link = "https://www.youtube.com/watch?v=" + video_id
                x = YouTube(link)
                curl = x.channel_url
                c = Channel(curl)
                print(f"({counter}) {curl}")
                # {len(c.video_urls)}
                counter += 1
    else:
        for file in directory:
            if file.endswith('.mp4'):
                video_id = file[:11]
                link = "https://www.youtube.com/watch?v=" + video_id
                x = YouTube(link)
                curl = x.channel_url
                webbrowser.open_new_tab(curl)


def channel_download(args):
    """Loops through folder of videos and downloads entirety of each videos respective channel"""
    video_id_list = []
    directory = os.listdir(args.origin_directory)
    for file in directory:
        if file.endswith(".mp4"):
            video_id = file[:11]
            print(f"video id: {video_id}")
            x = YouTube("https://www.youtube.com/watch?v=" + video_id)
            print(f"X: {x}")
            curl = x.channel_url
            print(f"Curl: {curl}")
            c = Channel(curl)
            path = os.path.join(args.destination_directory, c.channel_name)
            print(f"path: {path}")
            try:
                os.mkdir(path)
            except FileExistsError:
                print("error")
                pass
            finally:
                x = 1
                print(f"before for loop")
                print(c.video_urls)
                for url in c.video_urls:

                    yt = YouTube(url)
                    vid_info = f"{yt.video_id}_{yt.publish_date.date()}_{yt.views}_"
                    print(f"vid info: {vid_info}")
                    print(f"downloading ({x}/{len(c.video_urls)}) {vid_info}")
                    try:
                        yt.streams.get_highest_resolution().download(output_path=path, filename_prefix=vid_info)
                    except KeyError as error:
                        print(error)
                        pass
                    x += 1
                print("after for loop")
                shutil.move(args.origin_directory + file, path)


def channel_length(args):
    """Responds with number of videos on channel given a Youtube Video ID"""

    x = YouTube("https://www.youtube.com/watch?v=" + args.video_id)
    curl = x.channel_url
    print("channel url" + curl)
    c = Channel(curl)
    print(c)
    print(f"this channel has {len(c.video_urls)} videos.")


def playlist_download(args):
    """Downloads Youtube playlist from playlist url"""
    p = Playlist(args.url)
    x = 0
    for videos in p.videos:
        url = p.video_urls[x]
        vid_id = url[-11:]
        yt = YouTube(url)
        x += 1
        vid_info = f"{vid_id}_{yt.author}_{yt.channel_id}_{yt.publish_date.date()}_{yt.views}_"
        print(f"downloading {vid_info}...")
        videos.streams.get_highest_resolution().download(output_path=self.destination_directory, filename_prefix=vid_info)