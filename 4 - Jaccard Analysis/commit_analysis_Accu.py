import pandas as pd

def jaccard(list_a, list_b):
    len_intersect = len(set(list_a).intersection(set(list_b)))
    len_union = len(set(list_a).union(set(list_b)))
    return len_intersect/len_union

df = pd.read_csv('target_Accu_non_Zero.csv')

key_column = 'creationDate'
filter = df.groupby(key_column).filter(lambda x: len(x) > 1)
date_list = filter[key_column].unique()

result_list = list()

for i in date_list:
    pcEffort = df.groupby(key_column).get_group(i)['PC - Effort'].tolist() 
    weight = df.groupby(key_column).get_group(i)['Architectural Weighting'].tolist()
    res_list = [pcEffort [i] * weight[i] for i in range(len(weight))]
    result_list.append(sum(res_list))

column_names = ['Creation_Date','weightedPC-Effort']
zipped = list(zip(date_list,result_list))

write = pd.DataFrame(zipped,columns = column_names)
write.to_csv('weightedPC-Effort_list_Accu.csv', index = False, sep=';', encoding='utf-8')