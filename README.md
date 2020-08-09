# VideoDecodingusingGPU

This repository emphaasizes my brief exposure with FFMPEG. Here, I have gone through the process of how I compiled my FFMPEG on Windows system. This repo also deals with Transcoding, Decoding and Encoding of the video on the NVIDIA hardware accelerator. 

## Initial State of GPU Hardware
The following image presents a performance profile for the NVIDIA GTX1060 GPU on my computer.

<img src="https://github.com/AnshMittal1811/VideoDecodingusingGPU/blob/master/Images/01.%20Normal.jpg" alt="NormalTask#1" width="512"/>


## Transcoding
**Command Used**

We used the following command for transcoding the Video:```ffmpeg -y -vsync 0 -hwaccel cuvid -resize 320x180 -c:v h264_cuvid -i ./Data/Source/Source1.mp4 -c:a copy -c:v h264_nvenc -b:v 5M ./Data/Transcoded/T_1.mp4```. The hardware encoder and decoder changes in the performace profile can be observed in the following image.

**After Transcoding**

<img src="https://github.com/AnshMittal1811/VideoDecodingusingGPU/blob/master/Images/02.%20Transcoded.jpg" alt="TranscodingTask#1" width="512"/>


## Encoding and Decoding

**Command Used**

We used the following command for decoding the Video: ```ffmpeg -y -vsync 0 -hwaccel cuvid -resize 320x180 -c:v h264_cuvid -i ./Data/Source/Source1.mp4 -c:a copy -c:v h264_nvenc -b:v 5M ./Data/Transcoded/T_1.mp4```. The hardware decoder changes in the performace profile and the folder under consideration can be observed in the following image.

**After Transcoding**

<table>
  <tr>
    <td>Performance Profile</td>
     <td>Files in Folder</td>
  </tr>
  <tr>
    <td valign="top"><img src="https://github.com/AnshMittal1811/VideoDecodingusingGPU/blob/master/Images/03.%20Decoded.jpg" alt="DecodingTask#1" width="512"></td>
    <td valign="top"><img src="https://github.com/AnshMittal1811/VideoDecodingusingGPU/blob/master/Images/03.01.%20Decoded_files.jpg" alt="DecodingProfile#1" width="512"></td>
  </tr>
</table>
