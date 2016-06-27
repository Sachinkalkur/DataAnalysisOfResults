import numpy
from matplotlib import pyplot
import pandas

df = pandas.read_csv("Studentmarks-296.csv")
names = df.Name
roll = df['Reg. No.']
kannadaMarks = df.KANNADA
pyplot.plot(kannadaMarks)
pyplot.show()
print names[0], roll[0]