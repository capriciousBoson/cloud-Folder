import grpc
from concurrent import futures
from grpc_file_server_pb2 import FileUploadRequest, FileUploadResponse, FileDownloadRequest, FileChunk, FileDeleteRequest, FileDeleteResponse, FileRenameRequest, FileRenameResponse
from grpc_file_server_pb2_grpc import FileServiceServicer, add_FileServiceServicer_to_server
import os

class FileServer(FileServiceServicer):
    # class FileServer that extends FileServiceServicer to handle service requests

    def UploadFile(self, request, context):
        """
        Handles file upload requests from clients.

        Args:
            request (FileUploadRequest): The gRPC request containing file metadata and data.
            context (grpc.ServicerContext): The context for the service method.

        Returns:
            FileUploadResponse: The gRPC response indicating the success of the upload.
        """
    

        file_name = request.file_name
        file_data = request.file_data
        upload_dir = "uploads/"
        file_path = upload_dir + file_name

        with open(file_path, "wb") as file:
            file.write(file_data)

        response = FileUploadResponse(success=True, message="File upload was successfull !!!")
        return response

    # def DownloadFile(self, request, context):
    #     """
    #     Handles file download requests from clients.

    #     Args:
    #         request (FileDownloadRequest): The gRPC request containing the file name to be downloaded.
    #         context (grpc.ServicerContext): The context for the service method.

    #     Yields:
    #         FileChunk: A gRPC response containing file data in chunks.
    #     """

    #     saved_data_dir = "uploads/"
    #     file_path = os.path.join(saved_data_dir, request.file_name)

    #     try:
    #         with open(file_path, 'rb') as file:
    #             while True:
    #                 data_chunk = file.read(1024)
    #                 if not data_chunk : 
    #                     break
    #                 yield FileChunk(data_chunks=data_chunk)
    #     except FileNotFoundError:
    #         context.set_details(f"File '{request.file_name}' not found !!! ")
    #         context.set_code(grpc.StatusCode.NOT_FOUND)
    #         return
         
    def DeleteFile(self, request, context):
        """
        Handles file deletion requests from clients.

        Args:
            request (FileDeleteRequest): The gRPC request containing the file name to be deleted.
            context (grpc.ServicerContext): The context for the service method.

        Returns:
            FileDeleteResponse: The gRPC response indicating the success of the deletion.
        """
        file_name = request.file_name

        # Specify the upload directory
        upload_directory = "uploads/"

        file_path = os.path.join(upload_directory , file_name)
        #print("FIle path in delete function ",file_path)
        try:
            # Delete the file
            os.remove(file_path)
            response = FileDeleteResponse(success=True, message="File deleted successfully")
        except FileNotFoundError:
            response = FileDeleteResponse(success=False, message=f"File '{file_name}' not found.")
            context.set_details(f"File '{file_name}' not found.")
            context.set_code(grpc.StatusCode.NOT_FOUND)
        except Exception as e:
            response = FileDeleteResponse(success=False, message=str(e))
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
        
        return response

    # def RenameFile(self, request, context):
    #     """
    #     Handles file renaming requests from clients.

    #     Args:
    #         request (FileRenameRequest): The gRPC request containing old and new file names.
    #         context (grpc.ServicerContext): The context for the service method.

    #     Returns:
    #         FileRenameResponse: The gRPC response indicating the success of the renaming.
    #     """

    #     old_file_name = request.old_file_name
    #     new_file_name = request.new_file_name

    #     # Specify the server's data directory
    #     data_directory = "uploads/"

    #     old_file_path = data_directory + old_file_name
    #     new_file_path = data_directory + new_file_name

    #     try:
    #         # rename the file
    #         os.rename(old_file_path, new_file_path)
    #         response = FileRenameResponse(success=True, message="File renamed successfully")
    #     except FileNotFoundError:
    #         response = FileRenameResponse(success=False, message=f"File '{old_file_name}' not found.")
    #         context.set_details(f"File '{old_file_name}' not found.")
    #         context.set_code(grpc.StatusCode.NOT_FOUND)
    #     except Exception as e:
    #         response = FileRenameResponse(success=False, message=str(e))
    #         context.set_details(str(e))
    #         context.set_code(grpc.StatusCode.INTERNAL)
        
    #     return response
    
    def ListFiles(self, request, context):
        # Placeholder implementation to return the list of files on the server
        # You may want to modify this based on how you store and manage file information
        file_names = os.listdir("uploads")
        for file_name in file_names:
            yield FileUploadResponse(success=True, message=file_name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_FileServiceServicer_to_server(FileServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
