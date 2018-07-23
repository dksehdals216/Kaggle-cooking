


import numpy as np
import json
import csv
import re
import string
from pprint import pprint


def normalizeStr(s):
    s = re.sub(r"[^a-zA-Z.!?]+", r" ", s.lower().strip())
    return s

def readFile():
    print("Reading File")

    with open('data/train.json', encoding='utf-8') as data_f:
        data = json.loads(data_f.read())
        #data = json.dumps(data_f.read())

    #train file looks like:
    '''
    {
        "id": 10259,
        "cuisine": "greek",
        "ingredients": [
         "romaine lettuce",
         "black olives",
         ....
    }
    '''
    print(data[0]["id"])
    #print(data)
    


def preprint(arg_s):

    print("\'t\' to print test.json")
    print("\'r\' to print train.json")
    print("\'s\' to print sample_submission.csv")

    print("Enter command:")
    cmd_args = input()

    if cmd_args == 't':
        with open('data/test.json') as f:
            data = json.load(f)
            pprint(data)

    elif cmd_args == 'r':
        with open('data/train.json') as f:
            data = json.load(f)
            pprint(data)

    elif cmd_args == 's':
        with open('data/sample_submission.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    else:
        print("invalid input")
readFile()

