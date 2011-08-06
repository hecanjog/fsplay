import sys
import random
import wave

def main(argv):
    if len(argv) > 1 and len(argv) < 3:
        try:
            rawdata = open(argv[1])
            rawdata = rawdata.read()
        except:
            print "not a valid file, yo"
    else:
        print 'oops, what file should I read?'
        print 'try something like this:'
        print
        print 'python fsplay.py /full/path/to/file'
        exit()

    filename = 'output' + str(random.random() * 100000) + '.wav'
    outputfile = wave.open(filename, 'w')
 
    outputfile.setnchannels(1)
    outputfile.setsampwidth(1)
    outputfile.setframerate(11025)
    outputfile.setcomptype('NONE', 'not compressed')

    print 'writing', len(rawdata), 'frames...'

    outputfile.writeframes(rawdata)
    outputfile.close()

    print 'listen to this:', filename

if __name__ == '__main__':
    main(sys.argv)
