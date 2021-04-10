#encoding:utf-8
'''
@File    :   atom.py
@Time    :   2021/04/08 22:14:54
@Author  :   ponychen 
@Version :   0.1
@Contact :   18709821294@outlook.com
@WebSite :   https://github.com/ponychen123
'''
# Start typing your code from here

import numpy as np 

# atom class to get the cell parameters and coordinates
class atom:
  def __init__(self,File=None):
    if File is None:
      self.filename = 'POSCAR' # default read POSCAR
    else:
      self.filename = File
    self.position = None # positions of atoms
    self.cell = None # lattice vectors (3x3) matrix
    self.symbol = None # element symbol of each atom 
    self.ele = None # element types and related numbers