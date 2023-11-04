import os
import shutil

# Create txt file for list of songs and copy the path
song_list_file = ""
# Enter path of folder you wish to search
source_folder = ""
#  Enter path of folder to where you would like to copy the songs
destination_folder = ""


class SongFinder:
    def __init__(self, song_list_file, source_folder, destination_folder):
        self.song_list_file = song_list_file
        self.source_folder = source_folder
        self.destination_folder = destination_folder

    def find_and_copy_songs(self):
        missing_songs = []
        with open(self.song_list_file, 'r') as file:
            for line in file:
                song_name = line.strip()
                song_found = False
                for root, dirs, files in os.walk(self.source_folder):
                    for file in files:
                        if song_name.lower() in file.lower():
                            source_path = os.path.join(root, file)
                            destination_path = os.path.join(self.destination_folder, file)
                            shutil.copy(source_path, destination_path)
                            song_found = True
                            break
                    if song_found:
                        break
                if not song_found:
                    missing_songs.append(song_name)
        return missing_songs


song_finder = SongFinder(song_list_file, source_folder, destination_folder)
missing_songs = song_finder.find_and_copy_songs()

if missing_songs:
    print("The following songs were not found in the folder:")
    for song in missing_songs:
        print(song)
