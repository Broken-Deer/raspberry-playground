rpicam-vid -t 0 -n --codec libav --libav-format mpegts --width 1920 --height 1080 -o - | cvlc stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/stream1}'
