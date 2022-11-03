#Ref: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
from scipy.stats import mannwhitneyu
import re

ONE_TAILED = True
LESS_IS_BETTER = False

#Cost
#input_a = ["Cost_A_0_01.txt","Cost_A_0_1.txt","Cost_A_0_2.txt","Cost_A_0_3.txt","Cost_A_0_4.txt","Cost_A_0_5.txt","Cost_A_0_6.txt","Cost_A_0_7.txt","Cost_A_0_8.txt","Cost_A_0_9.txt"]
#input_b = ["Cost_B_Q1.txt","Cost_B_Q2.txt","Cost_B_Q3.txt"]

#Jaccard Index
input_a = ["Jac_Arch.txt"]
input_b = ["Jac_Neu.txt"]

#TDS
#input_a = ["TDS_A_0_01.txt","TDS_A_0_1.txt","TDS_A_0_2.txt","TDS_A_0_3.txt","TDS_A_0_4.txt","TDS_A_0_5.txt","TDS_A_0_6.txt","TDS_A_0_7.txt","TDS_A_0_8.txt","TDS_A_0_9.txt"]
#input_b = ["TDS_B_Q1.txt","TDS_B_Q2.txt","TDS_B_Q3.txt"]

for m in input_a:
    f = open(m,"r", encoding='utf-8')
    lines = f.readlines()

    #Dictionary Creator
    data1 = []
    for i in range(0,len(lines)):
        text_ = re.sub("\n", " ", lines[i])
        data1.append(float(text_))
    
    for n in input_b:
        f = open(n,"r", encoding='utf-8')
        lines = f.readlines()

        #Dictionary Creator
        data2 = []
        for i in range(0,len(lines)):
            text_ = re.sub("\n", " ", lines[i])
            data2.append(float(text_))
        
        if ONE_TAILED == True:
            if LESS_IS_BETTER == False:
                stat, p = mannwhitneyu(data1, data2, alternative = 'greater')
                print(m+" v. "+n)
                print('stat=%.3f, p=%.3f' % (stat, p))
                if p > 0.05:
                    print('Probably the same (not greater/not less than) distribution')
                else:
                    print('Probably X is a greater distribution')
            else:
                stat, p = mannwhitneyu(data1, data2, alternative='less')        
                print(m+" v. "+n)
                print('stat=%.3f, p=%.3f' % (stat, p))
                if p > 0.05:
                    print('Probably the same (not greater/not less than) distribution')
                else:
                    print('Probably X is a lesser distribution')
        else:
            stat, p = mannwhitneyu(data1, data2, alternative='two-sided')        
            print(m+" v. "+n)
            print('stat=%.3f, p=%.3f' % (stat, p))
            if p > 0.05:
                print('Probably the same (not greater/not less than) distribution')
            else:
                print('Probably the different (greater/less than) distribution')

