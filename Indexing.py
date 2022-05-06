import numpy as np 
import pandas as pd
exam_data  = {'name': ['Andu', 'Abay', 'Sosina', 'Ribka', 'Iyasu', 'Muse', 'Julie', 'Rama', 'Kiya', 'Blen'], 
              'score': [15.5, 9, 16.5, np.nan, 9, 30, 17.5, np.nan, 8, 20], 
              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']} 
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#CHnge our data into dataframe
Exam_dataF = pd.DataFrame(exam_data,labels)
Exam_dataF
Exam_dataF.iloc[:4]
#1 Select the columns 'score' and 'attempts' in rows 1, 3, 5, 7
Exam_dataF.iloc[[1,3,5,7],[1,2]]

#2.Count the number of rows and columns without shape attribute
Exam_dataF.axes[0]
Exam_dataF.axes[1]
print('number of row :',len(Exam_dataF.axes[0]))
print('number of columns :',len(Exam_dataF.axes[1]))
# shows boelean value of dataframe 
selection = Exam_dataF['score'].between(16,20)
selection
print(Exam_dataF[selection])

#pass the selection to method directly
print(Exam_dataF[Exam_dataF['score'].between(16,20)])

# select the rows where number of attempts in the examination is less than 2 and score greater than 16 
print(Exam_dataF)
cond = (Exam_dataF['attempts'] > 2) & (Exam_dataF['score']> 16)
print(Exam_dataF[cond])
#Change the score of rows 'C' and 'I' to 16 
Exam_dataF.loc[['C','I'],'score'] = 16
Exam_dataF
#total examination attempts
Exam_dataF['attempts'].sum()

#add new row Hagi,score 19 ,attempts 2 Qualify yes Label L
Exam_dataF.loc['L'] = ['Yohanna',19,2,'yes']
Exam_dataF
# remove the row index 'L'
Or_data = Exam_dataF.iloc[:-1,:]
Or_data
#second method
Exam_dataF.drop('L',inplace=True)
print(Exam_dataF)

#remove last 4 row
new_data = Exam_dataF.iloc[:-4]
print(new_data)
