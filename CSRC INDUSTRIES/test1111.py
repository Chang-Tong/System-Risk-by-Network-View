# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
import os
import time
from tqdm import tqdm


# %%
file_path = os.listdir('cleaned_data')
file_path = [x[:-4] for x in file_path]
# file_path


# %%
df = pd.read_csv('whole.csv',index_col=0)


# %%
start_time = time.time()
total_dict = {}
for j in tqdm(range(len(file_path))):
# for j in range(1):
    one_industry_index = {}
    one_industry = df[df['industry']==file_path[j]]
    days = one_industry['日期'].drop_duplicates()
    for i in range(len(days)):
        one_industry_one_day = one_industry[one_industry['日期']==days[i]]
        one_industry_one_day['weight']=one_industry_one_day['总市值(元)']/sum(one_industry_one_day['总市值(元)'])
        one_industry_one_day_index = sum(one_industry_one_day['收盘价(元)']*one_industry_one_day['weight'])
        # print(one_industry_one_day_index)
        # one_industry_index.append(one_industry_one_day_index)
        one_industry_index[days[i]]=one_industry_one_day_index
    # if j%10==0:
    #     print(one_industry_index)
    total_dict[file_path[j]] = one_industry_index
end_time = time.time()
print('time claupse: ',end_time-start_time)


# %%
# total_dict
all_index = pd.DataFrame(total_dict)


# %%
all_index.to_csv('all_year_index.csv')

# %% [markdown]
# ## year by year

