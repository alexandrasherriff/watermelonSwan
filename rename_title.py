import os

class FileRenamer:
    def __init__(self, directory, unwanted_part):
        self.directory = directory
        self.unwanted_part = unwanted_part

    def clean_and_rename_files(self):
        files = os.listdir(self.directory)

        for file in files:
            if file.endswith('.mp3') and self.unwanted_part in file:
                file_path = os.path.join(self.directory, file)
                clean_title = file.split(self.unwanted_part)[0].strip()
                new_filename = clean_title + '.mp3'
                new_file_path = os.path.join(self.directory, new_filename)

                os.rename(file_path, new_file_path)

if __name__ == "__main__":
    directory = '/Users/alexandrasherriff/desktop/must_plays/tracks'
    unwanted_part = ' myfreemp3.vip'

    renamer = FileRenamer(directory, unwanted_part)
    renamer.clean_and_rename_files()
