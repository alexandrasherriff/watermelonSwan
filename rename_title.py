import os
import eyed3
import argparse
import logging

# Configure logging to capture informational messages
logging.basicConfig(level=logging.INFO)

# Parse command-line arguments for directory and unwanted part
parser = argparse.ArgumentParser(description='Clean and rename MP3 files.')
parser.add_argument('directory', help='The directory containing the MP3 files')
parser.add_argument('unwanted_part', help='The unwanted part of the title')
args = parser.parse_args()

class FileRenamer:
    def __init__(self, directory, unwanted_part):
        """
        Initialize the FileRenamer instance.

        Parameters:
        - directory (str): The directory containing the MP3 files.
        - unwanted_part (str): The unwanted part of the title.
        """
        self.directory = directory
        self.unwanted_part = unwanted_part
        self.logger = logging.getLogger(__name__)

    def clean_and_rename_files(self):
        """
        Clean and rename MP3 files in the specified directory.

        This method iterates through the files in the specified directory,
        performs cleaning and renaming, and updates MP3 metadata.
        """
        self.logger.info('Cleaning and renaming files...')
        for root, _, files in os.walk(self.directory):
            for file in files:
                if self.is_valid_mp3_file(file):
                    file_path = os.path.join(root, file)
                    clean_title = self.clean_title(file)

                    artist, title = self.extract_artist_and_title(clean_title)

                    new_filename = f"{artist} - {title}.mp3"
                    new_file_path = os.path.join(root, new_filename)

                    if not os.path.exists(new_file_path):
                        os.rename(file_path, new_file_path)
                        self.logger.info(f'Renamed file: {file} -> {new_filename}')
                    else:
                        self.logger.warning(f'Skipped renaming file {file}. New file already exists.')
                    
                    self.update_mp3_metadata(new_file_path, title, artist)

            self.logger.info('Finished cleaning and renaming files.')

    def is_valid_mp3_file(self, file):
        """
        Check if a file is a valid MP3 file.

        Parameters:
        - file (str): The file name.

        Returns:
        - bool: True if the file is a valid MP3 file, False otherwise.
        """
        _, extension = os.path.splitext(file)
        return extension.lower() == '.mp3' and self.unwanted_part in file
    
    def clean_title(self, file):
        """
        Clean the title of an MP3 file.

        Parameters:
        - file (str): The file name.

        Returns:
        - str: The cleaned title.
        """
        return file.split(self.unwanted_part)[0].strip()
    
    def extract_artist_and_title(self, clean_title):
        """
        Extract artist and title from a cleaned title.

        Parameters:
        - clean_title (str): The cleaned title.

        Returns:
        - tuple: A tuple containing artist and title.
        """
        if '-' in clean_title:
            artist, title = map(str.strip, clean_title.split('-', 1))
        else:
            artist = ''
            title = clean_title.strip()
        return artist, title
    
    def update_mp3_metadata(self, file_path, title, artist):
        """
        Update MP3 metadata for a file.

        Parameters:
        - file_path (str): The path to the MP3 file.
        - title (str): The title to set in the metadata.
        - artist (str): The artist to set in the metadata.
        """
        audiofile = eyed3.load(file_path)
        if audiofile.tag:
            audiofile.tag.title = title
            audiofile.tag.artist = artist
            audiofile.tag.save()
            self.logger.info(f'Updated metadata for {file_path}: Title={title}, Artist={artist}')

if __name__ == "__main__":
    # Print the provided directory and unwanted part for verification
    print("Directory:", args.directory)
    print("Unwanted Part:", args.unwanted_part)

    # Create a FileRenamer instance and perform file cleaning and renaming
    renamer = FileRenamer(args.directory, args.unwanted_part)
    renamer.clean_and_rename_files()
