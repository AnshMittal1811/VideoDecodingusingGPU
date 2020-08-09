import subprocess

ffmpeg_cmd = ["ffmpeg",  "-y",
                "-vsync", "0",
                "-hwaccel",  "nvdec",
                "–s","1280x720", 
                "-c:v",  "h264_cuvid",
                "-i", "./Data/Source1.mp4",
                "-preset", "slow",
                "-b:v", "5M",
                "./Data/outTrans.yuv"]

