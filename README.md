# VideoDecodingusingGPU

This repository emphaasizes my brief exposure with FFMPEG. Here, I have gone through the process of how I compiled my FFMPEG on Windows system. This repo also deals with Transcoding, Decoding and Encoding of the video on the NVIDIA hardware accelerator. 

## Transcoding
**Command Used**

We used the command given below ```ffmpeg -y -vsync 0 -hwaccel cuvid -resize 320x180 -c:v h264_cuvid -i ./Data/Source/Source1.mp4 -c:a copy -c:v h264_nvenc -b:v 5M ./Data/Transcoded/T_1.mp4'''

**Before Transcoding**

<img src="https://github.com/AnshMittal1811/VideoDecodingusingGPU/blob/master/Images/01.%20Normal.jpg" alt="NormalTask#1" width="512"/>

**After Transcoding**

<img src="https://github.com/AnshMittal1811/VideoDecodingusingGPU/blob/master/Images/02.%20Transcoded.jpg" alt="TranscodingTask#1" width="512"/>
