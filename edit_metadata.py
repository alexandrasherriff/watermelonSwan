import os
import eyed3
import argparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_title_name(file):
    """Extract the title name without the '.mp3' extension."""
    return file.replace('.mp3', '')

def split_title(title_name):
    """Split the title at the '-' character and return artist and title."""
    if '-' in title_name:
        return map(str.strip, title_name.split('-', 1))
    else:
        return '', title_name.strip()

def load_metadata(file_path):
    """Load existing metadata or return None if no metadata found."""
    try:
        audiofile = eyed3.load(file_path)
        return audiofile.tag if audiofile and audiofile.tag else None
    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")
        return None

def update_metadata(file_path, title, artist):
    """Update MP3 metadata and log a message if metadata is updated."""
    audiofile = eyed3.load(file_path)
    if audiofile.tag:
        original_title, original_artist = audiofile.tag.title, audiofile.tag.artist
        audiofile.tag.title, audiofile.tag.artist = title, artist
        audiofile.tag.save()

        if (original_title, original_artist) != (title, artist):
            logger.info(f"Updated metadata for {file_path}")
    else:
        logger.warning(f"No metadata found in {file_path}")

def process_file(directory, file):
    """Process an individual MP3 file."""
    file_path = os.path.join(directory, file)
    title_name = get_title_name(file)
    artist, title = split_title(title_name)
    metadata = load_metadata(file_path)

    if metadata:
        update_metadata(file_path, title, artist)

def assign_artist_and_title(directory):
    """Assign artist and title for all MP3 files in the specified directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp3'):
                process_file(root, file)

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Assign artist and title to MP3 files.')
    parser.add_argument('directory', help='The directory containing the MP3 files')
    return parser.parse_args()

if __name__ == "__main__":
    # Parse command-line arguments
    args = parse_arguments()

    # Configure logger to write to a file
    log_file = os.path.join(args.directory, 'metadata_editor.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info(f"Started processing MP3 files in directory: {args.directory}")

    # Process MP3 files
    assign_artist_and_title(args.directory)

    logger.info("Finished processing MP3 files.")
