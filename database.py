from setup import *

testing = False

def crossSection(mol,wavRange,wavStep=0.01,
                p=1.0,T=296.0,
                profile='Voigt',broadeners={'air':1.0}):
    # wavRange = wavenumber list min, max
    # molSet = list of tables
    # envir = pressure temp dict
    # profile = coeff calculator
    # broadeners = dict of broadener, mixing ratio
    if profile in ['HT','Voigt','Lorentz','Doppler']:
        func = eval('absorptionCoefficient_'+profile)
    else:
        raise ValueError('Line shape must be HT, Voigt, Lorentz, or Doppler.')
    envir = {'p':p,'T':T}
    nu,coef = func(SourceTables=[mol],WavenumberRange=wavRange,WavenumberStep=wavStep,Environment=envir,Diluent=broadeners,HITRAN_units=True)
    return (nu,coef)

if testing:
	nu,coef = crossSection('CO2',wavRange=[2000.,2100.],wavStep=1)
	plt.plot(nu,coef)
	plt.show()

def databaseGen(molSet=['CO2'],wavRange=[2020.,2100.],wavStep=0.01,
                tRange=[296,296],tStep=1,
                pRange=[1,1],pStep=1,
                profile='Voigt',broadeners={'air':1.0}):
    # molSet = list of molcules
    # tRange, pRange,wavRange = lists with min, max
    # tRange, pStep = temp and pressure step size
    # profile = string
    # broadeners = dict
    tArange = np.arange(tRange[0],tRange[1]+tStep,tStep)
    pArange = np.arange(pRange[0],pRange[1]+pStep,pStep)
    db = []
    for tVal in tArange:
        tList = []
        for pVal in pArange:
            pList = []
            for mol in molSet:
                nu,coef = crossSection(mol,wavRange=wavRange,wavStep=wavStep,
                                        p=(1*10**pVal),T=tVal,
                                        profile=profile,broadeners=broadeners)
                molList = [i for i in coef]
                pList.append(molList)
            tList.append(pList)
        db.append(tList)
    db = np.array(db)
    info_dict = {'t_vec':tArange,
                'p_vec':pArange,
                'mols':molSet,
                'wavs':nu,
                'sigma':db}
    return info_dict
