
import matplotlib.pyplot as plt
import goosempl          as gplt
import numpy             as np

plt.style.use(['goose','goose-latex'])

# ------------------------------------------------------------------------------

def distribution(a=100, b=3, g=-.3, size=10000):

  r = np.random.random(size=size)

  return (a**g + (b**g - a**g)*r)**(1./g)

# ------------------------------------------------------------------------------

data = distribution()

fig, axes = plt.subplots(ncols=3, nrows=2, figsize=(3*8,2*6))

# --- histogram ---

P,x = gplt.histogram(data, bins=41, density=False)

gplt.hist(P,x,facecolor=[.2,.2,.2],axis=axes[0,0])

P,x = gplt.histogram(data, bins=41, density=True)

gplt.hist(P,x,facecolor=[.2,.2,.2],axis=axes[1,0])

# --- histogram_log ---

P,x = gplt.histogram_log(data, bins=41, density=False)

gplt.hist(P,x,facecolor='b',axis=axes[0,1])

P,x = gplt.histogram_log(data, bins=41, density=True)

gplt.hist(P,x,facecolor='b',axis=axes[1,1])

# --- histogram_uniform ---

P,x = gplt.histogram_uniform(data, bins=41, density=False)

gplt.hist(P,x,facecolor='r',axis=axes[0,2])

P,x = gplt.histogram_uniform(data, bins=41, density=True)

gplt.hist(P,x,facecolor='r',axis=axes[1,2])

# --- axes settings ---

axes[0,0].set_title(r'histogram')
axes[0,1].set_title(r'histogram\_log')
axes[0,2].set_title(r'histogram\_uniform')

for ax in axes.ravel():

  ax.set_xlabel(r'$x$')
  ax.set_ylabel(r'$N(x)$')

plt.savefig('histogram.svg')
plt.show()