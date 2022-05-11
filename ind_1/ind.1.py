#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


if __name__ == "__main__":
    with open("file3.txt", "r") as file:
        for line in file.readlines():
            split_line = line.split()
            split_line = iter(split_line)
            print(''.join(
                [f'{two} {one}' for one, two in zip(split_line, split_line)]

                        )
            )




