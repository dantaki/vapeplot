#!/usr/bin/env python
from matplotlib import rcParams
import matplotlib.pyplot as plt 
import cycler
import json,os

loc=os.path.dirname(os.path.realpath(__file__))
pal_path = os.path.join(loc,'aesthetics.json')
palettes = json.load(open(pal_path))
def available(show=True):
    if not show:
        return palettes.keys()
    else:
        f,ax = plt.subplots(4,2,figsize=(6,6))
        for i, name in enumerate(palettes.keys()):
            x,y = i //2, i %2
            cycle = palettes[name]
            for j,c in enumerate(cycle):
                ax[x,y].hlines(h,0,1,colors=c,linewidth=30)
            ax[x,y].set_title(name)
            despine(ax[x,y],True)
        f.tight_layout()
        plt.show()
def despine(ax,all=False):
    if all==True:
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    else:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
def font_size(s):
    import matplotlib
    matplotlib.rcParams.update({'font.size': s})
def set_palette(self,palname=None):
        try:
            vape_on(palettes[palname])
        except KeyError:
            raise KeyError("{} not an accepted palette name. Check vapeplot.available() for available palettes\n".format(palname))
def view_palette(*args):
    if len(args) > 1:
        f, ax = plt.subplots(1,len(args))
        for i, name in enumerate(args):
            cycle = palettes[name]
            for j,c in enumerate(cycle):
                ax[i].hlines(j,0,1,colors=c,linewidth=30)
            ax[i].set_title(name)
            despine(ax[i],True)
        f.tight_layout()
        plt.show()
    elif len(args) == 1:
        f = plt.figure()
        cycle = palettes[args[0]]
        for j,c in enumerate(cycle):
            plt.hlines(j, 0, 1, colors=c, linewidth=30)
        plt.title(args[0])
        despine(plt.axes(),True)
        f.tight_layout()
        plt.show()
    else:
        raise NotImplementedError("ERROR: supply a palette to plot. check vapeplot.available() for available palettes\n")
def vape_on(ccycle):
    rcParams['axes.prop_cycle'] = cycler.cycler(color=ccycle)
