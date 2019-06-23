
import os
import csv


budget_csv = os.path.join("budget_data.csv")
results_txt= os.path.join("results.txt")

money=[]
dinero=[]
money_change=[]
months=[]


with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    for row in csvreader:
    	months.append(row[0])
    	dinero=float(row[1])
    	money.append(dinero)
    	for i in range(1,len(money)):
    		money_change.append(money[i] - money[i-1])
    		average_change = sum(money_change)/len(money_change)
    		maximo = max(money_change)
    		minimo =min(money_change)


    print("Financial analysis")
    print("------------------")
    
    #The total number of months
    def countmotnths(list):
    	return(len(months))

    #The net total amount of Profit/Losses
    def sumprofit(list):
    	return round(sum(money))

    #The average of changes in Profit/Losses
    def averagechange(list):
    	
    	return average_change

    #The greatest increase in profits
    def maxchange(list):
    	return round(maximo)

    #The greatest decrease
    def minchange(list):
    	return round(minimo)
         

    print(f'Total Months: {countmotnths(list)}')
    print(f'Total: ${sumprofit(list)}')
    print(f'Average change: ${averagechange(list)}')
    print(f'Greatest Increase in Profits: (${maxchange(list)})')
    print(f'Greatest Decrease in Profits: (${minchange(list)})')


f = open(results_txt,'w+')

f.write(f"Financial Analysis\n------------------\n")
f.write(f"Total Months: {countmotnths(list)}\n")
f.write(f"Total: ${sumprofit(list)}\n")
f.write(f"Average change: ${averagechange(list)}\n")
f.write(f"Greatest Increase in Profits: (${maxchange(list)})\n")
f.write(f"Greatest Decrease in Profits: (${minchange(list)})\n")

f.close()
