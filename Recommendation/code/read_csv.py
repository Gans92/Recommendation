# -*- coding: utf-8 -*-

import gzip
import csv
from random import randint

#read file from json.gz to csv and delete unused key 

#path file and number of data ex. 500k    
def parsecsvContent(path1, path2, path3, num):
    f = open(path1, 'wb') #content.csv file name
    a = open(path2, 'wb') #cf.csv filename
    b = open(path3, 'wb') #testing filename
    unusedKey = ['helpful', 'reviewerName', 'summary', 'unixReviewTime', 'reviewTime'] #for content based
    g = gzip.open("reviews_Movies_and_TV.json.gz", 'r') 
    count = 1
    for l in g:
        data = eval(l)
        #delete unusedkey
        for key in unusedKey:
            if key in data:
                del data[key]        
        #set header
        if count == 1:
            w = csv.DictWriter(f, data.keys()) #content
            w.writeheader()
            if('reviewText' in data):
                    del data['reviewText']
            u = csv.DictWriter(a, data.keys()) #cf
            u.writeheader()
            v = csv.DictWriter(b, data.keys()) #testing
            v.writeheader()

        count += 1
        if count == num:
            break
        #write data
        if count <= num:
            if(randint(0,9) < 2): #select 20%
                if('reviewText' in data):
                    del data['reviewText']
                v.writerow(data)
            else:
                w.writerow(data) # write to content.csv
                if('reviewText' in data):
                    del data['reviewText']
                u.writerow(data)
        
    f.close()
    a.close()
    b.close()
    return 0     
 
    
def parsecsvMeta(path):
    f = open(path, 'wb') #training set file name

    unusedMeta = ['title', 'imUrl', 'related', 'salesRank', 'brand', 'categories', 'description'] #for meta file

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
            w = csv.DictWriter(f, data.keys())
            w.writeheader()

        count += 1

        w.writerow(data)
       
    f.close()
    return 0       


numData = 600000 #total data used in project

parsecsvContent("Content500k.csv", "CF500k.csv", "Testing.csv", numData)

parsecsvMeta("MetaData.csv")


