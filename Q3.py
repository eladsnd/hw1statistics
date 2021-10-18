import pandas as pd
path = "C:\\Users\\tom_b\Desktop\\University\סטטיסטיקה למדעי המחשב\מטלות\hw1statistics\\appendicitis.csv"
df = pd.read_csv(path)
def Q3_A():
    is_false_positive = df['Pathology'] == 2
    only_false_positive = df[is_false_positive]
    only_false_positive_size = only_false_positive.shape[0]
    total_size = df.shape[0]
    return only_false_positive_size/total_size
def Q3_B():
   groups = df.groupby(['Sex','Pathology']).groups
   freq_dict = {k: v.size for k, v in groups.items()}

   freq_table = pd.DataFrame.from_dict(freq_dict,'index',columns=['size'])
   freq_table.reset_index(level=0, inplace=True)
   return freq_table.rename(columns={"index" : "group","size" : "size"})



if __name__ == '__main__':
 Q3_B()


