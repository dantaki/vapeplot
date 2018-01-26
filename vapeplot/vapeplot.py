#!/usr/bin/env python
class palettes():
    def __init__(self):
        self.vaporwave = ['#94D0FF','#8795E8','#966bff','#AD8CFF','#C774E8','#c774a9','#FF6AD5','#ff6a8b','#ff8b8b','#ffa58b','#ffde8b','#cdde8b','#8bde8b','#20de8b'] 
        self.cool = [ '#94D0FF','#a994ff','#bf94ff','#f494ff','#ff94b1']
def despine(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
def font_size(s):
    import matplotlib
    matplotlib.rcParams.update({'font.size': s})
