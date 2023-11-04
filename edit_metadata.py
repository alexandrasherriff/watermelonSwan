import os
import eyed3

# Enter path of the folder
directory = ""


class MetadataEditor:
    def __init__(self, directory):
        self.directory = directory

    def assign_artist_and_title(self):
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.endswith('.mp3'):
                    file_path = os.path.join(root, file)
                    title_name = file.replace('.mp3', '')

                    # Split the clean_title at the '-' character
                    if '-' in title_name:
                        artist, title = map(str.strip, title_name.split('-', 1))
                    else:
                        artist = ''  # Set artist to an empty string or another default value
                        title = title_name.strip()  # Use the entire string as the title

                    # Update MP3 metadata (title and artist)
                    try:
                        audiofile = eyed3.load(file_path)
                        if audiofile.tag:
                            audiofile.tag.title = title
                            audiofile.tag.artist = artist
                            audiofile.tag.save()
                            print(f"Updated metadata for {file}")
                        else:
                            print(f"No metadata found in {file}")
                    except Exception as e:
                        print(f"Error processing {file}: {e}")


if __name__ == "__main__":
    metadata = MetadataEditor(directory)
    metadata.assign_artist_and_title()
