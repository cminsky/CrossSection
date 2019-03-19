from hapi import *
import numpy as np
import matplotlib.pyplot as plt
import pickle

db_begin('data')

wavMin,wavMax = 0,30000

# https://hitran.org/lbl/2?1=on&2=on&3=on&6=on&22=on&45=on

new = False

if new:

	fetch('H2',45,1,wavMin,wavMax) # molecular hydrogen
	fetch('O2',7,1,wavMin,wavMax) # molecular oxygen
	fetch('N2',22,1,wavMin,wavMax) # molecular nitrogen
	fetch('CO',5,1,wavMin,wavMax) # carbon monoxide

	fetch('H2O',1,1,wavMin,wavMax) # water
	fetch('CO2',2,1,wavMin,wavMax) # carbon dioxide
	fetch('O3',3,1,wavMin,wavMax) # ozone
	fetch('N2O',4,1,wavMin,wavMax) # nitrous oxide

	fetch('C2H2',26,1,wavMin,wavMax) # acetylene
	fetch('CH4',6,1,wavMin,wavMax) # methane
	fetch('C2H6',27,1,wavMin,wavMax) # ethane

print('Done')
