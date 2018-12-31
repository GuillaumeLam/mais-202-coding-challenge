import csv
import functools
import matplotlib.pyplot as plt
import numpy as np

with open('data.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	
	result=[]
	
	for i, row in enumerate(reader):
		if i == 0:
			print(row)
		else:
			purpose=row[16]
			intRate=row[5]
			
			found = False
			for row in result:
				if row[0] == purpose:
					row.append(intRate)
					found = True
					# print("purpose found")
					break										
			if found:
				continue
			else:
				row=[]
				row.append(purpose)
				row.append(intRate)
				result.append(row)
				# print(purpose + " " + intRate)	
	print(result)
	print(len(result))

	avResult=[]
	for row in result:
		purpose = row[0]
		intRate = row[1:]
		print(purpose)
		print(functools.reduce(lambda x,y: float(x)+float(y), intRate))
		avIntRate = float(functools.reduce(lambda x, y: float(x)+float(y), intRate))/ len(intRate)
		entry = [purpose, avIntRate]
		avResult.append(entry)
	
	print(avResult)

	#fig, axs = plt.subplots(2,1)
	purposes=[]
	avg_rates=[]
	
	for i, row in enumerate(avResult):
		purposes.append(row[0])
		avg_rates.append(row[1])

	index = np.arange(len(purposes))
	
	print(index)
	print(purposes)
	print(avg_rates)	

	#clust_data = np.array(clust_data)

	collabel=("purpose", "avg_rate")
	#axs[0].axis('tight')
	#axs[0].axis('off')
	#the_table = axs[0].table(cellText=clust_data,colLabels=collabel,loc='center')
	#the_table = axs[0].table(celltText=clust_data, loc='center')

	#axs[1].plot(clust_data[:,1],clust_data[:,2])
	
	colors=['#FFA8BB', '#C7E9FF', '#C4FF99', '#FF85E5', '#FFE59E', '#EDFF94', '#FFC7DB', '#94FFC1', '#FE9EFF', '#FF9E85', '#A3C8FF', '#A3FFB3']	

	plt.bar(index, avg_rates, color=colors)	
	plt.xticks(index, purposes, fontsize=10, rotation=30)

	plt.show()

