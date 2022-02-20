import re
from os import walk
from pathlib import Path

class subsequence:
    def __init__(self) -> None:
        self.getFiles()

    FILE_LIST = []

    STRING_A  = (str)
    STRING_B  = (str)

    def getFiles(self):
        # Scan the directory for text input files with the naming convention input_*.txt (where * is some number)
        currentPath = Path(__file__).parent.resolve()
        # Loop through files in directory and find input files
        for file in next(walk(currentPath), (None, None, []))[2]:
            if re.search("^input_.*.txt",file):
                self.FILE_LIST.append(file)

    def getStrings(self,f):
        try:
            with open(f ,'r', encoding='utf-8') as file:
                lines         = file.readlines()
                self.STRING_A = lines[0].replace("\n","")
                self.STRING_B = lines[1].replace("\n","")
                print(f + " produced strings " + self.STRING_A + " AND " + self.STRING_B)
        except OSError:
            print("There was an error opening the file " + f)
        

    def lcs(self):
        pass

    def run(self):
        for fileName in self.FILE_LIST:
            self.getStrings(fileName)

if __name__ == "__main__":
    program = subsequence()
    program.run()