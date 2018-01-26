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

#### view all palettes

```
import vapeplot
%matplotlib inline

vapeplot.available()
```

![alt text](https://raw.githubusercontent.com/dantaki/vapeplot/master/vapeplot.png "vapeplot palettes")

#### view specific palettes

```
vapeplot.view_palette("cool",'sunset')
```

![alt text](https://raw.githubusercontent.com/dantaki/vapeplot/master/view_palette.png "cool sunset")

#### set the color palette

```
import numpy as np
import matplotlib.pyplot as plt

vapeplot.set_palette('vaporwave')
for i in range(10):
    plt.plot(range(100),np.random.normal(i,1,100))
vapeplot.despine(plt.axes()) #remove right and top axes
```

![alt test](https://raw.githubusercontent.com/dantaki/vapeplot/master/vaporwave.png "vaporwave palette")

#### access a palette

```
# cool is a list of colors
cool = vapeplot.pal().cool

# reverse the order of colors
seapunk_r = list(reversed(vapeplot.pal().seapunk))

```

---

## api

* `vapeplot.pal()`
  * object of palettes 
  * attribute is the palette name
  * value is a list of colors

  * `vapeplot.pal().macplus # returns a list of macplus colors`


* `vapeplot.available(show=True)`
  * function to plot all vapeplot palettes
  * `show=False` prints palette names


* `vapeplot.despine(ax,all=False)` 
  * removes figure axes
  * default action: remove right and top axes
  * `all=True` removes all axes


* `vapeplot.font_size(s)`
  * change the font size globally


* `vapeplot.set_palette(palname)`
  * change the color palette globally
  * `palname` is the name of the color palette

* `vapeplot.view_palette(*args)`
  * view individual palettes
  * arguments: one or more palette names

---


## more to come :wink:
