import logs_pb2
import sys
from google.protobuf import json_format as json_format

log_video_start = logs_pb2.VideoStart(log_id=logs_pb2.VIDEO_START, s_pl_cookie="abc:1", u_segment_id=1, u_duration_ms=100)

log_video_end = logs_pb2.VideoEnd(log_id=logs_pb2.VIDEO_END, s_pl_cookie="abc:1", u_segment_id=1, u_played_dur=80)

vid_start_bytes = log_video_start.SerializeToString()
vid_end_bytes = log_video_end.SerializeToString()


l_hdr = logs_pb2.LogHdr()
l_hdr.ParseFromString(vid_start_bytes)
print(l_hdr)

if l_hdr.log_id == logs_pb2.VIDEO_START:
    vid_start_rec = logs_pb2.VideoStart()
    vid_start_rec.ParseFromString(vid_start_bytes)
    j = json_format.MessageToJson(vid_start_rec)
    print(j)
else:
    print("Error: Expected VideoStart")
    sys.exit(1)


l_hdr = logs_pb2.LogHdr()
l_hdr.ParseFromString(vid_end_bytes)
print(l_hdr)

if l_hdr.log_id == logs_pb2.VIDEO_END:
    vid_end_rec = logs_pb2.VideoEnd()
    vid_end_rec.ParseFromString(vid_end_bytes)
    j = json_format.MessageToJson(vid_end_rec)
    print(j)
else:
    print("Error: Expected VideoEnd")
    sys.exit(1)
