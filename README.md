# DownPlaylistFull

Don't know English? [CLICK HERE](https://github.com/DaviJoseMach/DownPlaylistFull/blob/main/ReadmePt-BR.md)

DownPlaylistFull was created to address the need for downloading all videos from a YouTube playlist quickly, efficiently, and in the highest possible quality. Currently, there are few reliable websites or projects dedicated to this, which is why DownPlaylistFull was developed.

## Technologies Used

| Name    | Version |
|---------|---------|
| Python  | 3.12.8 (or any version above) |
| ffmpeg  | (latest version) |
| yt-dlp  | (latest version) |
| browser-cookie3  | (latest version) |


## Installation

Before running the script, you need to install **Python**, **yt-dlp**, and **FFmpeg**.

### Installing yt-dlp

For **Windows**:

```sh
pip install yt-dlp

```

For **Linux**:

```sh
pip install yt-dlp

```
For **Windows**:

```sh
pip install browser-cookie3

```

For **Linux**:

```sh
pip install browser-cookie3

```
### Installing FFmpeg

For **Windows** (using Winget):

```sh
winget install -e --id Gyan.FFmpeg

```

For **Linux**:

```sh
sudo apt update && sudo apt install ffmpeg

```

## Usage

First, you have to be logged in to YouTube in your browser. (Firefox or Chrome based ones) so the script can access the cookies.

Once you have installed all dependencies, download or copy the script from [HERE](https://github.com/DaviJoseMach/DownPlaylistFull/blob/main/down_playlist.py).

Run the script using the following command:

```sh
python your_script_name.py

```

Follow the on-screen instructions to input the YouTube playlist link and the folder where the videos will be saved.

### Features

-   Downloads all videos (or just the audio) from a YouTube playlist.
-   Ensures the highest available quality (up to 1080p with audio).
-   Uses **FFmpeg** to merge video and audio files seamlessly.
-   Works on both Windows and Linux.

Enjoy hassle-free YouTube playlist downloads with **DownPlaylistFull**! 🚀
