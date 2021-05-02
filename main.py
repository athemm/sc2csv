import os, sys
import lib.pngsclib
import lib.pngarraylib


def main(to_process):
    for file in to_process:
        junk = lib.pngsclib.convert(file,os.getcwd())
        lib.pngarraylib.convert(junk)
        for subfile in junk:
            os.remove(subfile)

to_process = []

for file in os.listdir():
    if file.endswith("_tex.sc"):
        to_process.append(file)

main(to_process)
    
