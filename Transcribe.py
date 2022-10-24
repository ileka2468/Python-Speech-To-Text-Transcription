import whisper  # needs GitHub version, pip install git+https://github.com/openai/whisper.git
import splitClip
import os
from analyze import speech_stats

def main():

    file = "medschool_lecture.wav"
    # Number of words per line
    words_per_line = 10
    transcribe(file, words_per_line)
    display_stats(speech_stats())

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
            os.remove(f"{num}.wav")
            count = 0
            for word in line:
                count += 1
                f.write(word + " ")
                if count % wpl == 0:
                    f.write("\n")
def display_stats(dict):
    print(f"{'Speech Stats':_^60}")
    print(f"Speech Complexity Score: {dict.get('Speech Complexity')}")
    print(f"Speech Grade Level: {dict.get('grade_level')}")
    print(f"Total Word Count: {dict.get('word_count')}")
    print(f"Average Word Length: {dict.get('average_word_length')}")
    print(f"Total Number of Sentences: {dict.get('number_of_sentences')}")
    print(f"Average Words per Sentence: {dict.get('avg_word_per_sentences')}")
    print(f"Total Syllables Spoken: {dict.get('total_syllables')}")

main()
