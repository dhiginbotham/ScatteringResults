
#
# Electron Scattering Proton Radius Results 
# by Douglas.W. Higinbotham
#

import numpy as np
import matplotlib.pyplot as plt

mylist=np.array([
["Hand 1963",         1,  0.805,  0.011,  "https://doi.org/10.1103/RevModPhys.35.335"],
["Frerejacque 1966",  2,  0.800,  0.025,  "https://doi.org/10.1103/PhysRev.141.1308"],
["Akimov 1972",       3,  0.810,  0.020,  "http://www.jetp.ac.ru/cgi-bin/dn/e_035_04_0651.pdf"],
["Murphy 1974",       4,  0.810,  0.04,   "https://doi.org/10.1103/PhysRevC.9.2125"],
["Borkowski 1974",    5,  0.880,  0.030,  "https://doi.org/10.1016/0550-3213(75)90514-3"],
["Borkowski 1975",    6,  0.870,  0.020,  "https://doi.org/10.1007/BF01409496"],
["Hohler 1976",       7,  0.840,  0.01,   "https://doi.org/10.1016/0550-3213(76)90449-1"],
["Simon 1980",        8,  0.862,  0.012,  "https://doi.org/10.1016/0375-9474(80)90104-9"],
["McCord 1991",       9,  0.865,  0.020,  "https://doi.org/10.1016/0168-583X(91)96079-Z"],
["Wong 1994",        10,  0.877,  0.024,  "https://doi.org/10.1142/S0218301394000255"],
["Mergell 1996",     11,  0.847,  0.008,  "https://doi.org/10.1016/0375-9474(95)00339-8"],
["Rosenfelder 2000", 12,  0.880,  0.015,  "https://doi.org/10.1016/S0370-2693(00)00316-6"],
["Eschrich 2001",    13,  0.830,  0.036,  "https://doi.org/10.1016/S0370-2693(01)01285-0"],
["Sick 2003",        14,  0.895,  0.018,  "https://doi.org/10.1016/j.physletb.2003.09.092"],
["Kelly 2004",       15,  0.863,  0.004,  "https://doi.org/10.1103/PhysRevC.70.068202"],
["Blunden 2005",     16,  0.897,  0.018,  "https://doi.org/10.1103/PhysRevC.72.057601"],
["Belushkin 2007",   17,  0.844,  0.006,  "https://doi.org/10.1103/PhysRevC.75.035202"],
["Bernauer 2010",    18,  0.879,  0.008,  "https://doi.org/10.1103/PhysRevLett.105.242001"],
["Hill 2010",        19,  0.871,  0.009,  "https://doi.org/10.1103/PhysRevD.82.113005"],
["Borisyuk 2010",    20,  0.912,  0.011,  "https://doi.org/10.1016/j.nuclphysa.2010.05.054"],
["Ron 2011",         21,  0.875,  0.010,  "https://doi.org/10.1103/PhysRevC.84.055204"],
["Zhan 2011",        22,  0.875,  0.010,  "https://doi.org/10.1016/j.physletb.2011.10.002"],
["Sick 2012",        23,  0.886,  0.008,  "https://doi.org/10.1016/j.ppnp.2012.01.013"],
["Adamuscin 2012",   24,  0.849,  0.007,  "https://doi.org/10.1016/j.ppnp.2012.01.014"],
["Lorenz 2012",      25,  0.840,  0.01,   "https://doi.org/10.1140/epja/i2012-12151-1"],
["Graczyk 2014",     26,  0.899,  0.003,  "https://doi.org/10.1103/PhysRevC.90.054334"],
["Lorenz 2015",      27,  0.843,  0.004,  "https://doi.org/10.1103/PhysRevD.91.014023"],
["Arrington 2015",   28,  0.879,  0.011,  "https://doi.org/10.1063/1.4921430"],
["Lee 2015",         29,  0.904,  0.015,  "https://doi.org/10.1103/PhysRevD.92.013013"],
["Griffioen 2016",   30,  0.840,  0.016,  "https://doi.org/10.1103/PhysRevC.93.065207"],
["Higinbotham 2016", 31,  0.845,  0.005,  "https://doi.org/10.1103/PhysRevC.93.055207"],
["Horbatsch 2017",   32,  0.855,  0.011,  "https://doi.org/10.1103/PhysRevC.95.035203"  ],
["Alarcon 2019",     33,  0.844,  0.007,  "https://doi.org/10.1103/PhysRevC.99.044303"  ],
["Zhou 2019",        34,  0.845,  0.001,  "https://doi.org/10.1103/PhysRevC.99.055202"  ],
["Xiong 2019",       35,  0.831,  0.013,  "https://doi.org/10.1038/s41586-019-1721-2"  ],
["Mihovilovic 2020", 36,  0.851,  0.019,  "https://doi.org/10.3389/fphy.2020.00036"], 
["Alarcon 2020",     37,  0.842,  0.010,  "https://doi.org/10.1103/PhysRevC.102.035203"  ],
["Hayward 2020",     38,  0.842,  0.004,  "https://doi.org/10.1016/j.nuclphysa.2020.121767"],
["Mihovilovic 2021", 39,  0.878,  0.032,  "https://doi.org/10.1140/epja/s10050-021-00414-x" ],
["Atac 2021",        40,  0.852,  0.009,  "https://doi.org/10.1140/epja/s10050-021-00389-9"],
["Lin 2021",         41,  0.838,  0.005,  "https://doi.org/10.1016/j.physletb.2021.136254"],
["Cui 2021",         42,  0.847,  0.008,  "https://doi.org/110.1103/PhysRevLett.127.092001"],
["Lin 2022",         43,  0.840,  0.003,  "https://doi.org/10.1103/PhysRevLett.128.052002"],
["Gramolin 2022",    44,  0.889,  0.007,  "https://doi.org/10.1103/PhysRevD.105.054004"]
])

x  = mylist[:,2].astype(np.float)
y  = mylist[:,1].astype(np.float)
dx= mylist[:,3].astype(np.float) 
labels = mylist[:,0]
morelabels  = mylist[:,4]

xx  = mylist[:,2][6].astype(np.float)
yy  = mylist[:,1][6].astype(np.float)
dxx= mylist[:,3][7].astype(np.float) 

xaxis=[0.77,0.81,0.85,0.89,0.93]

plt.figure(dpi=150,figsize=(5,5.2))
plt.errorbar(x, y,xerr=dx,fmt='o',lw=1.25,ms=3.5,marker='o',color='black')
#plt.errorbar(xx, yy,xerr=dxx,fmt='o',lw=1.25,ms=3.5,marker='o',color='red')
plt.yticks(y, labels, rotation='horizontal',fontsize=8)
plt.xticks(xaxis, xaxis, rotation='horizontal')
plt.xlabel('Radius [fm]')
plt.xlim(0.76,0.94)
plt.plot([0.875,0.875],[1.5,43.5],'-',color='grey',lw=18,zorder=1,label='CODATA-2014')
plt.annotate('CODATA-2014',xy=(0.855,45),color='black')
plt.plot([0.84087,0.84087],[0.5,44.5],'-',color='black',lw=1,zorder=1,label='$\mu H$')
#plt.plot([0.875,0.875],[0,30.5],'-',color='black',lw=2,zorder=1,label='$\mu H$')
plt.annotate('$\mu$H',xy=(0.8345,45))
plt.tight_layout()
plt.savefig('ScatteringResults.png')
plt.savefig('ScatteringResults.pdf')
plt.show()
