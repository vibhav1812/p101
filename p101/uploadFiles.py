import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from): #for example file name is uploadFiles.py which is inside p101 folder(root)
            for file_name in files:
                local_path = os.path.join(root, file_name)
                print(local_path)
                #contruct the full dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                #upload the file 
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path, mode = WriteMode('overwrite'))
            

                
def main():
    access_token = 'sl.BP4k62D7BZi-tIqKwKvcbf4ucAy0o7WXuH39qDVdtCCcMbrYRw81O_LXJijpjI6laLe4H3G6tdGxZ5N1NqHLqR55p9UBzPXnyLr71AU2LMsdx2Arb9YLy77rpmQT8ZvNBjW43rwzvt4'
    transferData = TransferData(access_token)

    file_from = input('Enter the folder path that you want to upload on DropBox: ' )
    file_to = input('Enter the dropbox path you want to upload it in: ')  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print('File Uploaded Successfully')

main()