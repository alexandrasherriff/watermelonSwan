import os
import shutil
import logging

# Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
log_file = "song_finder.log"  # Specify the log file path
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.StreamHandler(),
    logging.FileHandler(log_file)
])
logger = logging.getLogger(__name__)


class SongFinder:
    def __init__(self, song_list_file, source_folder, destination_folder):
        self.song_list_file = song_list_file
        self.source_folder = source_folder
        self.destination_folder = destination_folder

    def find_and_copy_songs(self):
        missing_songs = []
        try:
            with open(self.song_list_file, 'r') as file:
                for line in file:
                    song_name = line.strip()
                    song_found = False
                    for root, dirs, files in os.walk(self.source_folder):
                        for file_name in files:
                            if song_name.lower() in file_name.lower():
                                source_path = os.path.join(root, file_name)
                                destination_path = os.path.join(self.destination_folder, file_name)
                                shutil.copy2(source_path, destination_path)
                                song_found = True
                                logger.info(f"Copied {file_name} to {destination_path}")
                                break
                        if song_found:
                            break
                    if not song_found:
                        missing_songs.append(song_name)
                        logger.warning(f"Song not found: {song_name}")
        except FileNotFoundError:
            logger.error(f"Song list file not found: {self.song_list_file}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")

        return missing_songs

if __name__ == "__main__":
    # Set your file paths here
    song_list_file = ""
    source_folder = ""
    destination_folder = ""
    

    song_finder = SongFinder(song_list_file, source_folder, destination_folder)
    missing_songs = song_finder.find_and_copy_songs()

    if missing_songs:
        print("The following songs were not found in the folder:")
        for song in missing_songs:
            print(song)
