import csv
import functools

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
		entry = {purpose: avIntRate}
		avResult.append(entry)
	
	print(avResult)
