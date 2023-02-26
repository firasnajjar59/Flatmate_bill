from filestack import Client

class FileShare:
    def __init__(self,file_path,api="AeAV3wpTcRsWMwc0yFRYkz"):
        self.api = api
        self.file_path = file_path
        print(self.file_path)
        print(self.api)

    def share(self):
        client = Client(self.api)
        new_filelink = client.upload(filepath=self.file_path)
        return new_filelink.url