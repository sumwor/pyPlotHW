# make a class of plot contain general settings (axis, font, legend, etc)

# output: ax, fig handles
import matplotlib.pyplot as plt
import os

class StartPlots:
    # set font
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 20

    # set line width
    plt.rcParams["lines.linewidth"] = 1

    # set line width of x/y axis
    plt.rcParams["axes.labelweight"] = 0.5

    # set colormap
    plt.rcParams['image.cmap'] = 'jet'


    def __init__(self):

        self.ax, self.fig = plt.subplots()

        # set plot top/right boundaries to invisible
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

    def legend(self, leg):
        # add legend
        legend = self.ax.legend(leg)
        legend.get_frame().set_linewidth(0.0)
        legend.get_frame().set_facecolor('none')

    def save_plot(self, title, type, figpath):
        # save fig in specified type.
        # 'tiff', 'svg', etc
        """
        :param title: name of the figure, '*.pdf'
        :param type: extension name of the figure, 'tiff', 'svg', etc.
        :param figpath: the desired directory to save the figure
        :return:
        """
        # check if the directory exist
        if not os.path.exists(figpath):
            os.makedirs(figpath)

        self.fig.savefig(title, format=type)

# another class to generate subplots
class StartSubplots(StartPlots):

    def __init__(self, xdim, ydim, ifSharex=False, ifSharey=False):
        self.ax, self.fig = plt.subplots(xdim, ydim, sharex=ifSharex, sharey=ifSharey)

        # set plot top/right boundaries to invisible
        for xx in range(xdim):
            for yy in range(ydim):
                self.ax[xx,yy].spines['top'].set_visible(False)
                self.ax[xx,yy].spines['right'].set_visible(False)