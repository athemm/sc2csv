from PIL import Image, ImageOps
import numpy as np


import csv

def csvWriter(fil_name, nparray):
  example = nparray.tolist()
  with open(fil_name+'.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerows(example)


import ast

def csvReader(fil_name):
  with open(fil_name+'.csv', 'r') as f:
    reader = csv.reader(f)
    examples = list(reader)
    examples = np.array(examples)
  t1=[]
  for x in examples:
    t2=[]
    for y in x:
      z= ast.literal_eval(y)
      t2.append(np.array(z))
    t1.append(np.array(t2))
  ex = np.array(t1)
  return ex

def convert(args):
    for arg in args:
            print("Converting",arg,"to csv...")
            img = np.array(Image.open(arg))
            csvWriter(arg.replace(".png", ""),img)
    print("done!")

def cycletest():
    for image in __import__("os").listdir():
        if image.endswith(".png"):
            img = np.array(Image.open(image))
            csvWriter(image,img)
            backToNumpyArray = csvReader(image)
            Image.fromarray(np.uint8(backToNumpyArray)).save(f"{image}.cycled.png")

