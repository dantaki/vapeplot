# vapeplot

---

matplotlib extension for vaporwave aesthetics 

---

## install

```
pip install 
```

## demo

```
import vapeplot
import matplotlib.pyplot as plt
%matplotlib inline 

# simple vaporwave palette
pal = vapeplot.palettes().vaporwave
for x in range(0,len(pal)):
	plt.scatter(x,1,color=pal[x],s=250)
plt.show()
```

## api
