# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:15:31 2019

@author: Lorenzo-Lu 
University of Wisconsin-Madison
"""
def parameter_x(Q,name):
    import math
    pi = 3.1415926
    dic = {
"H"	:	[	0.489918	,	20.6593	,	0.262003	,	7.74039	,	0.196767	,	49.5519	,	0.049879	,	2.20159	,	0.001305	],
"He"	:	[	0.8734	,	9.1037	,	0.6309	,	3.3568	,	0.3112	,	22.9276	,	0.178	,	0.9821	,	0.0064	],
"Li"	:	[	1.1282	,	3.9546	,	0.7508	,	1.0524	,	0.6175	,	85.3905	,	0.4653	,	168.261	,	0.0377	],
"Be"	:	[	1.5919	,	43.6427	,	1.1278	,	1.8623	,	0.5391	,	103.483	,	0.7029	,	0.542	,	0.0385	],
"B"	:	[	2.0545	,	23.2185	,	1.3326	,	1.021	,	1.0979	,	60.3498	,	0.7068	,	0.1403	,	-0.1932	],
"C"	:	[	2.31	,	20.8439	,	1.02	,	10.2075	,	1.5886	,	0.5687	,	0.865	,	51.6512	,	0.2156	],
"N"	:	[	12.2126	,	0.0057	,	3.1322	,	9.8933	,	2.0125	,	28.9975	,	1.1663	,	0.5826	,	-11.529	],
"O"	:	[	3.0485	,	13.2771	,	2.2868	,	5.7011	,	1.5463	,	0.3239	,	0.867	,	32.9089	,	0.2508	],
"F"	:	[	3.5392	,	10.2825	,	2.6412	,	4.2944	,	1.517	,	0.2615	,	1.0243	,	26.1476	,	0.2776	],
"Ne"	:	[	3.9553	,	8.4042	,	3.1125	,	3.4262	,	1.4546	,	0.2306	,	1.1251	,	21.7184	,	0.3515	],
"Na"	:	[	4.7626	,	3.285	,	3.1736	,	8.8422	,	1.2674	,	0.3136	,	1.1128	,	129.424	,	0.676	],
"Mg"	:	[	5.4204	,	2.8275	,	2.1735	,	79.2611	,	1.2269	,	0.3808	,	2.3073	,	7.1937	,	0.8584	],
"Al"	:	[	6.4202	,	3.0387	,	1.9002	,	0.7426	,	1.5936	,	31.5472	,	1.9646	,	85.0886	,	1.1151	],
"Si"	:	[	6.2915	,	2.4386	,	3.0353	,	32.3337	,	1.9891	,	0.6785	,	1.541	,	81.6937	,	1.1407	],
"P"	:	[	6.4345	,	1.9067	,	4.1791	,	27.157	,	1.78	,	0.526	,	1.4908	,	68.1645	,	1.1149	],
"S"	:	[	6.9053	,	1.4679	,	5.2034	,	22.2151	,	1.4379	,	0.2536	,	1.5863	,	56.172	,	0.8669	],
"Cl"	:	[	11.4604	,	0.0104	,	7.1964	,	1.1662	,	6.2556	,	18.5194	,	1.6455	,	47.7784	,	-9.5574	],
"Ar"	:	[	7.4845	,	0.9072	,	6.7723	,	14.8407	,	0.6539	,	43.8983	,	1.6442	,	33.3929	,	1.4445	],
"K"	:	[	8.2186	,	12.7949	,	7.4398	,	0.7748	,	1.0519	,	213.187	,	0.8659	,	41.6841	,	1.4228	],
"Ca"	:	[	8.6266	,	10.4421	,	7.3873	,	0.6599	,	1.5899	,	85.7484	,	1.0211	,	178.437	,	1.3751	],
"Sc"	:	[	9.189	,	9.0213	,	7.3679	,	0.5729	,	1.6409	,	136.108	,	1.468	,	51.3531	,	1.3329	],
"Ti"	:	[	9.7595	,	7.8508	,	7.3558	,	0.5	,	1.6991	,	35.6338	,	1.9021	,	116.105	,	1.2807	],
"V"	:	[	10.2971	,	6.8657	,	7.3511	,	0.4385	,	2.0703	,	26.8938	,	2.0571	,	102.478	,	1.2199	],
"Cr"	:	[	10.6406	,	6.1038	,	7.3537	,	0.392	,	3.324	,	20.2626	,	1.4922	,	98.7399	,	1.1832	],
"Mn"	:	[	11.2819	,	5.3409	,	7.3573	,	0.3432	,	3.0193	,	17.8674	,	2.2441	,	83.7543	,	1.0896	],
"Fe"	:	[	11.7695	,	4.7611	,	7.3573	,	0.3072	,	3.5222	,	15.3535	,	2.3045	,	76.8805	,	1.0369	],
"Co"	:	[	12.2841	,	4.2791	,	7.3409	,	0.2784	,	4.0034	,	13.5359	,	2.3488	,	71.1692	,	1.0118	],
"Ni"	:	[	12.8376	,	3.8785	,	7.292	,	0.2565	,	4.4438	,	12.1763	,	2.38	,	66.3421	,	1.0341	],
"Cu"	:	[	13.338	,	3.5828	,	7.1676	,	0.247	,	5.6158	,	11.3966	,	1.6735	,	64.8126	,	1.191	],
"Zn"	:	[	14.0743	,	3.2655	,	7.0318	,	0.2333	,	5.1652	,	10.3163	,	2.41	,	58.7097	,	1.3041	],
"Ga"	:	[	15.2354	,	3.0669	,	6.7006	,	0.2412	,	4.3591	,	10.7805	,	2.9623	,	61.4135	,	1.7189	],
"Ge"	:	[	16.0816	,	2.8509	,	6.3747	,	0.2516	,	3.7068	,	11.4468	,	3.683	,	54.7625	,	2.1313	],
"As"	:	[	16.6723	,	2.6345	,	6.0701	,	0.2647	,	3.4313	,	12.9479	,	4.2779	,	47.7972	,	2.531	],
"Se"	:	[	17.0006	,	2.4098	,	5.8196	,	0.2726	,	3.9731	,	15.2372	,	4.3543	,	43.8163	,	2.8409	],
"Br"	:	[	17.1789	,	2.1723	,	5.2358	,	16.5796	,	5.6377	,	0.2609	,	3.9851	,	41.4328	,	2.9557	],
"Kr"	:	[	17.3555	,	1.9384	,	6.7286	,	16.5623	,	5.5493	,	0.2261	,	3.5375	,	39.3972	,	2.825	],
"Rb"	:	[	17.1784	,	1.7888	,	9.6435	,	17.3151	,	5.1399	,	0.2748	,	1.5292	,	164.934	,	3.4873	],
"Sr"	:	[	17.5663	,	1.5564	,	9.8184	,	14.0988	,	5.422	,	0.1664	,	2.6694	,	132.376	,	2.5064	],
"Y"	:	[	17.776	,	1.4029	,	10.2946	,	12.8006	,	5.72629	,	0.125599	,	3.26588	,	104.354	,	1.91213	],
"Zr"	:	[	17.8765	,	1.27618	,	10.948	,	11.916	,	5.41732	,	0.117622	,	3.65721	,	87.6627	,	2.06929	],
"Nb"	:	[	17.6142	,	1.18865	,	12.0144	,	11.766	,	4.04183	,	0.204785	,	3.53346	,	69.7957	,	3.75591	],
"Mo"	:	[	3.7025	,	0.2772	,	17.2356	,	1.0958	,	12.8876	,	11.004	,	3.7429	,	61.6584	,	4.3875	],
"Tc"	:	[	19.1301	,	0.864132	,	11.0948	,	8.14487	,	4.64901	,	21.5707	,	2.71263	,	86.8472	,	5.40428	],
"Ru"	:	[	19.2674	,	0.80852	,	12.9182	,	8.43467	,	4.86337	,	24.7997	,	1.56756	,	94.2928	,	5.37874	],
"Rh"	:	[	19.2957	,	0.751536	,	14.3501	,	8.21758	,	4.73425	,	25.8749	,	1.28918	,	98.6062	,	5.328	],
"Pd"	:	[	19.3319	,	0.698655	,	15.5017	,	7.98929	,	5.29537	,	25.2052	,	0.605844	,	76.8986	,	5.26593	],
"Ag"	:	[	19.2808	,	0.6446	,	16.6885	,	7.4726	,	4.8045	,	24.6605	,	1.0463	,	99.8156	,	5.179	],
"Cd"	:	[	19.2214	,	0.5946	,	17.6444	,	6.9089	,	4.461	,	24.7008	,	1.6029	,	87.4825	,	5.0694	],
"In"	:	[	19.1624	,	0.5476	,	18.5596	,	6.3776	,	4.2948	,	25.8499	,	2.0396	,	92.8029	,	4.9391	],
"Sn"	:	[	19.1889	,	5.8303	,	19.1005	,	0.5031	,	4.4585	,	26.8909	,	2.4663	,	83.9571	,	4.7821	],
"Sb"	:	[	19.6418	,	5.3034	,	19.0455	,	0.4607	,	5.0371	,	27.9074	,	2.6827	,	75.2825	,	4.5909	],
"Te"	:	[	19.9644	,	4.81742	,	19.0138	,	0.420885	,	6.14487	,	28.5284	,	2.5239	,	70.8403	,	4.352	],
"I"	:	[	20.1472	,	4.347	,	18.9949	,	0.3814	,	7.5138	,	27.766	,	2.2735	,	66.8776	,	4.0712	],
"Xe"	:	[	20.2933	,	3.9282	,	19.0298	,	0.344	,	8.9767	,	26.4659	,	1.99	,	64.2658	,	3.7118	],
"Cs"	:	[	20.3892	,	3.569	,	19.1062	,	0.3107	,	10.662	,	24.3879	,	1.4953	,	213.904	,	3.3352	],
"Ba"	:	[	20.3361	,	3.216	,	19.297	,	0.2756	,	10.888	,	20.2073	,	2.6959	,	167.202	,	2.7731	],
"La"	:	[	20.578	,	2.94817	,	19.599	,	0.244475	,	11.3727	,	18.7726	,	3.28719	,	133.124	,	2.14678	],
"Ce"	:	[	21.1671	,	2.81219	,	19.7695	,	0.226836	,	11.8513	,	17.6083	,	3.33049	,	127.113	,	1.86264	],
"Pr"	:	[	22.044	,	2.77393	,	19.6697	,	0.222087	,	12.3856	,	16.7669	,	2.82428	,	143.644	,	2.0583	],
"Nd"	:	[	22.6845	,	2.66248	,	19.6847	,	0.210628	,	12.774	,	15.885	,	2.85137	,	137.903	,	1.98486	],
"Pm"	:	[	23.3405	,	2.5627	,	19.6095	,	0.202088	,	13.1235	,	15.1009	,	2.87516	,	132.721	,	2.02876	],
"Sm"	:	[	24.0042	,	2.47274	,	19.4258	,	0.196451	,	13.4396	,	14.3996	,	2.89604	,	128.007	,	2.20963	],
"Eu"	:	[	24.6274	,	2.3879	,	19.0886	,	0.1942	,	13.7603	,	13.7546	,	2.9227	,	123.174	,	2.5745	],
"Gd"	:	[	25.0709	,	2.25341	,	19.0798	,	0.181951	,	13.8518	,	12.9331	,	3.54545	,	101.398	,	2.4196	],
"Tb"	:	[	25.8976	,	2.24256	,	18.2185	,	0.196143	,	14.3167	,	12.6648	,	2.95354	,	115.362	,	3.58024	],
"Dy"	:	[	26.507	,	2.1802	,	17.6383	,	0.202172	,	14.5596	,	12.1899	,	2.96577	,	111.874	,	4.29728	],
"Ho"	:	[	26.9049	,	2.07051	,	17.294	,	0.19794	,	14.5583	,	11.4407	,	3.63837	,	92.6566	,	4.56796	],
"Er"	:	[	27.6563	,	2.07356	,	16.4285	,	0.223545	,	14.9779	,	11.3604	,	2.98233	,	105.703	,	5.92046	],
"Tm"	:	[	28.1819	,	2.02859	,	15.8851	,	0.238849	,	15.1542	,	10.9975	,	2.98706	,	102.961	,	6.75621	],
"Yb"	:	[	28.6641	,	1.9889	,	15.4345	,	0.257119	,	15.3087	,	10.6647	,	2.98963	,	100.417	,	7.56672	],
"Lu"	:	[	28.9476	,	1.90182	,	15.2208	,	9.98519	,	15.1	,	0.261033	,	3.71601	,	84.3298	,	7.97628	],
"Hf"	:	[	29.144	,	1.83262	,	15.1726	,	9.5999	,	14.7586	,	0.275116	,	4.30013	,	72.029	,	8.58154	],
"Ta"	:	[	29.2024	,	1.77333	,	15.2293	,	9.37046	,	14.5135	,	0.295977	,	4.76492	,	63.3644	,	9.24354	],
"W"	:	[	29.0818	,	1.72029	,	15.43	,	9.2259	,	14.4327	,	0.321703	,	5.11982	,	57.056	,	9.8875	],
"Re"	:	[	28.7621	,	1.67191	,	15.7189	,	9.09227	,	14.5564	,	0.3505	,	5.44174	,	52.0861	,	10.472	],
"Os"	:	[	28.1894	,	1.62903	,	16.155	,	8.97948	,	14.9305	,	0.382661	,	5.67589	,	48.1647	,	11.0005	],
"Ir"	:	[	27.3049	,	1.59279	,	16.7296	,	8.86553	,	15.6115	,	0.417916	,	5.83377	,	45.0011	,	11.4722	],
"Pt"	:	[	27.0059	,	1.51293	,	17.7639	,	8.81174	,	15.7131	,	0.424593	,	5.7837	,	38.6103	,	11.6883	],
"Au"	:	[	16.8819	,	0.4611	,	18.5913	,	8.6216	,	25.5582	,	1.4826	,	5.86	,	36.3956	,	12.0658	],
"Hg"	:	[	20.6809	,	0.545	,	19.0417	,	8.4484	,	21.6575	,	1.5729	,	5.9676	,	38.3246	,	12.6089	],
"Tl"	:	[	27.5446	,	0.65515	,	19.1584	,	8.70751	,	15.538	,	1.96347	,	5.52593	,	45.8149	,	13.1746	],
"Pb"	:	[	31.0617	,	0.6902	,	13.0637	,	2.3576	,	18.442	,	8.618	,	5.9696	,	47.2579	,	13.4118	],
"Bi"	:	[	33.3689	,	0.704	,	12.951	,	2.9238	,	16.5877	,	8.7937	,	6.4622	,	48.0093	,	13.5782	],
"Po"	:	[	34.6726	,	0.700999	,	15.4733	,	3.55078	,	13.1138	,	9.55642	,	7.02588	,	47.0045	,	13.677	],
"At"	:	[	35.3163	,	0.68587	,	19.0211	,	3.97458	,	9.49887	,	11.3824	,	7.42518	,	45.4715	,	13.7108	],
"Rn"	:	[	35.5631	,	0.6631	,	21.2816	,	4.0691	,	8.0037	,	14.0422	,	7.4433	,	44.2473	,	13.6905	],
"Fr"	:	[	35.9299	,	0.646453	,	23.0547	,	4.17619	,	12.1439	,	23.1052	,	2.11253	,	150.645	,	13.7247	],
"Ra"	:	[	35.763	,	0.616341	,	22.9064	,	3.87135	,	12.4739	,	19.9887	,	3.21097	,	142.325	,	13.6211	],
"Ac"	:	[	35.6597	,	0.589092	,	23.1032	,	3.65155	,	12.5977	,	18.599	,	4.08655	,	117.02	,	13.5266	],
"Th"	:	[	35.5645	,	0.563359	,	23.4219	,	3.46204	,	12.7473	,	17.8309	,	4.80703	,	99.1722	,	13.4314	],
"Pa"	:	[	35.8847	,	0.547751	,	23.2948	,	3.41519	,	14.1891	,	16.9235	,	4.17287	,	105.251	,	13.4287	],
"U"	:	[	36.0228	,	0.5293	,	23.4128	,	3.3253	,	14.9491	,	16.0927	,	4.188	,	100.613	,	13.3966	],
"Np"	:	[	36.1874	,	0.511929	,	23.5964	,	3.25396	,	15.6402	,	15.3622	,	4.1855	,	97.4908	,	13.3573	],
"Pu"	:	[	36.5254	,	0.499384	,	23.8083	,	3.26371	,	16.7707	,	14.9455	,	3.47947	,	105.98	,	13.3812	],
"Am"	:	[	36.6706	,	0.483629	,	24.0992	,	3.20647	,	17.3415	,	14.3136	,	3.49331	,	102.273	,	13.3592	]

            }
    num_dic = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0
            }
    
    parameter_matrix = []
    element_ratio = []
    last = len(name)-1
    i = 0
    
    while i <= last:
        j = i
        #if name[i] not in num_dic and name[i] not in dic:
        #    return []
        if (i+1) <= last and (name[i:i+2]) in dic:
            parameter_matrix.append(dic[name[i:i+2]])
            i += 2
        elif name[i] in dic:
            parameter_matrix.append(dic[name[i]])
            i +=1
            
        if j == i :
            print("Wrong Formula Input")
            break
            
        ele_weight = 0
        if i <= last and name[i] in num_dic:
            ele_weight = num_dic[name[i]]
            i += 1
            while i <= last and name[i] in num_dic:
                ele_weight = ele_weight * 10 + num_dic[name[i]]
                i += 1
                if i > last:
                    break
        
            #return []
        else:
            ele_weight = 1
        
        element_ratio.append(ele_weight)
    #return (parameter_matrix,element_ratio)
    N_ele = len(element_ratio)
    ele_total = sum(element_ratio)
    for i in range(N_ele):
        element_ratio[i] = element_ratio[i] / ele_total
    
    
    L_Q = len(Q)
    f = [0] * L_Q
    f2 = [0] * L_Q
    for qi in range(L_Q):
        for ei in range(N_ele):
            X = pow((Q[qi] / 4 /pi),2)    
            S1 = math.exp(-parameter_matrix[ei][1] * X)
            S2 = math.exp(-parameter_matrix[ei][3] * X)
            S3 = math.exp(-parameter_matrix[ei][5] * X)
            S4 = math.exp(-parameter_matrix[ei][7] * X)
            cal_f = parameter_matrix[ei][0] * S1 + parameter_matrix[ei][2] * S2 + parameter_matrix[ei][4] * S3 + parameter_matrix[ei][6] * S4 + parameter_matrix[ei][8]            
            
            f[qi] += cal_f * element_ratio[ei]
            f2[qi] += pow(cal_f,2) * element_ratio[ei]
    return [f,f2]
   

# input the chemical  
#example
name = "C55H72O5N4Mg";    
#name = 'H2O';
Q = [i/100 for i in range(1000)]
factor =(parameter_x(Q,name)) 


import matplotlib.pyplot as plt
plt.plot(Q,factor[0],label = 'f') 
plt.plot(Q,factor[1],label = 'f^2')  
plt.legend()
plt.title("Form factor of %s under X-ray"%(name))
plt.xlabel("Q/(1/A)")
plt.ylabel("cts")
plt.show()
    
    
    
    
    
    
    
