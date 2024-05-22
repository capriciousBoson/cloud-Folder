import grpc
import sys
from grpc_file_server_pb2 import FileUploadRequest, FileDownloadRequest, FileDeleteRequest, FileRenameRequest
from grpc_file_server_pb2_grpc import FileServiceStub
import re
import os

def upload_file(stub, file_path):
    """
    Uploads a file to the gRPC server.

    Args:
        stub: gRPC stub for communication with the server.
        file_path (str): Path to the file to be uploaded.
    """

    # Open the file specified by file_path in binary read mode ('rb')
    # and read the contents of the file in a variable "file_data"
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as file:
            file_data = file.read()
    else:
        file_data = "new_dir"

    file_name = extract_file_name(file_path=file_path)

    #print("file path as seen by client app",file_path)
    # Create a gRPC request object (upload_request) of type FileUploadRequest 
    # Invoke the UploadFile method on the request object with gRPC stub and file data as arguments
    upload_request = FileUploadRequest(file_name=file_name, file_data=file_data)
    upload_response = stub.UploadFile(upload_request)

    print("Upload Response:", upload_response)


# def download_file(stub, file_name):
#     """
#     Downloads a file from the gRPC server.

#     Args:
#         stub: gRPC stub for communication with the server.
#         file_name (str): Name of the file to be downloaded.
#     """
#     download_request = FileDownloadRequest(file_name=file_name)
#     download_response = stub.DownloadFile(download_request)
    

#     # Initializing an empy bytes object to store complete file data
#     file_data = b''

#     try:
#         # Iterate over the response stream (download_response) received from the server.
#         # append each data chunk from the stream to the file_data variable.
#         for chunk in download_response:
#             file_data += chunk.data_chunks

#     except grpc.RpcError as e:
#         print(f" Error during downloading file : {e.details()}")
#         return

#     download_file_path = f"downloads/downloaded_{file_name}"

#     with open(download_file_path, 'wb') as file:
#         file.write(file_data)
    
#     print(f"File '{file_name}' downloaded successfully to {download_file_path}")

def delete_file(stub, file_name):
    """
    Deletes a file on the gRPC server.

    Args:
        stub: gRPC stub for communication with the server.
        file_name (str): Name of the file to be deleted.
    """
    #print("this is the name of the file as seen by delete function .. ", file_name)
    delete_request = FileDeleteRequest(file_name=file_name)
    delete_response = stub.DeleteFile(delete_request)
    print("Delete Response:", delete_response)

# def rename_file(stub, old_file_name, new_file_name):
#     """
#     Renames a file on the gRPC server.

#     Args:
#         stub: gRPC stub for communication with the server.
#         old_file_name (str): Name of the original file which to be renamed.
#         new_file_mame (str): New name of the file.
#     """
#     rename_request = FileRenameRequest(old_file_name=old_file_name, new_file_name=new_file_name)
#     rename_response = stub.RenameFile(rename_request)
#     print("Rename Response:", rename_response)

def extract_file_name(file_path):
    # Using a regex to extract the file name from the path
    match = re.search(r'[^\\/]+$', file_path)
    if match:
        return match.group(0)
    else:
        return None


def run():

    # Initialize a gRPC channel to connect to the server running on 'localhost:50051'.
    # Create a gRPC stub using the initialized channel
    channel = grpc.insecure_channel('localhost:50051')
    stub = FileServiceStub(channel)

    if len(sys.argv) < 3:
        print("Usage: python file_client.py <operation> <file_name>")
        sys.exit(1)

    operation = sys.argv[1].lower()
    if operation != "rename" : 
        file_name = ' '.join(sys.argv[2:]) 
    else: 
        file_name = sys.argv[2]

    if operation == 'upload':
        upload_file(stub, file_name)
    # elif operation == 'download':
    #     download_file(stub, file_name)
    elif operation == 'delete':
        delete_file(stub, file_name)
    # elif operation == 'rename':
    #     if len(sys.argv) < 4:
    #         print("Usage: python file_client.py rename <old_file_name> <new_file_name>")
    #         sys.exit(1)
    #     new_file_name = sys.argv[3]
    #     rename_file(stub, file_name, new_file_name)
    else:
        print("Invalid operation. Supported operations: upload, download, delete, rename")

if __name__ == '__main__':
    run()
