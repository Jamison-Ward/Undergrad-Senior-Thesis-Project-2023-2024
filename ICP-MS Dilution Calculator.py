# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 13:31:38 2022

@author: jamis
"""

c1_mL = float(input('Enter the initial molar concentration (mM): '))
c2_ppb = float(input('Enter the desired final concentration (ppb): '))
V2_mL = float(input('Enter the desired solution volume (mL): '))
atom_w = float(input('Enter the atmoic wight of the solute (g/mol): '))

c1_ppb = c1_mL * atom_w * 1000
V1_mL = (c2_ppb / c1_ppb) * V2_mL
V_H2O = V2_mL - V1_mL

print('\nDilute {:.3f} g of {:.3f} mM solution with {:.3f} g of H2O'
      .format(V1_mL, c1_mL, V_H2O))