Simulate RTP like udp communication

1. Run server.py on remote EC2 instance
2. Run client.py on local host with usage
  python client.py <ec2 instance ip> 20001 
3. Remote EC2 instance should have udp 20001 ingress port open

=============================================================

Description

- Client send a udp message to server
- Server on receiving knows the source udp ip and port
- Server sends a sequence of 100 packets which client receives. 
  If time between two sends in server is high client receive will 
  fail. This is to simulate udp media packets continuously sent by
  rtsp server

