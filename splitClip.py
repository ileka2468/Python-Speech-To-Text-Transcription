from mutagen.wave import WAVE
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def generateTimeCodes(filename):
    # obtains length of original video
    audio = WAVE(filename)
    audio_info = audio.info
    length = int(audio_info.length)
    print(f"{length} seconds.")

    # creates time code interval tuples and appends to list
    time_codes = []
    prev_num = 0
    for num in range(length):
        if num % 30 == 0 and num != 0:
            # print(f"{prev_num}, {num}")
            time_codes.append((prev_num, num))
            prev_num = num

    remainder = length - time_codes[-1][-1]
    time_codes.append((time_codes[-1][-1], time_codes[-1][-1] + remainder))
    # print(time_codes)

    # write time code tuples to file
    with open("time.txt", "w") as f:
        for index in time_codes:
            f.write(f"{index[0]}-{index[1]}\n")

# splits clip for each time interval and creates sub clip
def splitClip(filename):
    required_video_file = filename
    with open("time.txt") as f:
        times = f.readlines()
    times = [x.strip() for x in times]
    for time in times:
        starttime = int(time.split("-")[0])
        endtime = int(time.split("-")[1])
        ffmpeg_extract_subclip(required_video_file, starttime, endtime, targetname=str(times.index(time) + 1) + ".wav")
        num_of_clips = times.index(time) + 1
    return num_of_clips

# calls functions and splits clips
def main():
    file = "cool.wav"
    generateTimeCodes(file)

if __name__ == '__main__':
    main()