# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:00:48 2024

@author: jamis
"""

## https://github.com/marcharper/python-ternary

import ternary

def get_data(file_name):
    file_data = []
    input_ref = open(file_name + '.txt', 'r')
    for line in input_ref:
        line = line.strip()
        data = line.split('\t')
        for i in range(len(data)):
            data[i] = float(data[i])
        file_data.append(data)
    input_ref.close()
    # print(file_data)
    return file_data

def plt_data(data):
    ## Boundary and Gridlines
    scale = 100
    figure, tax = ternary.figure(scale=scale)

    # Draw Boundary and Gridlines
    tax.boundary(linewidth=1.5)
    tax.gridlines(color="black", multiple=10, ls = '-')
    tax.gridlines(color="blue", multiple=5, linewidth=0.5)

    # Plot a few different styles with a legend
    points = data
    tax.scatter(points, marker='o', color='red', edgecolor='k', s=15, label='')
    # tax.legend()

    # Set Axis labels and Title
    fontsize = 12
    offset = 0.14
    
    # tax.set_title("", fontsize=fontsize)
    tax.left_axis_label("Cl (Atomic %)", fontsize=fontsize, offset=offset)
    tax.right_axis_label("P (Atomic %)", fontsize=fontsize, offset=offset)
    tax.bottom_axis_label("Pb (Atomic %)", fontsize=fontsize, offset=offset)

    # Set ticks
    tax.ticks(axis='lbr', linewidth=1, multiple=10, offset=0.02)

    # Background color
    tax.set_background_color(color="whitesmoke", alpha=0.7) # the default, essentially

    # Remove default Matplotlib Axes
    tax.clear_matplotlib_ticks()
    tax.get_axes().axis('off')
    
    tax.savefig('Ternary Diagram.png', dpi = 384)
    ternary.plt.show()

def main():
    file_name = 'Ternary Data'
    print(file_name)
    data = get_data(file_name)
    print(data)
    plt_data(data)
    
if __name__ == '__main__':
    main()