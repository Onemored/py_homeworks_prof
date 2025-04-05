import os

class FileIterator:
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        self.files = self.get_files_list(self.path)
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.files):
            raise StopIteration
        return self.files[self.cursor]

    def get_files_list(self, path):
        result = []
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                result.append(file)
            else:
                result.extend(self.get_files_list(os.path.join(path, file)))
        return result


for file in FileIterator('test'):
    print(file)