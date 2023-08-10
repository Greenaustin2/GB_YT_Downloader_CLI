# GRAPHIC BALANCE CLI

## About

The Graphic Balance CLI is a simple program used for discovering, cataloguing, and archiving randomly generated found footage. While a niche use-case, the program could easily be adapted or built upon to support a variety of needs. This was written specifically for use with experimental found-footage documentary. The main functionality is based upon in-camera file naming protocol (IMG 2383, GOPR3483, DSCF9247, 9247MP4 etc.), which when queried to the Youtube Database yields some interesting and unique results. The program has been slightly adapted for use by others, however it has not yet been built into a well-structured CLI program.

![screen shot one](./gbd.png?raw=true)

## Tech Stack

![python logo](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![python logo](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white) 


## Running Locally

Clone the project
```
git clone https://github.com/Greenaustin2/GB_YT_Downloader_CLI.git
```
Go to project directory
```
cd GB_YT_Downloader_CLI
```
Remove remote origin
```
git remote remove origin
```
Install packages
```
pip install -r requirements.txt
```

Add your Youtube Data API Key to the .env file.

[How to get your API Key](https://blog.hubspot.com/website/how-to-get-youtube-api-key)
```
// .env

API_KEY="000000000000000000000000000000000000000"
```

## Commands

### Download

Takes a randomly generated search query (IMG 2383, GOPR3483, DSCF9247, 9247MP4), retrieves a list of results via the Youtube Data Api, selects one of the results at random and downloads the selected result via the Pytube downloader.

#### Arguments:

(**only --output_path is required**, other default values are in bold and can be overwritten )

**--output_path**: path/to/output/storage/directory

**--formats**: formats as list of strings. **["mp4", "wmv", "avi", "mov", "img"]**

**--video_def**: **any**, high, standard

**--max_results**: amount results returned, any int. default **50**

**--title_chars**: filters length of title of results, default **18**

**--video_duration**: **any**, long (> 20 min), medium (> 4, < 20 min), short (< 4 min)

**--embed**: is video embeddable. **any**, true

**--video_limit**: number of videos to be downloaded at random, int. default **100**

**--file_size**: maximum file size, int value in bytes. default **1e8**

**--random**: 'yes' will download one video per query, while 'no' will download videos from a single query. default 'yes'

**--published_before**: RFC 3339 time format (1970-01-01T00:00:00Z)

**--published_after**: RFC 3339 time format (1970-01-01T00:00:00Z)

**--order**: **relevance**, date, rating, title, viewCount

**--type**: **video**, channel, playlist

```
python download.py --output_path "/path/to/output/directory" --<other arguments>
```

### Channel Download

Takes a directory of downloaded videos, and loops through all files in that directory, downloading the entirety of each video's respective channel

#### Arguments:

**--origin_directory**: the directory with the source files (required)

**--destination_directory**: the directory in which to store the downloaded channels (required)
```
python channel_download.py --origin_directory "/path/to/origin" --destination_directory "/path/to/destination/
```

### Channel Browser

Takes a directory of downloaded videos, and loops through all files in that directory, populating each video's respective channel into a web browser

#### Arguments:

**--origin_directory**: the directory with the source files (required)

```
python channel_browser.py --origin_directory "/path/to/origin"
```

### Channel Length

Returns the length of a specified channels uploaded video catalogue

#### Arguments
**--video_id**: 11 character Youtube video id number of a video from the channel you wish to inspect (required)

(youtube.com/watch?v=**KzQp8wEx-DE**)

```
python channel_length.py --video_id KzQp8wEx-DE
```

### Playlist Download

Download a Youtube playlist when given a Youtube playlist URL

#### Arguments
**--playlist_url**: URL to Youtube playlist (required)

(https://youtube.com/playlist?list=PLvh1qErgmgw3dGtXi7ls5DAZf6YR2Th6A)

```
python playlist_download.py --playlist_url https://youtube.com/playlist?list=PLvh1qErgmgw3dGtXi7ls5DAZf6YR2Th6A
```







