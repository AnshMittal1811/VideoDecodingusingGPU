# VideoDecodingusingGPU

This repository emphaasizes my brief exposure with FFMPEG. Here, I have gone through the process of how I compiled my FFMPEG on Windows system. This repo also deals with Transcoding, Decoding and Encoding of the video on the NVIDIA hardware accelerator. 

## Prerequisites
Here, I mention the prerequisites to install and compile FFMPEG to your system for Windows. The following are the steps for the installation and compilation of FFMPEG.

- Step 1: Install msys2 from [msys2](www.msys2.org)
- Step 2: Clone ffnvcodec by typing the following in the Prompt: ```git clone https://git.videolan.org/git/ffmpeg/nv-codec-headers.git```
- Step 3: Clone FFmpeg's public GIT repository in the same folder: ```git clone https://git.ffmpeg.org/ffmpeg.git```
- Step 4: Create a folder named nv_sdk in the parent directory of FFmpeg and copy all the header files from C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v8.0\include and library files from C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v8.0\lib\x64 to nv_sdk folder.

- Step 5:



## Initial State of GPU Hardware
The following image presents a performance profile for the NVIDIA GTX1060 GPU on my system. 
<img src="https://github.com/AnshMittal1811/VideoDecodingusingGPU/blob/master/Images/01.%20Normal.jpg" alt="NormalTask#1" width="512"/>


## Transcoding
**Command Used**

We used the following command for transcoding the Video:```ffmpeg -y -vsync 0 -hwaccel cuvid -resize 320x180 -c:v h264_cuvid -i ./Data/Source/Source1.mp4 -c:a copy -c:v h264_nvenc -b:v 5M ./Data/Transcoded/T_1.mp4```. The hardware encoder and decoder changes in the performace profile can be observed in the following image.

**After Transcoding**

<img src="https://github.com/AnshMittal1811/VideoDecodingusingGPU/blob/master/Images/02.%20Transcoded.jpg" alt="TranscodingTask#1" width="512"/>


## Encoding and Decoding

### Encoding

**Command Used**

We used the following command for encoding the Video: ```ffmpeg -y -vsync 0 -s 160x90 -i ./Data/Y_U_V_file1.yuv -c:v h_264_nvenc ./Data/Encode1.mp4```. The hardware encoder changes in the performace profile can be observed in the following image.

**After Transcoding**

<table>
  <tr>
    <td valign="top"><img src="https://github.com/AnshMittal1811/VideoDecodingusingGPU/blob/master/Images/04.01.%20Encoded_files.jpg" alt="EncodingTask#1" width="512"></td>
    <td valign="top"><img src="https://github.com/AnshMittal1811/VideoDecodingusingGPU/blob/master/Images/04.02.%20Encoded_files.jpg" alt="EncodingTask#2" width="512"></td>
  </tr>
</table>


### Decoding

**Command Used**

We used the following command for decoding the Video: ```ffmpeg -y -vsync 0 -c:v h264_cuvid -i ./Data/Source1.mp4 ./Data/Y_U_V_file1.yuv```. The hardware decoder changes in the performace profile and the folder under consideration can be observed in the following image.

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

# FINAL RESULTS
## After FFMPEG and OpenCV used for Decoding
The hardware encoder changes in the performace profile can be observed in the following image.

<img src="https://github.com/AnshMittal1811/VideoDecodingusingGPU/blob/master/Images/06.%20EncodingusingPythonOpenCV.jpg" alt="TranscodingTask#1" width="512"/>

