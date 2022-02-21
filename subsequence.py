import re
from os import walk
from pathlib import Path

class subsequence:
    def __init__(self) -> None:
        self.getFiles()

    FILE_LIST     = []

    STRING_A      = (str)
    STRING_B      = (str)

    OUTPUT_STRING = ""

    def getFiles(self):
        # Scan the directory for text input files with the naming convention input_*.txt (where * is some number)
        currentPath = Path(__file__).parent.resolve()
        # Loop through files in directory and find input files
        for file in next(walk(currentPath), (None, None, []))[2]:
            if re.search("^input_.*.txt",file):
                self.FILE_LIST.append(file)

    def getStrings(self,f):
        # Refresh output string
        self.OUTPUT_STRING = ""

        try:
            with open(f ,'r', encoding='utf-8') as file:
                lines         = file.readlines()
                self.STRING_A = lines[0].replace("\n","")
                self.STRING_B = lines[1].replace("\n","")
        except OSError:
            print("There was an error opening the file " + f)
        

    def lcs(self,str0,str1):
        # Itterate over the two strings backwards
        # If two characters are equal add that character to the output string
        # Else
        #   determine 

        if len(str0) > 0 and len(str1) > 0:
            char0 = str0[-1]
            char1 = str1[-1]
        else:
            char0 = ""
            char1 = ""

        if char0 != '' and char1 != '':
            if char0 == char1:
                # Prepend char to output string
                self.OUTPUT_STRING = char0 + self.OUTPUT_STRING
                self.lcs(str0[:-1],str1[:-1])
            else:
                if self.helper(str0,str1[:-1]) >= self.helper(str0[:-1],str1):
                    self.lcs(str0,str1[:-1])
                else:
                    self.lcs(str0[:-1],str1)
    
    def helper(self,str0: str,str1: str) -> int:
        # Used to determine w

        if len(str0) > 0 and len(str1) > 0:
            char0 = str0[-1]
            char1 = str1[-1]
        else:
            char0 = ""
            char1 = ""

        if char0 != '' and char1 != '':
            if char0 == char1:
                # Prepend char to output string
                return 1 + self.helper(str0[:-1],str1[:-1])
            else:
                if self.helper(str0,str1[:-1]) >= self.helper(str0[:-1],str1):
                    self.helper(str0,str1[:-1])
                else:
                    self.helper(str0[:-1],str1)
        return 0

    def run(self):
        for fileName in self.FILE_LIST:
            self.getStrings(fileName)
            self.lcs(self.STRING_A,self.STRING_B)
            print(self.OUTPUT_STRING)

if __name__ == "__main__":
    program = subsequence()
    program.run()