#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


if __name__ == "__main__":
    with open("text.txt", "r") as file:
        string = ''
        string = "".join(file.readlines())
    words = string.split()
    words.sort(key=len, reverse=True)
    for word in words:
        if len(word) == len(words[0]):
            print(word)



