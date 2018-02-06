#!/usr/bin/env python
from matplotlib import rcParams
import matplotlib.pyplot as plt 
import cycler,matplotlib

palettes = {
    "vaporwave" : ["#94D0FF","#8795E8","#966bff","#AD8CFF","#C774E8","#c774a9","#FF6AD5","#ff6a8b","#ff8b8b","#ffa58b","#ffde8b","#cdde8b","#8bde8b","#20de8b"],
    "cool" : ["#FF6AD5","#C774E8","#AD8CFF","#8795E8","#94D0FF"],
    "crystal_pepsi" : ["#FFCCFF","#F1DAFF","#E3E8FF","#CCFFFF"],
    "mallsoft" : ["#fbcff3","#f7c0bb","#acd0f4","#8690ff","#30bfdd","#7fd4c1"],
    "jazzcup" : ["#392682","#7a3a9a","#3f86bc","#28ada8","#83dde0"],
    "sunset" : ["#661246","#ae1357","#f9247e","#d7509f","#f9897b"],
    "macplus" : ["#1b4247","#09979b","#75d8d5","#ffc0cb","#fe7f9d","#65323e"],
    "seapunk" : ["#532e57","#a997ab","#7ec488","#569874","#296656"]
}
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