#!/usr/bin/env python
from matplotlib import rcParams
import matplotlib.pyplot as plt 
import cycler,json,matplotlib,os
loc=os.path.dirname(os.path.realpath(__file__))
pal_path = os.path.join(loc,'aesthetics.json')
palettes = json.load(open(pal_path))
def available(show=True):
    if not show:
        return palettes.keys()
    else:
        f,ax = plt.subplots(4,2,figsize=(5,8))
        for i, name in enumerate(palettes.keys()):
            x,y = i //2, i %2
            cycle = palettes[name]
            for j,c in enumerate(cycle):
                ax[x,y].hlines(j,0,1,colors=c,linewidth=15)
            ax[x,y].set_ylim(-1,len(cycle))
            ax[x,y].set_title(name)
            despine(ax[x,y],True)
        plt.show()
def check_key(palname):
    try: palettes[palname]
    except KeyError:
        raise KeyError("{} not an accepted palette name. Check vapeplot.available() for available palettes".format(palname))
def cmap(palname):
    check_key(palname)
    return matplotlib.colors.ListedColormap(palettes[palname])
def despine(ax,all=False):
    if all==True:
        for sp in ax.spines:
            ax.spines[sp].set_visible(False)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    else:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
def font_size(s): matplotlib.rcParams.update({'font.size': s})
def palette(palname=None):
    if palname==None:
        return palettes
    else:
        check_key(palname)
        return palettes[palname]
def reverse(palname):
    check_key(palname)
    return list(reversed(palette(palname)))
def set_palette(palname):
        check_key(palname)
        rcParams['axes.prop_cycle'] = cycler.cycler(color=palettes[palname])
def view_palette(*args):
    if len(args) > 1:
        f, ax = plt.subplots(1,len(args),figsize=(3*len(args),3))
        for i, name in enumerate(args):
            check_key(name)
            cycle = palettes[name]
            for j,c in enumerate(cycle):
                ax[i].hlines(j,0,1,colors=c,linewidth=15)
            ax[i].set_title(name)
            despine(ax[i],True)
        plt.show()
    elif len(args) == 1:
        f = plt.figure(figsize=(3,3))
        check_key(args[0])
        cycle = palettes[args[0]]
        for j,c in enumerate(cycle):
            plt.hlines(j, 0, 1, colors=c, linewidth=15)
        plt.title(args[0])
        despine(plt.axes(),True)
        f.tight_layout()
        plt.show()
    else:
        raise NotImplementedError("ERROR: supply a palette to plot. check vapeplot.available() for available palettes")