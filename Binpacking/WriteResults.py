__author__ = 'Schrabauke'
import csv

with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(len(a))

    f = open('filename.txt', 'w')
    f.write('%d' % len(a))
    f.close()

    outf.write('{}'.format(len(a)))  # more "modern"
    outf.write('%d' % len(a))        # deprecated mostly
