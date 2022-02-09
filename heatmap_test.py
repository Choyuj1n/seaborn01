import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('flights')

# print(data)


data = data.pivot('month','year','passengers')
# print(data)

plt.pcolor(data)
plt.show()