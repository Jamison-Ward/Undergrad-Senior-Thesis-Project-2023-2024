# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:42:57 2024

@author: jamis
"""

import matplotlib.pyplot as plt

font = {'fontname':'Cambria'}

def get_data(file_name):
    file_data = []
    input_ref = open(file_name + '.txt', 'r', encoding = 'utf-8')
    
    for i, line in enumerate(input_ref):
        if i == 0:
            line = line.strip()
            headers = line.split('\t')
            # headers = sorted(headers, reverse = True)
            # print(headers)
        else:
            line = line.strip()
            data = line.split('\t')
            for i in range(len(data)):
                data[i] = float(data[i])
            file_data.append(data)
    # print(file_data)
    
    ## Group the data by variable type
    data_ordered = []
    k = 0
    for i in range(len(headers)):
        header_variable = []
        # print(k)
        for j in range(len(file_data)):
            header_variable.append(file_data[j][k])
        k += 1
        data_ordered.append(header_variable)
        # print('appended data')
    
    ## Sort the data by variable name
    data_dict = {i: j for i, j in zip(headers, data_ordered)}
    sorted_data_dict = dict(sorted(data_dict.items(), reverse = True))
    
    headers = []
    sorted_data = []
    for keys, values in sorted_data_dict.items():
        headers.append(keys)
        sorted_data.append(values)
        
    input_ref.close()
    
    return headers, sorted_data
        
def plt_data(headers, data):
    for i in range(len(data)-1):
        plt.plot(data[0], data[i+1], label = headers[i+1])
        #print(headers[i+1])
        
    plt.grid(True, which="both")
    plt.xlim([3, 9])
    plt.yscale('log')
    plt.ylim([1e-10, 1e35])
    plt.yticks([1e-10, 1e-5, 1e0, 1e5, 1e10, 1e15, 1e20, 1e25, 1e30, 1e35])
    
    ## Change 1e0 y-tick label to 1
    tick_labels = plt.gca().get_yticklabels()
    tick_labels[2] = '1'
    plt.gca().set_yticklabels(tick_labels)
        
    plt.xlabel('pH', fontsize = 12, **font)
    plt.ylabel('Mineral Saturation (Q/K)', fontsize = 12, **font)
    plt.tight_layout()
    plt.legend()
    plt.savefig('Pb-PO4 Mineral Sat', dpi = 384)
    plt.show()

    return None

def main():
    file_name = 'Pb-Po4 Mineral Sat'
    # print(file_name)
    headers, data = get_data(file_name)
    # headers
    # print(data)
    plt_data(headers, data)
    
if __name__ == '__main__':
    main()