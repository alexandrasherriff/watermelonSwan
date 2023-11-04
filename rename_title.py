import os
import eyed3

# Enter the path and the unwanted part of the title

directory = ''
unwanted_part = ''


class FileRenamer:
    def __init__(self, directory, unwanted_part):
        self.directory = directory
        self.unwanted_part = unwanted_part

    def clean_and_rename_files(self):
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.endswith('.mp3') and self.unwanted_part in file:
                    file_path = os.path.join(root, file)
                    clean_title = file.split(self.unwanted_part)[0].strip()

                    # Split the clean_title at the '-' character
                    if '-' in clean_title:
                        artist, title = map(str.strip, clean_title.split('-', 1))
                    else:
                        # Handle the case where there is no hyphen
                        artist = ''
                        title = clean_title.strip()

                    # artist, title = map(str.strip, clean_title.split('-'))

                    new_filename = f"{artist} - {title}.mp3"
                    new_file_path = os.path.join(root, new_filename)

                    # Check if the new file path already exists before renaming
                    if not os.path.exists(new_file_path):
                        os.rename(file_path, new_file_path)

                    # Update MP3 metadata (title and artist)
                    audiofile = eyed3.load(new_file_path)
                    if audiofile.tag:
                        audiofile.tag.title = title
                        audiofile.tag.artist = artist
                        audiofile.tag.save()


if __name__ == "__main__":
    renamer = FileRenamer(directory, unwanted_part)
    renamer.clean_and_rename_files()
