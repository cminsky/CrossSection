from setup import *

db_begin('data')

AllParamGroups = ['160-char','Standard','LineMixing',
                  'Voigt','SDVoigt','Galatry']

wavMin,wavMax = 3400,4100

# https://hitran.org/lbl/2?1=on&2=on&3=on&6=on&22=on&45=on

fetch('H2O',1,1,wavMin,wavMax)
fetch('CO2',2,1,wavMin,wavMax)
fetch('O3',3,1,wavMin,wavMax)
fetch('CH4',6,1,wavMin,wavMax)
fetch('N2',22,1,wavMin,wavMax)
fetch('H2',45,1,wavMin,wavMax)

# isn't connecting to HITRAN; use Jupyter notebook for now

print('Fetched')
