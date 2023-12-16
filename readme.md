# Watermelon Swan MP3 Management Scripts

## Overview

The Watermelon Swan MP3 Management Scripts are a collection of tools designed to automate and enhance the efficiency of managing MP3 files. Inspired by the whimsical combination of a watermelon sculpted into a swan at a wedding buffet, these scripts aim to streamline tasks related to MP3 file organization, metadata editing, and song list management.

## Collection Contents

### 1. `rename_title.py`

#### Description

The `rename_title.py` script is designed to clean and rename MP3 files based on a specified unwanted part in the title. It utilizes the EyeD3 library to update MP3 metadata, including title and artist information.

#### Usage

```bash
python3 rename_title.py /path/to/mp3_directory -"unwanted_part"

### 2. 'metadata_editot.py'

#### Description 

The metadata_editor.py script allows you to update the metadata of MP3 files in a given directory. It reads a list of songs from a text file and assigns artist and title information based on the filenames. The script utilizes the EyeD3 library for metadata manipulation.

#### Usages

```bash
python3 metadata_editor.py /path/to/song_list.txt /source/mp3_directory /destination/mp3_directory

### 3. 'song_finder.py' 

#### Description

The song_finder.py script assists in locating and copying specific songs from a source directory to a destination directory. It reads a list of songs from a text file, searches for them in the source directory, and copies them to the destination directory. The script logs the process and any missing songs.

####  Usage

```bash
python3 song_finder.py /path/to/song_list.txt /source/mp3_directory /destination/mp3_directory

## Background

The Watermelon Swan collection was conceived as a creative solution to streamline MP3 file management, inspired by a watermelon swan sculpture at a wedding buffet. The scripts cater to music enthusiasts, DJs, or anyone looking to automate and enhance the organization of their MP3 files.

Feel free to explore, use, and contribute to the Watermelon Swan collection! Issues and pull requests are welcome.

## License

This collection is licensed under the MIT License.

