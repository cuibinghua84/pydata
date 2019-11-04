# -*- coding: utf-8 -*-
"""
@author: 东风
@file: word_count.py
@time: 2019/11/4 16:09
"""


def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exits."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filename = "D:/data/pcc/chapter_10/alice.txt"
count_words(filename)