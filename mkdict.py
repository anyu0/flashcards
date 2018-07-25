# read plain txt file (f1) and generate a         dictionary (f2)

import os
import sys

dic={}
files=[]
# Default input dir: ./unprocessed
dir_in = "./unprocessed/"
# Default output dir: ./processed
dir_out = "./processed/"

'''
def readable(path):
    return os.access(path, os.R_OK)
'''

def parse_args(args):
    #end_args = False
    #var_arg  = None
    for a in args:
        files.append(a)

def mkdict(f1):
    f_in = dir_in + f1
    f_out = dir_out + f1 + "_dict"
    f=open(f_in)
    f.readline()
    for l in f:
        l=l.strip()
        if len(l) == 0:
            continue
        w = l.split(";")

        for i in range(len(w)):
            w[i]=w[i].lstrip()

        dic[w[0]] = w[1]
    f.close()

    k = open(f_out,'w')
    k.write('{\n')
    for x in dic.keys():
        k.write('"{}":"{}",\n'.format(x,dic[x]))

    k.write('}\n')
    k.close()
    return len(dic.keys())

def main(args):
    parse_args(args)
    mkdict(files[0])

if __name__ == '__main__':
    main(sys.argv[1:])
