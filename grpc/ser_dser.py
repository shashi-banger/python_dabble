import example_pb2
from google.protobuf import json_format as json_format

track_v = example_pb2.TrackDesc(id=0, pid=2064, type="video", codec="mpeg2video", tag="img_main_vid",\
                         resolution="720x576", frame_rate=25)
track_a = example_pb2.TrackDesc(id=1, pid=2068, type="audio", codec="aac", tag="img_main_aud",\
                         sampling_rate=48000)
recorder_params = example_pb2.RecorderParams(event_id='abcdefg',
             ingest_name="img_main", udp_url="udp://127.0.0.1:1234", primary=True, \
             tracks=[track_v, track_a])

s = recorder_params.SerializeToString()
print(s)

rec_recorder_params = example_pb2.RecorderParams()
rec_recorder_params.ParseFromString(s)

j = json_format.MessageToJson(rec_recorder_params)
print(j)

