# -*- cconcing: utf-8 -*-
"""
Created on Sat Apr 20 16:05:01 2024

@author: jamis
"""

import matplotlib.pyplot as plt

font = {'fontname':'Cambria'}

def get_data(file_names):
    conc_data = []
    for input_file in file_names:
        # print('opening file')
        input_ref = open(input_file + '.txt', 'r')
        data_set = []
        data_abio = []
        data_bio = []
        line_count = 0
        for line in input_ref:
            line = line.strip()
            data = line.split('\t')
            for i in range(len(data)):
                data[i] = float(data[i])
            if line_count % 2 == 0:
                data_abio.append(data)
            else:
                data_bio.append(data)
            line_count += 1
            # print(line_count)
        input_ref.close()
        data_set.append(data_abio)
        data_set.append(data_bio)
        conc_data.append(data_set)
    # print(conc_data)
    return conc_data
        
def plt_data(conc_data, conc_list):
    for i in range(len(conc_data)):
        for j in range(len(conc_data[i])):
            if j % 2 == 0:
                series = 'Abiotic'
                color = 'tab:red'
                symbol = '^'
            else:
                series = 'Biotic'
                color = 'tab:blue'
                symbol = 'o'
            times = []
            concs = []
            conc_errors = []
            conc_name = conc_list[i]
            for k in range(len(conc_data[i][j])):
                times.append(conc_data[i][j][k][0])
                concs.append(conc_data[i][j][k][1])
                conc_errors.append(conc_data[i][j][k][2])
            plt.errorbar(times, concs, marker = symbol, yerr=conc_errors, xerr=None,
                         fmt=color, linewidth = None, ecolor=None, elinewidth=1,
                         capsize=3, barsabove=False, lolims=False, uplims=False,
                         xlolims=False, xuplims=False, errorevery=1,
                         capthick=None, data=None, label = series)
        plt.grid()
        plt.xlim([0, 160])
        plt.ylim([0, 100])
        # plt.title(conc_name, fontsize = 12, **font)
        plt.xticks(fontsize = 10, **font)
        plt.yticks(fontsize = 10, **font)
        plt.xlabel('Time (hrs)', fontsize = 12, **font)
        plt.ylabel('[Pb] (µM)', fontsize = 12, **font)
        plt.legend(loc='lower right', fontsize = 10)
        plt.tight_layout()
        plt.savefig('{} Conc Curve.png'.format(conc_list[i]), dpi = 384)
        plt.show()
    return None

def main():
    file_names = ['Pb Conc',
                  'Pb Conc FS']
    conc_list = ['Pb Concentration (No Filter)',
                 'Pb Concentration (Filter)']
    conc_data = get_data(file_names)
    plt_data(conc_data, conc_list)
    
if __name__ == '__main__':
    main()