import sys 
import re

def out(in_string):
    no_vowel = re.sub(r"[aoyeui]", "", in_string.lower())
    consonant_transform = re.sub(r"(\w)", r".\g<1>", no_vowel)
    print(consonant_transform)

if __name__ == "__main__":
    out(input())