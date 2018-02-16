# -*- coding: utf-8 -*-
import gzip
import csv
from random import randint
   
def getePurchaseHistory(training, testing, num):
	unusedMeta = ['categories', 'description', 'price', 'salesRank', 'imUrl', 'brand']
	
	testingFile = open(testing,'w', newline='')
	trainingFile = open(training, 'w', newline='')
	g = gzip.open('meta_Movies_and_TV.json.gz', 'r')
	count = 1
	
	for l in g:
		data = eval(l)
      #delete unusedkey
		for key in unusedMeta:
			if key in data:
				del data[key]
		#set header
		if count == 1:
			testWriter = csv.DictWriter(testingFile, data.keys())
			testWriter.writeheader()
			trainWriter = csv.DictWriter(trainingFile, data.keys())
			trainWriter.writeheader()
		
		count += 1
		#write data
		if count <= num:
			if(randint(0,9) < 2): #select 20%
				testWriter.writerow(data)
			else:
				trainWriter.writerow(data)
	
	trainingFile.close()
	testingFile.close()
	g.close()
	return 0     
 
    
def getProductReviews(training, testing, num):
	unusedMeta = ['reviewerName', 'helpful', 'reviewText', 'summary', 'unixReviewTime', 'reviewTime']
	
	testingFile = open(testing,'w', newline='')
	trainingFile = open(training, 'w', newline='')
	g = gzip.open('reviews_Movies_and_TV.json.gz', 'r')
	count = 1
	
	for l in g:
		data = eval(l)
      #delete unusedkey
		for key in unusedMeta:
			if key in data:
				del data[key]
		#set header
		if count == 1:
			testWriter = csv.DictWriter(testingFile, data.keys())
			testWriter.writeheader()
			trainWriter = csv.DictWriter(trainingFile, data.keys())
			trainWriter.writeheader()
		
		count += 1
		#write data
		if count <= num:
			if(randint(0,9) < 2): #select 20%
				testWriter.writerow(data)
			else:
				trainWriter.writerow(data)
	
	trainingFile.close()
	testingFile.close()
	g.close()
	return 0

def productReviewText(path):
    f = open(path, 'w', newline='')
    unusedMeta = ['title', 'imUrl', 'related', 'salesRank', 'brand', 'categories', 'description']
    g = gzip.open('meta_Movies_and_TV.json.gz', 'r') 
    count = 1
    for l in g:
        data = eval(l)
        #delete unusedkey
        for key in unusedMeta: 
            if key in data:
                del data[key]        
        #set header
        if count == 1:
            writer = csv.DictWriter(f, data.keys())
            writer.writeheader()
            
        count += 1
        writer.writerow(data)
        
    f.close()
    g.close()
    return 0       


numData = 200000 #Total data used in the project
getProductReviews("ProductReviewsTraining.csv", "ProductReviewsTesting.csv", numData)
#getePurchaseHistory("PurchaseHistoryTraining.csv", "PurchaseHistoryTesting.csv", numData)
#productReviewText("ProductReviewText.csv")

