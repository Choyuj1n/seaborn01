import seaborn as sns
import matplotlib.pyplot as plt

sns.regplot
iris = sns.load_dataset('iris')

sns.regplot(x='petal_length', y='petal_width', data=iris)
# sns.scatterplot
plt.show()