from scipy.stats import shapiro
import matplotlib.pyplot as plt
import re

input = ["Cost_A_0_01.txt","Cost_A_0_1.txt","Cost_A_0_2.txt","Cost_A_0_3.txt","Cost_A_0_4.txt","Cost_A_0_5.txt","Cost_A_0_6.txt","Cost_A_0_7.txt","Cost_A_0_8.txt","Cost_A_0_9.txt","Cost_B_Q1.txt","Cost_B_Q2.txt","Cost_B_Q3.txt"]
#input = ["TDS_A_0_01.txt","TDS_A_0_1.txt","TDS_A_0_2.txt","TDS_A_0_3.txt","TDS_A_0_4.txt","TDS_A_0_5.txt","TDS_A_0_6.txt","TDS_A_0_7.txt","TDS_A_0_8.txt","TDS_A_0_9.txt","TDS_B_Q1.txt","TDS_B_Q2.txt","TDS_B_Q3.txt"]
#input = ["Jac_Arch.txt","Jac_Neu.txt"]

for m in input:
    f = open(m,"r", encoding='utf-8')
    lines = f.readlines()

    #Dictionary Creator
    data = []
    for i in range(0,len(lines)):
        text_ = re.sub("\n", " ", lines[i])
        data.append(float(text_))

    stat, p = shapiro(data)
    print('stat=%.5f, p=%.5f' % (stat, p))
    if p > 0.05:
        print('Probably Gaussian')
    else:
        print('Probably not Gaussian')

    plt.hist(data, 30, histtype='bar')
    plt.show()