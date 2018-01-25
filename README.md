# vapeplot

---

matplotlib extension for vaporwave aesthetics 

---

## install

```
pip install vapeplot
```

---

## demo

```
from vapeplot import vapeplot
import matplotlib.pyplot as plt
%matplotlib inline

vapeplot.font_size(16) # change font size
pal = vapeplot.palettes().vaporwave
for x in range(0,len(pal)):
    plt.scatter(x,1,color=pal[x],s=500)
    plt.text(x-0.2,0.997,'{}'.format(x))
vapeplot.despine(plt.axes()) # despine figure
plt.show()
```

![alt text](https://raw.githubusercontent.com/dantaki/vapeplot/master/vaporwave.png "extended vaporwave")

```
pal = vapeplot.palettes().cool
vapeplot.font_size(20) # change font size
for x in range(0,len(pal)):
    plt.scatter(x,1,color=pal[x],s=2500)
    plt.text(x-0.1,0.995,'{}'.format(x))
vapeplot.despine(plt.axes()) # despine figure
plt.show()
```

![alt text](https://raw.githubusercontent.com/dantaki/vapeplot/master/cool.png "cool vaporwave")

---

## api

`vapeplot.palettes()`
* Object containing lists of colors
* `vapeplot.palettes().vaporwave`
  * extended vaporwave palette
* `vapeplot.palettes().cool`
  * cool aesthetics

`vapeplot.despine(ax)`
  * removes the top and right axis

`vapeplot.font_size(s)`
  * change the font size globally 

## more to come :wink: