# -*- cODsing: utf-8 -*-
"""
Created on Sat Apr 20 15:04:09 2024

@author: jamis
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr

font = {'fontname':'Cambria'}
mpl.rcParams.update({'font.size': 10})
mpl.rcParams['font.family'] = 'Cambria'
def get_data(file_names):
    growth_data = []
    for input_file in file_names:
        # print('opening file')
        input_ref = open(input_file + '.txt', 'r')
        input_contents = []
        for line in input_ref:
            line = line.strip()
            data = line.split('\t')
            for i in range(len(data)):
                data[i] = float(data[i])
            input_contents.append(data)
        # print(input_contents)
        input_ref.close()
        growth_data.append(input_contents)
    # print(growth_data)
    return growth_data
        
def plt_data(growth_data, growth_list):
    count = 0
    for i in range(len(growth_data)):
        count += 1
        times = []
        ODs = []
        OD_errors = []
        growth_name = growth_list[i]
        for j in range(len(growth_data[i])):
            times.append(growth_data[i][j][0])
            ODs.append(growth_data[i][j][1])
            OD_errors.append(growth_data[i][j][2])
        plt.grid(True, which="both")
        plt.errorbar(times, ODs, marker = 'o', yerr=OD_errors, xerr=None,
                     fmt='black', ecolor=None, elinewidth=1, capsize=3,
                     barsabove=False, lolims=False, uplims=False,
                     xlolims=False, xuplims=False, errorevery=1,
                     capthick=None, data=None, label = growth_name)
        # plt.plot(times, ODs, 'black', label = growth_name, linewidth = 1)
        # plt.xlim([0, 150])
        # plt.title(growth_name, fontsize = 12, **font)
        plt.yscale('log')
        
        if count == 1:
            plt.ylim([0.001, 1])  # Set upper y limit
            plt.gca().yaxis.set_major_formatter(tkr.ScalarFormatter())
            plt.ticklabel_format(axis = 'y', style = 'plain')
        else:
            plt.ylim([0.1, 1])  # Set upper y limit
            plt.gca().yaxis.set_major_formatter(tkr.ScalarFormatter())
            plt.gca().yaxis.set_minor_formatter(tkr.ScalarFormatter())
            plt.ticklabel_format(axis = 'y', style = 'plain')
        
        plt.xlabel('Time (hrs)', fontsize = 12, **font)
        plt.ylabel('OD600', fontsize = 12, **font)
        plt.tight_layout()
        plt.savefig('{} Growth Curve.png'.format(growth_list[i]), dpi = 384)
        plt.show()
    return None

def main():
    file_names = ['Pb- Growth Curve',
                  'Pb+ Growth Curve']
    growth_list = ['B. megaterium Growth Curve (Pb-Free)',
                   'B. megaterium Growth Curve (0.1 mM Pb)']
    growth_data = get_data(file_names)
    plt_data(growth_data, growth_list)
    
if __name__ == '__main__':
    main()