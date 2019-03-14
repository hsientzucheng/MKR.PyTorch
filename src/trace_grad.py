import os, sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plot_grad_flow(named_parameters, output_name=None):
    ave_grads = []
    layers = []
    fig = plt.figure()
    for n, p in named_parameters:
        if(p.requires_grad) and ("bias" not in n):
            layers.append(n)
            #print(n)
            if p.grad is not None:
                ave_grads.append(p.grad.abs().mean())
            else:
                ave_grads.append(-1)
    plt.plot(ave_grads, alpha=0.3, color="b")
    plt.hlines(0, 0, len(ave_grads)+1, linewidth=1, color="k" )
    plt.xticks(range(0,len(ave_grads), 1), layers, rotation="vertical")
    plt.xlim(xmin=0, xmax=len(ave_grads))
    plt.xlabel("Layers")
    plt.ylabel("average gradient")
    plt.title("Gradient flow")
    plt.grid(True)
    plt.tight_layout()

    if output_name is not None:
        print("Save grad file to {}".format(output_name))
        fig.savefig(output_name)

def plot_grad_flow_mean(named_parameters, output_name=None):
    '''Plots the gradients flowing through different layers in the net during training.
    Can be used for checking for possible gradient vanishing / exploding problems.

    Usage: Plug this function in Trainer class after loss.backwards() as
    "plot_grad_flow(self.model.named_parameters())" to visualize the gradient flow
    Code from: https://discuss.pytorch.org/t/check-gradient-flow-in-network/15063/10 '''
    ave_grads = []
    max_grads= []
    layers = []
    fig = plt.figure()
    for nn, pp in named_parameters:
        if(pp.requires_grad) and ("bias" not in nn):
            layers.append(nn)
            if pp.grad is None:
                ave_grads.append(-1)
                max_grads.append(-1)
            else:
                ave_grads.append(pp.grad.abs().mean())
                max_grads.append(pp.grad.abs().max())
    plt.bar(np.arange(len(max_grads)), max_grads, alpha=0.1, lw=1, color="c")
    plt.bar(np.arange(len(max_grads)), ave_grads, alpha=0.1, lw=1, color="b")
    plt.hlines(0, 0, len(ave_grads)+1, lw=2, color="k" )
    plt.xticks(range(0,len(ave_grads), 1), layers, rotation="vertical")
    plt.xlim(left=0, right=len(ave_grads))
    plt.ylim(bottom = -0.001, top=0.02) # zoom in on the lower gradient regions
    plt.xlabel("Layers")
    plt.ylabel("average gradient")
    plt.title("Gradient flow")
    plt.grid(True)
    plt.legend([Line2D([0], [0], color="c", lw=4),
                Line2D([0], [0], color="b", lw=4),
                Line2D([0], [0], color="k", lw=4)], ['max-gradient', 'mean-gradient', 'zero-gradient'])
    plt.tight_layout()
    if output_name is not None:
        print("Save grad file to {}".format(output_name))
        fig.savefig(output_name, dpi=fig.dpi)



