import grpc
from concurrent import futures
import example_pb2
import example_pb2_grpc
import time
from google.protobuf import json_format as json_format

class Recorder(example_pb2_grpc.RecorderServicer):
    def StartRecorder(self, request, context):
        print(json_format.MessageToJson(request))
        return example_pb2.RecorderResponse(message="Success")

def serve():
     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
     example_pb2_grpc.add_RecorderServicer_to_server(Recorder(), server)
     server.add_insecure_port('[::]:50051')
     server.start()
     try:
         while True:
             time.sleep(5)
     except KeyboardInterrupt:
         server.stop(0)


if __name__ == '__main__':
     serve()
