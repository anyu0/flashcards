def mkdic(f1,f2):
    f=open(f1)
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

    k = open(f2,'w')
    k.write('{\n')
    for x in dic.keys():
        k.write('"{}":"{}",\n'.format(x,dic[x]))

    k.write('}\n')
    k.close()
    return len(dic.keys())

def main(args):
    parse_args(args)
    mkdic(files[0],files[1])

if __name__ == '__main__':
    main(sys.argv[1:])
