from Binpacking.bin import work

__author__ = 'Schrabauke'
import csv
import glob

with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(len(a))

    f = open('filename.txt', 'w')
    f.write('%d' % len(a))
    f.close()

    outf.write('{}'.format(len(a)))  # more "modern"
    outf.write('%d' % len(a))        # deprecated mostly
    # import glob

for filename in glob.glob("C:/Users/Schrabauke/Desktop/PythonProjects/Data/*"):
    print(filename)
    with open(filename.read().split('\n')) as f:
        work(f)

glob.iglob("C:/Users/Schrabauke/Desktop/PythonProjects/Data/*")
test = open(tryi[1]).read().split('\n')
tryi = []
tryi = glob.glob("C:/Users/Schrabauke/Desktop/PythonProjects/Data/*")
for item in tryi:
    data = open(item).read().split('\n')
    work(data)

 f = open('exactfit.txt', 'w')
    f.close()
 for item in tryi:
    f.write("%s\n" % item)

    castdata(data)
elements = data.pop(0)
binsize = data.pop(0)

test = exactfit(data, binsize)