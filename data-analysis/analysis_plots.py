# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import yaml
import pandas as pd
import numpy as np

file = "analysis_results.yaml"

with open(file, "r") as stream:
    res = yaml.safe_load(stream)
    
#%% plot all setups
cores = [i for i in range(1,len(res['worker5c2e1a'])+1)]
plt.plot(cores, res['worker5c2e1a'], '-o', label='setup 0')
cores = [i for i in range(1,len(res['worker3c3e1a'])+1)]
plt.plot(cores, res['worker3c3e1a'], '-o', label='setup 1')
cores = [i for i in range(1,len(res['worker3c3e15a'])+1)]
plt.plot(cores, res['worker3c3e15a'], '-o', label='setup 2')
plt.ylim(0,18)
plt.legend()
plt.xlabel('Number of cores')
plt.ylabel('Time of Analysis in s')

#%% plot the sngle setups

#cores = [i for i in range(1,11)]
#plt.plot(cores, [np.mean(np.array(res['w5c2e10a10'])[:,i]) for i in range(10)], '-o', label='setup 0')
#cores = [i for i in range(1,10)]
#plt.plot(cores, [np.mean(np.array(res['w3c3e10a10'])[:,i]) for i in range(9)], '-o', label='setup 1')
cores = [i for i in range(1,10)]
[plt.plot(cores, np.array(res['w3c3e15a10'])[i] , '-o') for i in range(9)]
plt.ylim(0,18)
plt.legend()
plt.xlabel('Number of cores')
plt.ylabel('Time of Analysis in s')