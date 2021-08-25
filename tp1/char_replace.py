"""Search and replace weird accented characters.

Passing the name of a text file to modify, replace weird accented characters in it.
Overwrites text file.
"""
import sys

def main_replace(filename):
    """Search and replaces weird accented characters from input text file."""
    replacement = {
        "á": "á",
        "é": "é",
        "ı́": "í",
        "ó": "ó",
        "ú": "ú"
    }
    with open(filename, "r") as file :
        filedata = file.read()
    for text_to_replace, text_replacing in replacement.items():
        filedata = filedata.replace(text_to_replace, text_replacing)
    with open(filename, "w") as file:
        file.write(filedata)

if __name__ == "__main__":
    main_replace(str(sys.argv[1]))