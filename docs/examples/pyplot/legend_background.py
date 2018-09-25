
import numpy             as np
import matplotlib.pyplot as plt

plt.style.use(['goose', 'goose-latex'])

fig, ax = plt.subplots()

for i in range(10):
  ax.plot([0,1], [i/10,(i+10)/10], label=r'$i = {0:d}$'.format(i))

ax.legend(loc='center right', facecolor='white', framealpha=1)

plt.savefig('legend_background.svg')
plt.show()