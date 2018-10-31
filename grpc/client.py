import grpc

import example_pb2
import example_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = example_pb2_grpc.RecorderStub(channel)
        track_v = example_pb2.TrackDesc(id=0, pid=2064, type="video", codec="mpeg2video", tag="img_main_vid", resolution="720x576", frame_rate=25)
        track_a = example_pb2.TrackDesc(id=1, pid=2068, type="audio", codec="aac", tag="img_main_aud", sampling_rate=48000)
        response = stub.StartRecorder(example_pb2.RecorderParams(event_id='abcdefg',
                                ingest_name="img_main", udp_url="udp://127.0.0.1:1234", primary=True, \
                                tracks=[track_v, track_a]))
    print("Recorder client received: " + response.message)


if __name__ == '__main__':
    run()
