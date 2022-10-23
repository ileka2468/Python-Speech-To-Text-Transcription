from tkinter import *
import syllables
import string
import math




def speech_stats():
    file_words = []
    total_sylables = 0
    letter_count = 0
    sentences = 0

    # reads in text from file and adds words to a list
    with open("transcription.txt", "r") as f:
        for line in f:
            word_list = line.split(" ")
            file_words.extend(word_list)

    #  removes spaces and new line characters from list
    remove = ["\n", ""]
    for word in list(file_words):
        if word in remove:
            file_words.remove(word)

    for word in file_words:
        for letter in word:
            if letter == ".":
                sentences += 1

    # loops through each word and removes punctuation

    for word in range(len(file_words)):
        new_string = file_words[word].translate(str.maketrans('', '', string.punctuation))
        file_words[word] = new_string

    # estimates total syllables
    for word in file_words:
        total_sylables += syllables.estimate(word)
        for letter in word:
            letter_count += 1

    word_count = len(file_words)

    ease_score = round(206.835 - 1.015 * (word_count/ sentences) - 84.6 * (total_sylables / word_count))
    grade_level = round(0.39 * (word_count/ sentences) + 11.8 * (total_sylables/word_count) - 15.59)
    words_per_sentence = round(word_count / sentences)

    stats = {"word_count": word_count,
             "average_word_length": letter_count / word_count,
             "total_syllables": total_sylables,
             "number_of_sentences": sentences,
             "avg_word_per_sentences": words_per_sentence,
             "Speech Complexity": ease_score,
             "grade_level": grade_level
             }

    return stats


print(speech_stats())

if __name__ == '__main__':
    speech_stats()