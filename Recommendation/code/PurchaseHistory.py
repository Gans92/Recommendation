# -*- coding: utf-8 -*-
import datetime
import gzip
import csv

def createPurchaseHistory(fileName):
    file = open(fileName,'w', newline='')
    metaFile = open('ProductReviewMetaData_Sort.csv', 'r')
    
    mydict = dict()
    fileReader = csv.reader(metaFile, delimiter=',')
    
    for row in fileReader:
        reviewID = row[0]
        asin = row[1]
        if reviewID in mydict:
            mydict[reviewID] = mydict.get(reviewID) + ',' + asin
        else:
            mydict[reviewID] = asin
    
    writer = csv.writer(file)
    for key, value in mydict.items():
        if len(value.split(',')) > 3:
            writer.writerow([key, {value}])
            
    f = open('History.txt', 'w')
    for key, value in mydict.items():
        if len(value.split(',')) > 3:
           f.write('{0}, {1}\n'.format(key, value))
    f.close()

    metaFile.close()
    file.close()
    return 0

def productReviewData(fileName):
    unusedMeta = ['reviewerName', 'helpful', 'reviewText', 'summary', 'unixReviewTime', 'reviewTime']
	
    file = open(fileName,'w', newline='')
    g = gzip.open('reviews_Movies_and_TV.json.gz', 'r')
    count = 1;

    for l in g:
        data = eval(l)
        #delete unusedkey
        for key in unusedMeta:
            if key in data:
                del data[key]
        #set header
        if count == 1:
            fileWriter = csv.DictWriter(file, data.keys())
            fileWriter.writeheader()
            count=count+1

        fileWriter.writerow(data)
        
    file.close()
    g.close()
    file.close()    
    return 0

#productReviewData("ProductReviewMetaData.csv")
createPurchaseHistory("PurchaseHistory.csv")
