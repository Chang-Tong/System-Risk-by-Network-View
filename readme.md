# 货币金融业的稳定是金融业保持稳定的关键吗？

## 一个网络的视角

#### **问题提出**

在传统视角看来，金融业在整个经济稳定中起到关键作用，而作为金融行业子行业的银行业在金融业是重中之重。但是随着国内证券市场的发展，这个观点是否还可卡片，在金融行业是否和传统观点银行业为主导影响整个金融业发展一致？

#### **数据来源**

##### **金融业**

本文使用的金融行业数据来自于wind，2010年初至2020年底的金融行业股票数据，依照证监会行业分类，讲金融行业分为保险业，资本市场服务业、货币金融业以及其他金融业，截止到2020年底一共有123家企业在其目录下，其中其他金融业21家，保险业7家，资本市场服务业56家，货币金融业39家。

##### **整个市场**

本文使用的金融行业数据来自于wind，2010年初至2020年底的所有行业分类数据，依照证监会行业分类。

（note：本部分还待补充）

#### **研究方法**

##### **全行业网络构建方法**

本文首先探究金融行业在过去十年中对证券市场影响力的变化，依照证监会行业分类，讲股票所在行业分为种行业，本文将每个行业的每支股票跟另一个行业的每一支股票的相关系数再乘上他们各自的权重，变成行业之间的相关系数，这样做的好处是将其结果计算介于 -1与1之间，并且能够有效降低网络中的节点个数，减轻算力负担。

<img src="http://latex.codecogs.com/gif.latex?\rho_{IJ}=\sum_{i=1}^{n}\sum_{j=1}^{m} w_iw_j\rho_{ij}"/>

其中：

<img src="http://latex.codecogs.com/gif.latex?\rho_{ij}=corr(i,j)=\frac{cov(i,j)}{\sqrt{Var(i)Var(j)}}"/>

再将相关系数转化成网络节点之间的距离，公式如下：

<img src="http://latex.codecogs.com/gif.latex?D_{ij}=\sqrt{2(1-\rho_{ij})}" />

得到一个全联接的regular network，随后在此基础上构建$PMFG$进行简化。

之所以使用$PMFG$构建网络，而不使用$MST$构建网络，是因为$PMFG$能够保留更多的信息，其构建出来的子图更有代表性。$PMFG$所留下来的边的数量为$3(n-2)$，而$MST$所剩余的边的数量为$(n-1)$条。

（note：本部分还待补充）

##### **金融行业网络构建方法**

与全行业网络构建的方法类似，主要的区别在于金融行业网络的构建后，其节点不是行业，而是金融企业的股票。也正是因为如此，其构建不需要计算权重。

直接依照以下公式计算相关系数即可。

<img src="http://latex.codecogs.com/gif.latex?\rho_{ij}=corr(i,j)=\frac{cov(i,j)}{\sqrt{Var(i)Var(j)}}"/>

再将相关系数转化成网络节点之间的距离，公式如下：

<img src="http://latex.codecogs.com/gif.latex?D_{ij}=\sqrt{2(1-\rho_{ij})}"/>

得到一个全联接的regular network，随后在此基础上构建$PMFG$进行简化。

得到PMFG的如下图所示：

