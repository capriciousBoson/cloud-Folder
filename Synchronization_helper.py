import grpc
from grpc_file_server_pb2_grpc import FileServiceStub
from grpc_file_server_pb2 import FileDownloadRequest
import os
import time
import subprocess
import sys

def synchronize_folder_with_server(folder_to_monitor):
    while True:
        current_files = set(os.listdir(folder_to_monitor))
        server_files = set(os.listdir("uploads"))

        # Upload new files to the server
        new_files = current_files - server_files
        for file_name in new_files:
            file_path = os.path.join(folder_to_monitor, file_name)
            print(f"This file is being uploaded: {file_path}")
            upload_file_to_server(file_path)

        # Delete files that are not present locally
        missing_files = server_files - current_files
        for file_name in missing_files:
            print(f"This file is being deleted: {file_name}")
            delete_file_on_server(file_name)

        time.sleep(5)
        print("Refreshing files...")  
        # Adjust the interval based on your requirements

def get_server_files():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = FileServiceStub(channel)

        # Use the FileServiceStub to get the list of files currently on the server
        # You might need to modify this based on your actual FileService implementation
        # For example, you might have a ListFiles method in your FileService
        try:
            server_files = set(file.file_name for file in stub.ListFiles(FileDownloadRequest()))
            return server_files
        except grpc.RpcError as e:
            print(f"Error fetching server files: {e}")
            return set()

def upload_file_to_server(file_path):
    # Run the filesystem_client.py script to upload the file to the server
    command = f"python filesystem_client.py upload {file_path}"
    subprocess.run(command, shell=True)

def delete_file_on_server(file_name):
    
    # Run the filesystem_client.py script to delete the file on the server
    command = f"python filesystem_client.py delete {file_name}"
    subprocess.run(command, shell=True)

if __name__ == '__main__':
    folder_to_monitor = sys.argv[1]
    synchronize_folder_with_server(folder_to_monitor)