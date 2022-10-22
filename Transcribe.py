import whisper  # needs GitHub version, pip install git+https://github.com/openai/whisper.git
import splitClip

def main():

    file = "sample_audio.wav"
    # Number of words per line
    words_per_line = 10
    transcribe(file, words_per_line)

def transcribe(file, wpl):
    splitClip.generateTimeCodes(file)
    clips = splitClip.splitClip(file)
    print(clips)

    model = whisper.load_model("base")
    with open("transcription.txt", "w", encoding='utf-8') as f:
        print(f"Number of clips: {clips}")
        for num in range(1, clips + 1):
            print(f"{clips - num} left to be transcribed!")
            result = model.transcribe(f"{num}.wav", fp16=False)
            line = result["text"].split(" ")
            count = 0
            for word in line:
                count += 1
                f.write(word + " ")
                if count % wpl == 0:
                    f.write("\n")


main()
