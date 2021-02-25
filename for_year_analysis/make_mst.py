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
def get_graph_corr(month):
    raw_data = pd.read_csv('cleaned_data.csv',index_col=0)
    one_month = raw_data[raw_data['month']==month]
    pivot_m = pd.pivot_table(data=one_month,values='return',columns='简称',index='日期')
    corr=pivot_m.corr()
    # corr = np.abs(corr)
    # print(corr)
    zipped = []
    for i in range(len(corr.columns)):
        zipped.append(list(zip([corr.columns[i]]*corr.shape[0],corr.index,corr[corr.columns[i]])))
    List_flat = []
    for i in zipped:
        for j in i:
            if not np.isnan(j[2]):
                List_flat.append(j)
    s_List_flat = list(set(List_flat))
    List = []
    for i in range(len(s_List_flat)):
        # print(s_List_flat[i])
        if int(s_List_flat[i][2])!=1:
            List.append(s_List_flat[i])
    # print(List)
    G = nx.Graph()
    node_list = list([x for x,y,z in s_List_flat])
    for i in range(len(node_list)):
        if one_month[one_month['简称']==node_list[i]].iloc[0]['subsector'] == '资本市场服务':
            G.add_node(node_list[i],color ='yellow')
        elif one_month[one_month['简称']==node_list[i]].iloc[0]['subsector'] == '保险业':
            G.add_node(node_list[i],color ='blue')
        elif one_month[one_month['简称']==node_list[i]].iloc[0]['subsector'] == '货币金融':
            G.add_node(node_list[i],color ='red')
        elif one_month[one_month['简称']==node_list[i]].iloc[0]['subsector'] == '其他金融业':
            G.add_node(node_list[i],color ='green')
    G.add_weighted_edges_from(List)

    return G


# %%
def get_graph_distance(month):
    raw_data = pd.read_csv('cleaned_data.csv',index_col=0)
    one_month = raw_data[raw_data['month']==month]
    pivot_m = pd.pivot_table(data=one_month,values='return',columns='简称',index='日期')
    corr=pivot_m.corr()
    distance_m = np.sqrt(2*(1-corr))
    # print(distance_m)
    zipped = []
    for i in range(len(distance_m.columns)):
        zipped.append(list(zip([distance_m.columns[i]]*distance_m.shape[0],distance_m.index,distance_m[distance_m.columns[i]])))
    List_flat = []
    for i in zipped:
        for j in i:
            if not np.isnan(j[2]):
                List_flat.append(j)
    s_List_flat = list(set(List_flat))
    List = []
    for i in range(len(s_List_flat)):
        # print(s_List_flat[i])
        if int(s_List_flat[i][2])!=0:
            List.append(s_List_flat[i])
    G = nx.Graph()
    node_list = list([x for x,y,z in s_List_flat])
    for i in range(len(node_list)):
        G.add_node(node_list[i])
    G.add_weighted_edges_from(List)
    return G

# def get_graph_distance(month):
#     raw_data = pd.read_csv('cleaned_data.csv',index_col=0)
#     one_month = raw_data[raw_data['month']==month]
#     pivot_m = pd.pivot_table(data=one_month,values='return',columns='简称',index='日期')
#     corr=pivot_m.corr()
#     distance_m = np.sqrt(2*(1-corr))
#     # print(distance_m)
#     # 获取edges 信息
#     zipped = []
#     for i in range(len(distance_m.columns)):
#         zipped.append(list(zip([distance_m.columns[i]]*distance_m.shape[0],distance_m.index,distance_m[distance_m.columns[i]])))
#     List_flat = []
#     for i in zipped:
#         for j in i:
#             if not np.isnan(j[2]):
#                 List_flat.append(j)
#     # 取出重复处理
#     s_List_flat = list(set(List_flat))
#     List = []
#     for i in range(len(s_List_flat)):
#         # print(s_List_flat[i])
#         # 去除自连边
#         if int(s_List_flat[i][2])!=0:
#             List.append(s_List_flat[i])
#     G = nx.Graph()
 #   # 获取node信息
    # node_list = list([x for x,y,z in s_List_flat])
    # # 将node和颜色相互映射上
    # for i in range(len(node_list)):
    #     if one_month[one_month['简称']==node_list[i]].iloc[0]['subsector'] == '资本市场服务':
    #         G.add_node(node_list[i],color ='yellow')
    #     elif one_month[one_month['简称']==node_list[i]].iloc[0]['subsector'] == '保险业':
    #         G.add_node(node_list[i],color ='blue')
    #     elif one_month[one_month['简称']==node_list[i]].iloc[0]['subsector'] == '货币金融':
    #         G.add_node(node_list[i],color ='red')
    #     elif one_month[one_month['简称']==node_list[i]].iloc[0]['subsector'] == '其他金融业':
    #         G.add_node(node_list[i],color ='green')
    # G.add_weighted_edges_from(List)
    # return G
#%%
# def get_mst(G):
#     mst = nx.minimum_spanning_tree(G=G)
#     plt.figure(figsize=(20,20))
    
#     plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
#     nx.draw_spring(mst,with_labels=True,)
#     plt.show()
#     # plt.close()
#     return mst


# %%
def main(month):
    G = get_graph_distance(month)
    # get_mst(G)


# %%
if __name__=='__main__':
    main('2010-11')


# %%



