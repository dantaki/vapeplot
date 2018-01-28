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

![alt text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/vapeplot.png "vapeplot palettes")

#### view specific palettes

```
vapeplot.view_palette("cool",'sunset')
```

![alt text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/view_palette.png "cool sunset")

#### set the color palette

```
import numpy as np
import matplotlib.pyplot as plt

vapeplot.set_palette('vaporwave')
for i in range(10):
    plt.plot(range(100),np.random.normal(i,1,100))
vapeplot.despine(plt.axes()) #remove right and top axes
```

![alt text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/vaporwave.png "vaporwave palette")

#### make a colormap

```
cmap = vapeplot.cmap('crystal_pepsi')
A = np.random.rand(25, 25)
plt.imshow(A,cmap=cmap)
# remove all axes
vapeplot.despine(plt.axes(),True)
plt.show()
```

![alt text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/vapeplot_colormaps.png "crystal_pepsi colormap")


#### access a palette

```
# cool is a list of colors
cool = vapeplot.palette("cool")

# reverse the order of colors
seapunk_r = vapeplot.reverse("seapunk")

```

---

## examples

plots produced with [seaborn tutorials](https://seaborn.pydata.org/examples/index.html)

set the palette with vapeplot

```
pal =  sns.blend_palette(vapeplot.palette(palname))

g = sns.FacetGrid(df, row="g",hue="g", palette=pal)
```

### cool 

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/cool_seaborn_facetgrid.png "cool facetgrid")

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/cool_seaborn_kdeplot.png "cool kdeplot")


### crystal_pepsi

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/crystal_pepsi_seaborn_facetgrid.png "crystal_pepsi facetgrid")

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/crystal_pepsi_seaborn_kdeplot.png "crystal_pepsi kdeplot")

### jazzcup 

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/jazzcup_seaborn_facetgrid.png "jazzcup facetgrid")

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/jazzcup_seaborn_kdeplot.png "jazzcup kdeplot")

### macplus 

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/macplus_seaborn_facetgrid.png "macplus facetgrid")

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/macplus_seaborn_kdeplot.png "macplus kdeplot")

### mallsoft 

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/mallsoft_seaborn_facetgrid.png "mallsoft facetgrid")

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/mallsoft_seaborn_kdeplot.png "mallsoft kdeplot")

### seapunk 

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/seapunk_seaborn_facetgrid.png "seapunk facetgrid")

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/seapunk_seaborn_kdeplot.png "seapunk kdeplot")

### sunset

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/sunset_seaborn_facetgrid.png "sunset facetgrid")

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/sunset_seaborn_kdeplot.png "sunset kdeplot")

### vaporwave 

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/vaporwave_seaborn_facetgrid.png "vaporwave facetgrid")

![alt_text](https://raw.githubusercontent.com/dantaki/vapeplot/master/examples/vaporwave_seaborn_kdeplot.png "vaporwave kdeplot")

---

## api

* `vapeplot.available(show=True)`
  * function to plot all vapeplot palettes
  * `show=False` prints palette names


* `vapeplot.cmap(palname)`
  * returns a colormap object
  * `palname` is the name of the color palette


* `vapeplot.despine(ax,all=False)` 
  * removes figure axes
  * default action: remove right and top axes
  * `all=True` removes all axes


* `vapeplot.font_size(s)`
  * change the font size globally


* `vapeplot.palette(palname)`
  * returns a list of colors
  * if no `palname` is given, a dict of all the palettes is returned


* `vapeplot.reverse(palname)`
  * returns a list of colors in reverse



* `vapeplot.set_palette(palname)`
  * change the color palette globally



* `vapeplot.view_palette(*args)`
  * view individual palettes
  * arguments: one or more palette names

---


## more to come :wink:
