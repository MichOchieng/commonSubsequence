import re
from os import walk
from pathlib import Path

class subsequence:
    def __init__(self) -> None:
        self.getFiles()

    FILE_LIST = []

    def getFiles(self):
        # Scan the directory for text input files with the naming convention input_*.txt (where * is some number)
        currentPath = Path(__file__).parent.resolve()
        # Loop through files in directory and find input files
        for file in next(walk(currentPath), (None, None, []))[2]:
            if re.search("^input_.*.txt",file):
                self.FILE_LIST.append(file)
                print(file)
        

    def run(self):
        pass

if __name__ == "__main__":
    program = subsequence()
    program.run()