class File:
    def __init__(self, vFileName) -> None:
        self.vFileName = vFileName
        self.file = None
    def open(self):
        self.file = open(self.vFileName, "a+", encoding="utf-8")
    def write(self, text):
        self.file.write(text)
    def read(self):
        return self.file.read()