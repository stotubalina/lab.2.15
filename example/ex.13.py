#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open("file2.txt", "r") as filptr:
        print("The filepointer is at byte:", filptr.tell())
        filptr.seek(10)
        print("After reading, the filepointer is at:", filptr.tell())


        