import matplotlib.pyplot as plt
data=[33,25,20,12,10]

plt.axes(aspect=1)
plt.title("pie")
plt.pie(data,labels=("oil","gas","nuclear","natural","other"))
plt.show()
