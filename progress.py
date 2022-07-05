#showing progress through bar chart
import matplotlib.pyplot as plt

left_coordinates=[1,2,3,4,5]
heights=[5,60,50,75,100]
bar_labels=['Deployment','Coding','Design ','Analysis','Documentation']
plt.bar(left_coordinates,heights,tick_label=bar_labels,width=0.8,color=['blue','Brown'])
plt.xlabel('Tasks Progress ')
plt.ylabel('Percentage Done')
plt.title("Medaresha Project Progress")
plt.show()