![PMFG in 202012](https://i.loli.net/2021/02/18/BK9LOVtkTic2QPI.png)

![betweenness](https://i.loli.net/2021/02/19/MGIKOw5gmYsSjuR.png)

![Degree](https://i.loli.net/2021/02/19/ydUiXrptOjImEk5.png)

以2020年12月为例，关键节点都为货币金融业和资本市场服务业。

#### **目前研究结论**

##### **金融稳定性不断增加**

![image-20210219030400557](https://i.loli.net/2021/02/19/D6WCJNxaZiRYtMo.png)

在只减少一个子行业节点的情形下，巨片节点个数占据初始网络节点个数的比例呈现不断上升的趋势，但是所有子行业在被去除一个子节点的情形下，都在2014年与2015年间出现了明显的波动。这与2014年与2015年间的股市整体上升和股灾反应一致。

同时，本文也依照网络中熵的定义，对2010年至2020年的熵进行了计算，同样展现出内地金融市场逐渐稳定成熟的趋势。

<img src="https://i.loli.net/2021/02/19/6B4CSYLsqvxQw73.png" alt="image-20210219034245734" style="zoom:30%;" />

##### **保险业的影响趋于稳定**

![image-20210219031545186](https://i.loli.net/2021/02/19/jiWLGd9UpnKzotD.png)

![image-20210219031603163](https://i.loli.net/2021/02/19/w6G1B9LXpANqlVJ.png)

 在去除3个节点后，保险业对金融业整体的影响仍然保持稳定，其趋势和其他金融业的影响区别不大，而此时货币金融业和资本市场服务业的对金融市场的影响明显开始分化。

##### **资本市场服务对金融行业稳定性最大**

传统观点看来，我国是以间接融资为主要渠道，自然而言货币金融业（主要指银行业）的影响是最大的，但是这仅仅涉及到金融业影响传统行业的渠道，没有探究这几个子行业的影响力在金融业内部是如何分配的。本文使用以度为依据的target attack进行去除固定数量节点，发现资本市场服务节点受攻击后，金融行业的稳定性受影响程度最大，其次为货币金融业，而保险业由于节点数量比较低，呈现较平稳的影响。

<img src="https://i.loli.net/2021/02/19/P9pbZIyJsdYhoxM.png" alt="image-20210219035031432" style="zoom:50%;" />

本文一去除14个节点为例，可以发现资本市场服务子行业中节点遭受攻击后，其巨片所包含的节点数量下降得更快，其巨片节点数量占比区间也小于货币金融子行业。

但是由于货币金融行业和资本市场服务行业中上市公司数量有较大区别，所以本文引入固定比例去除节点，发现此趋势仍然可靠。

<img src="https://i.loli.net/2021/02/19/ezOLDhbcXpkqSRg.png" alt="image-20210219040443757" style="zoom:50%;" />

但是本文发现，去除如此大比例的节点不仅不符合实际，而且也遗漏了网络发生破裂的关键信息，所以本文将节点去除比例缩小到10%以内，而且以2%为步长。

可以看出资本市场服务和货币金融对金融行业的冲击力在2%的固定百分比水平上在2019年就开始出现了分化。

![image-20210219040900648](https://i.loli.net/2021/02/19/ZqNX75C1Grk6luy.png)

而在6%的水平上，这种分化出现的更早，大约在2015年左右出现分化。

![image-20210219041044963](https://i.loli.net/2021/02/19/2ZfxJP1EliFS53k.png)

相同的，这种分化的提前，也出现在8%的水平上，大约在2011年就开始分化。

![image-20210219041124305](https://i.loli.net/2021/02/19/DEnIekL4btJCrcy.png)

更直观的，将货币金融业节点去除后巨片节点数量占比和资本市场服务业节点去除后巨片节点数量占比直接对比，得到下图：

<img src="https://i.loli.net/2021/02/19/NF94HP2GtoOqSQ6.png" alt="pk" style="zoom:50%;" />

<img src="https://i.loli.net/2021/02/19/BZEO4mLqyeXaHCA.png" alt="pk_p" style="zoom:50%;" />

可以看出随着节点数量去除的增加，不论是去除相同节点数量([1,15])还是去除相同比例([0.01,0.02,0.04,0.06,0.08,0.09])的节点，货币金融所能留下的巨片大小更大，再次说明资本市场服务在影响金融行业稳定所拥有的影响力更大。

#### 结论

本文发现，和常见看法不通，在现在的金融市场，资本市场服务需要得到更多关注。其重要性的不断提升也见证中国资本市场的不断发展和成熟。

