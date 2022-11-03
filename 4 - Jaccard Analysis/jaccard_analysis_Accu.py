import pandas as pd

def jaccard(list_a, list_b):
    len_intersect = len(set(list_a).intersection(set(list_b)))
    len_union = len(set(list_a).union(set(list_b)))
    return len_intersect/len_union

df = pd.read_csv('target_Accu.csv')

key_column = 'creationDate'
filter = df.groupby(key_column).filter(lambda x: len(x) > 1) 
unique_list = filter[key_column].unique()

functionality_weight_list = list()
architecture_weight_list = list()
neutral_weight_list = list()

def weightAdjustment(score):
    #Example:
    #u_list = [50,20,30,10,80]
    #w_list_A = [0.2,0.2,0.2,0.2,0.2]
    #w_list_B = [0.2,0.2,0.1,0.1,0.4]
    #w_list_C = weightAdjustment(u_list)
    #print(score)
    score = [int(x) for x in score]
    #print(score)
    sum_score = sum(score)
    res = list()
    for i in range(0,len(score)):
        if sum_score > 0:
            res.append(score[i]/sum_score)
        else:
            res.append(0)
    return res

for i in unique_list:
    id = filter.groupby(key_column).get_group(i)['component'].tolist()
    functionality_weight_list.append(filter.groupby(key_column).get_group(i)['Functional Weighting'].tolist())
    architecture_weight_list.append(filter.groupby(key_column).get_group(i)['Architectural Weighting'].tolist())
    neutral_weight_list.append(filter.groupby(key_column).get_group(i)['Neutral Weighting'].tolist())

functionality_weight_list_adjust = list()
architecture_weight_list_adjust = list()
neutral_weight_list_adjust = list()

for i in functionality_weight_list:
    functionality_weight_list_adjust.append(weightAdjustment(i))

for i in architecture_weight_list:
    architecture_weight_list_adjust.append(weightAdjustment(i))

for i in neutral_weight_list:
    neutral_weight_list_adjust.append(weightAdjustment(i))

column_names = ['functionality','architecture','neutral']
zipped = list(zip(functionality_weight_list_adjust,architecture_weight_list_adjust,neutral_weight_list_adjust))

write = pd.DataFrame(zipped,columns = column_names)
write.to_csv('weight_list_Accu.csv', index = False, sep=';', encoding='utf-8')

Jac_Func_Arch = list()
Jac_Func_Neutral = list()

for i in range(0,len(functionality_weight_list_adjust)):
    Jac_Func_Arch.append(jaccard(functionality_weight_list_adjust[i],architecture_weight_list_adjust[i]))
    Jac_Func_Neutral.append(jaccard(functionality_weight_list_adjust[i],neutral_weight_list_adjust[i]))

column_names = ['Jac_Func_Arch','Jac_Func_Neutral']
zipped = list(zip(Jac_Func_Arch,Jac_Func_Neutral))

write = pd.DataFrame(zipped,columns = column_names)
write.to_csv('Jac_list_Accu.csv', index = False, sep=';', encoding='utf-8')