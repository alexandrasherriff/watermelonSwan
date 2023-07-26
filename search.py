import os
import shutil


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


# Example usage
song_list_file = "/Users/alexandrasherriff/desktop/must_plays/song_list.txt"
source_folder = "/Users/alexandrasherriff/downloads"
destination_folder = "/Users/alexandrasherriff/desktop/must_plays/tracks"

song_finder = SongFinder(song_list_file, source_folder, destination_folder)
missing_songs = song_finder.find_and_copy_songs()

if missing_songs:
    print("The following songs were not found in the folder:")
    for song in missing_songs:
        print(song)
