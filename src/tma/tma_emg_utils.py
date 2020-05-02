"""
defines utility functions that supports tma_emg_learn.py
author(s) : Ashwin de Silva and Malsha Perera
"""

# import the libraries
import matplotlib as mpl

mpl.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd


def plot_latent_space(X_reduced, y_train, labels):
    """
    plot the reduced dim space
    """
    num_classes = len(np.unique(y_train))
    cmap = cm.get_cmap('jet')
    idx = np.linspace(0, 1, num_classes)
    colors = cmap(idx)

    for l, c in zip(np.unique(y_train), colors):
        plt.scatter(X_reduced[y_train == l, 0], X_reduced[y_train == l, 1], c=c, label=l)

    plt.xlabel('Dim 1')
    plt.ylabel('DIm 2')
    plt.legend(tuple(labels), loc='lower right')
    plt.show()


def plot_recording(data, fs):
    """
    plot the raw recordings from the acquisition system
    """
    fig = plt.figure()
    num_channels = data.shape[1]
    num_samples = data.shape[0]
    print(num_channels)
    axes = [fig.add_subplot('%i1' % num_channels + str(i)) for i in range(0, num_channels)]
    [(ax.set_ylim([-100, 100])) for ax in axes]
    t = np.array(list(range(num_samples))) / fs
    i = 0
    for ax in axes:
        ax.plot(t, data[:, i])
        i += 1
    plt.show()


def read_from_csv(file):
    """
    read the recordings from the .csv files
    """
    df = pd.read_csv(file, delimiter='\t')
    data = df.values
    data = data[:, 1:data.shape[1]]
    return data.T


def write_to_csv(file, data):
    """
    write data to .csv files
    """
    df = pd.DataFrame(data)
    df.to_csv(file, sep='\t')

# def get_corr_plot(X, title):
#     """
#     visualize the correlation matrix
#     """
#     df = pd.DataFrame(X.T)
#     corr = df.corr()
#     cm = plt.imshow(corr, cmap='Blues', vmin=0, vmax=1)
#     cm.set_cmap('Blues')
#     plt.colorbar()
#     plt.xticks(range(len(corr.columns)), corr.columns)
#     plt.yticks(range(len(corr.columns)), corr.columns)
#     plt.title(title)
#     plt.show()


# def plot_ethogram(t, pred, gestures):
#     """
#     plot the action ethogram
#     """
#     num_classes = len(gestures)
#     classes = list(range(0, num_classes))
#     cmap = cm.get_cmap('jet')
#     idx = np.linspace(0, 1, num_classes)
#     colors = cmap(idx)
#     for l, c in zip(classes, colors):
#         idx = np.where(pred == l)[0]
#         t_i = t[idx]
#         p_i = (l + 1) * np.ones(len(t_i))
#         plt.scatter(t_i, p_i, c=c, label=l)
#     plt.ylim((0, num_classes + 2))
#     plt.legend(gestures)
#     plt.xticks(np.arange(0, 130, step=5))
#     plt.grid()
#     plt.show()
