#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot
get_ipython().run_line_magic('matplotlib', 'inline')

x = np.linspace(1E-3, 2 * np.pi)

pyplot.plot(x, np.sin(x) / x)
pyplot.plot(x, np.cos(x))
pyplot.grid()

