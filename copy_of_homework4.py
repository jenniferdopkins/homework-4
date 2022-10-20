# -*- coding: utf-8 -*-
"""Copy of homework4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k8jojYIJP8hIYXVr89MHnFL1xYhOB5wN
"""

#1a
import numpy as np
numbers = np.array([[1, 2, 3, 4] , [5, 6, 7, 8], [ 9, 10, 11, 12]])
print(numbers * 2)

#1b
for row in numbers:
  for column in row:
    print(column, end=' ')
  print()

#1c
for i in numbers.flat:
  print(i, end = ' ')

#2
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1,2,3,4,5,6])
ypoints = np.array([5, 6,7,8,9,10])
plt.plot(xpoints, ypoints)
plt.show()

#2a
import matplotlib.pyplot as plt
import numpy as np
xpoints=([3,6,9,12])
ypoints=([2,8,1,10])
plt.plot(xpoints, ypoints, marker = 'o')
plt.show()

#3
import matplotlib.pyplot as plt
import numpy as np
xpoints=([0,1,2,3,4,5])
ypoints=([2,4,6,14,10,12])
plt.plot(xpoints, ypoints, marker = 's', ms= 10, linestyle = '--', mec='g', mfc='g', color='r' )

#4
import matplotlib.pyplot as plt
import numpy as np
x1=([0,4])
y1=([0,4])
x2=([0,4])
y2=([5,9])
x3=([0,4])
y3=([9,13])
plt.plot(x1,y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.show()

#5
import matplotlib.pyplot as plt
import numpy as np
marks = {'Andy':88, 'Amy':66, 'James': 90, 'Jules': 55, 'Arthur': 77}
values = marks.values()
mylabels =['Andy', 'Amy', 'James', 'Jules', 'Arthur']
plt.pie(values, labels=mylabels)
plt.legend(bbox_to_anchor=(1.05, 1.0), loc = 'upper left')
plt.show()

#6
import matplotlib.pyplot as plt
import numpy as np
x1=([0,4])
y1=([0,4])
x2=([0,4])
y2=([5,9])
x3=([0,4])
y3=([9,13])

plt.subplot(2, 3, 1)
plt.plot(x1,y1)
plt.plot(x2, y2)
plt.plot(x3, y3)

x=(["cats", "dogs", "mice"])
y=([5,3, 4])
plt.subplot(2,3,2)
plt.bar(x,y)

y=np.array([25, 35, 20, 8])
mylabels=["Jenny", "Carrie", "Rob", "Shawn"]
plt.subplot(2,3,3)
plt.pie(y, labels = mylabels)

x = np.array([0,1,2,3,4])
y= np.array([5, 6, 8, 12, 10])
plt.subplot(2,3,4)
plt.plot(x, y)
plt.grid(color='r', linestyle = '--', linewidth = .5)

x = np.array([7,8,3,6])
y = np.array([55, 33, 33, 22])
plt.subplot(2,3,5)
plt.scatter(x,y)

x = np.random.normal(100, 50, 300)
plt.subplot(2,3,6)
plt.hist(x)

plt.show()