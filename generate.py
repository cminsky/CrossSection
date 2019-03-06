from setup import *

db_begin('data')
molDict = {1:'H2O',2:'CO2',3:'O3',
            6:'CH4',22:'N2',45:'H2'}

def crossSection(molSet,p=1.0,T=296.0,profile='Voigt',gamma='air'):
    # wavRange = wavenumber tuple min, max
    # molSet = list of tables
    # envir = pressure temp dict
    # profile = coeff calculator
    # gamma = self, air, etc
    if profile in ['HT','Voigt','Lorentz','Doppler']:
        func = eval('absorptionCoefficient_'+profile)
    else:
        raise ValueError('Line shape must be HT, Voigt, Lorentz, or Doppler.')
    if gamma in ['air','self']:
        gL = 'gamma_'+gamma
    envir = {'p':p,'T':T}
    nu,coef = func(SourceTables=molSet,Environment=envir,GammaL=gL)
    return (nu,coef)

def databaseGen(tRange,tStep,pRange,pStep,compList,pickleSave=True):
    # tRange, pRange = temp and pressure tuples with min, max
    # tRange, pStep = temp and presure step size
    # compList = list of molecule numbers
    tArange = np.arange(tRange[0],tRange[1]+tStep,tStep)
    pArange = np.arange(pRange[0],pRange[1]+pStep,pStep)
    wavNums = len(crossSection([[molDict[compList[0]]]])[0])
    db = np.empty((len(tArange),len(pArange),len(compList),wavNums))
    for t in range(len(db)):
        tVal = tArange[t]
        for p in range(len(db[t])):
            pVal = pArange[p]
            for c in range(len(db[t][p])):
                cVal = compList[c]
                mol = molDict[cVal]
                nu,coef = crossSection([mol],p=pVal,T=tVal)
                db[t][p][c] = coef
    if pickleSave:
        filename = 'db'+str(tRange[0])+str(tRange[1])+str(tStep)+str(pRange[0])+str(pRange[1])+str(pStep)
        outfile = open(filename,'wb')
        pickle.dump(db,outfile)
        outfile.close()
    return db
