# Python Speech To Text Transcription :speaking_head: :arrow_right: :scroll:
Using the Whisper API we can transcribe audio clips of any length to create a transcription file that contains all the words said in the audio clip.
 
### Motivation :rocket:
------------------
Ever watched a Youtube video or anything with closed captions on? At some point in time people actually had to listen to audio and do live transcriptions. In this digital age we can do away witht the stenographers and use AI models to transcribe text for us.

## Required Python Packages

[Whisper](https://github.com/openai/whisper) - A general purpose speech recognition model that takes our audio file and returns the text in a dictionary.

```
pip install git+https://github.com/openai/whisper.git 
```

[moviepy](https://pypi.org/project/moviepy/) - We will be using a function from moviepy that allows us to split clips and create sub clips since Whisper models are optimized for 30 second clips.

 ```
pip install moviepy
 ```
 
[Mutagen](https://pypi.org/project/mutagen/) - Python audio library that allows us to extract metadata about audio files, we will use it to obtain the length of the audio file.

 ```
pip install mutagen
 ```
 ------------
 
 ## Installing ffmpeg and Chocolatey (Required)
 
 This project requires you have ffmpeg installed, I reccommend installing it through chocolatey as installing it through pip may still cause errors. Open **PowerShell** as **Administrator** and run the following commands:
 
 ### Set Eexecution Policies
 1. - You will have to set your execution policy to AllSigned so that chocolatey can install properly.
 
 ```PowerShell
Set-ExecutionPolicy AllSigned
 ```
 
 2. - After this you can install chocolatey with the following command:
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
 3. - Now you can install ffmpeg with the following command:
 
 ```Powershell
 choco install ffmpeg
 ```
 ---------------------
 
## Transcribing your Audio

I have made it relatively easy for you to transcribe your files, it is essentially plug an play. There are two files, one is a module that detects the length of your audio clip and 
generates a text file of the time codes in 30 second intevals. These timecodes will be used by the splitClip() function to generate 30 second video chunks.

1. Simply add the relative path of your audio file **(all audio files must be in .wav format)**. Select the amount of words you wanter per line, default is 10.


```python
def main():

    file = "your_audio_here.wav"
    # Number of words per line
    words_per_line = 10
    transcribe(file, words_per_line)
```

- Make sure all files are in the root directory of whatever folder you are working in, refer to the picture below.

![Sample directory](https://i.ibb.co/4mh6GJh/image.png)

- When you run the script, you should see terminal prints from moviepy letting you know the sub clips are generating, and after a short time you will see the status of your transcription. Refer to the picture below

![Success example](https://i.ibb.co/C8k9rMR/image.png)

- Once the script terminates your transcription will be in the generate "transcript.txt" file.
------------

## Errors :x:
- Potential errors

```PowerShell
FileNotFoundError: [WinError 2] The system cannot find the file specified
```
If this happens check your path and make sure it is correect. If the path is correct it means you did not install ffmpeg which is required. Refer to [Installing ffmpeg and Chocolatey (Required)](installing-ffmpeg-and-chocolatey-(required)) above on how to install.
