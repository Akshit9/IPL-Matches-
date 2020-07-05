#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
matches=pd.read_csv(r'C:\Users\Admin\Downloads\Kaggle Datasets\deliveries.csv~\matches.csv')
matches.head(10)


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(10,8))
d1=plt.plot(matches['win_by_runs'][0:10])
d2=plt.plot(matches['win_by_wickets'][0:10])


# In[3]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(10,8))
d1=plt.plot(matches['win_by_runs'][0:10],color='g')
d2=plt.plot(matches['win_by_wickets'][0:10],color='r')


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(10,8))
d1=plt.plot(matches['win_by_runs'][0:10],linestyle='-')
d2=plt.plot(matches['win_by_wickets'][0:10],linestyle='-.')


# In[5]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12,10))
d1=plt.plot(matches['win_by_runs'][0:10],'-.m',label='win_by_runs')
d2=plt.plot(matches['win_by_wickets'][0:10],'-g',label='win_by_wickets')
plt.legend()


# In[6]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12,10))
d1=plt.plot(matches['win_by_runs'][0:10],'-.m',label='win_by_runs')
d2=plt.plot(matches['win_by_wickets'][0:10],'-g',label='win_by_wickets')
plt.legend()
plt.axis('tight')


# In[7]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12,10))
d1=plt.plot(matches['win_by_runs'][0:10],'-.m',label='win_by_runs')
d2=plt.plot(matches['win_by_wickets'][0:10],'-g',label='win_by_wickets')
plt.legend()
plt.axis('equal')


# In[8]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12,10))
d1=plt.plot(matches['win_by_runs'][0:637],'-.m',label='win_by_runs')
d2=plt.plot(matches['win_by_wickets'][0:637],'-g',label='win_by_wickets')
plt.legend()


# In[9]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12,10))
d1=plt.plot(matches['win_by_runs'][0:637],':y',label='win_by_runs')
d2=plt.plot(matches['win_by_wickets'][0:637],'-g',label='win_by_wickets')
plt.legend()


# In[10]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12,10))
d1=plt.plot(matches['win_by_runs'][0:637],'-.m',label='win_by_runs')
d2=plt.plot(matches['win_by_wickets'][0:637],'-g',label='win_by_wickets')
plt.xlabel('win_by_runs')
plt.ylabel('win_by_wickets')
plt.legend()


# In[11]:


plt.plot(matches['win_by_runs'],matches['win_by_wickets'],'o',color='black')


# In[12]:


plt.plot(matches['win_by_runs'],matches['win_by_wickets'],'d',color='blue')
plt.figure(figsize=(28,30))


# In[ ]:




