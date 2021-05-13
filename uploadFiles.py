import os
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx =  dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            f = open(file_from, 'rb')
            dbx.files_upload(f.read(), file_to)
            

def main():
    access_token = 'lslluDCKn0sAAAAAAAAAAeuA6eE0F2MO1RpGuBo8YWj3mB8uxn-Y3Qd2A57j9yQn'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")   
    transferData.upload_file(file_from, file_to)

main()