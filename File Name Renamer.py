import os
import shutil
import threading

def fill(msg, length, symbol):
    return msg + ((length - len(msg))* symbol)

def clear(Directory):
    # clear folder
    print(fill("resetting directory", 60, '-'))
    i = 0
    directory = os.listdir(Directory)
    dirlen = len(directory)
    for filename in directory:
        i+=1
        os.remove(f"{Directory}/{filename}")
        print(f"    [{i}/{dirlen}]removing file")
    print("    Done!\n")

class Processor:
    def __init__(self):
        self.i=0
        self.o=0
    def processFile(self, filename, rawDirectory, newDirectory):
        filepath = f"{rawDirectory}/{filename}"
        newname = f"NEW {filename}"
        ID = filename[:5]
        if (not os.path.exists(newDirectory)):
            os.makedirs(newDirectory)
        shutil.copyfile(f"{filepath}", f"{newDirectory}/{ID}")
        self.o+=1
        print(f"    [{self.o}] pasting {filename} to {newDirectory}/{ID}\n", end = "")
    def copydir(self, rawDirectory, newDirectory):
        #read old folder
        directory = os.listdir(rawDirectory)
        threads = list()
        for filename in directory:
            #if folder
            if ("." not in filename):
                #print()
                print(f"{newDirectory}/{filename}\n", end = "")
                self.copydir(f"{rawDirectory}/{filename}", f"{newDirectory}/{filename}")
            else:
                #if file
                selfThread = threading.Thread(target=self.processFile, args=(filename, rawDirectory, newDirectory))
                threads.append(selfThread)
                selfThread.start()

if __name__ == "__main__":
    printer = Processor()
    clear("./DummyFolderNew") # Clearing of new directory of organized files
    print(fill("Moving Files to new Directory", 60, '-'))
    printer.copydir("./Dummy Folder", "./DummyFolderNew")# Reference old DIR for moving to new DIR
