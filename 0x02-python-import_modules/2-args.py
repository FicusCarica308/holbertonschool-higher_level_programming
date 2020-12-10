#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    av_lgt = len(argv)
    if av_lgt == 1:
        print("0 arguments.")
    elif av_lgt == 2:
        print("1 argument:\n1: {}".format(argv[1]))
    elif av_lgt > 2:
        print("{} arguments:".format(av_lgt - 1))
        count = 0
        for i in argv:
            if count != 0:
                print("{0}: {1:s}".format(count, i))
            count = count + 1
