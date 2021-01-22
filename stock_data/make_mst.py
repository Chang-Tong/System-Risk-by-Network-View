# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import time
import planarity
from networkx.algorithms import community


# %%
raw_data = pd.read_csv('cleaned_data.csv',index_col=0)
# # raw_data.columns.values
# print(raw_data['month'])


# %%
raw_data[raw_data['month']=='2018-01']


# %%
def get_graph(month,method = 'corr'):
    raw_data = pd.read_csv('cleaned_data.csv',index_col=0)
    one_month = raw_data[raw_data['month']==month]
    # print(one_month)
    pivot_m = pd.pivot_table(data=one_month,values='return',columns='简称',index='日期')
    corr=pivot_m.corr()
    if method == 'distance':
        distance_m = np.sqrt(2*(1-corr))
        zipped = []
        for i in range(len(distance_m.columns)):
            zipped.append(list(zip([distance_m.columns[i]]*distance_m.shape[0],distance_m.index,distance_m[distance_m.columns[i]])))
        List_flat = []
        for i in zipped:
            for j in i:
                # print(j)
                # print(type(j[2]))
                if not np.isnan(j[2]):
                    # print(j[2])
                    List_flat.append(j)
        s_List_flat = list(set(List_flat))
        G = nx.Graph()
        node_list = list([x for x,y,z in s_List_flat])
        for i in range(len(node_list)):
            G.add_node(node_list[i])
        G.add_weighted_edges_from(s_List_flat)
    if method == 'corr':
        zipped = []
        for i in range(len(corr.columns)):
            zipped.append(list(zip([corr.columns[i]]*corr.shape[0],corr.index,corr[corr.columns[i]])))
        List_flat = []
        for i in zipped:
            for j in i:
                # print(j)
                # print(type(j[2]))
                if not np.isnan(j[2]):
                    # print(j[2])
                    List_flat.append(j)
        s_List_flat = list(set(List_flat))
        G = nx.Graph()
        node_list = list([x for x,y,z in s_List_flat])
        for i in range(len(node_list)):
            G.add_node(node_list[i])
        G.add_weighted_edges_from(s_List_flat)
    return G


# %%
def get_mst(G):
    mst = nx.minimum_spanning_tree(G=G)
    plt.figure(figsize=(20,20))
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    nx.draw_spring(mst,with_labels=True,)
    # plt.show()
    # plt.close()
    return mst


# %%
def main(month):
    G = get_graph(month)
    mst = get_mst(G)


# %%
if __name__=='__main__':
    main('2010-11')


# %%



