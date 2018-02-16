# -*- coding: utf-8 -*-
def readcsv(path):
    return pd.read_csv(path, iterator=True, chunksize=10000, skip_blank_lines=True)

dataChunk = readcsv("ProductReviewsTraining.csv")
data = concat(dataChunk, ignore_index=True)

#Select popular products
popularProduct = data.groupby("asin").filter(lambda x: len(x) > 100)

#create utility matrix
utilityMatrix = popularProduct.pivot_table(values='overall', index=['reviewerID'], columns=['asin'])

#normalize data
utilityMatrix = utilityMatrix.apply(lambda x: (x - np.mean(x)))

#fill emptyspace with 0
utilityMatrix = utilityMatrix.fillna(value=0)

#create table to hold result
result = pd.DataFrame(index=utilityMatrix.columns,columns=utilityMatrix.columns)


 #for each item
for i in range(0,len(result.columns)):
    #compare with another item
    for j in range(0,len(result.columns)): 
        #find cosine similarity of item1 and item2
        result.ix[i,j] = 1-spatial.distance.cosine(utilityMatrix.ix[:,i],utilityMatrix.ix[:,j])

#table to hold the similarity of item
rank = pd.DataFrame(index=result.columns,columns=range(1,11))

#rank data based on cosine similarity
for i in range(0,len(result.columns)):
    rank.ix[i,:10] = result.ix[0:,i].sort_values(ascending=False)[:10].index

#write to file
rank.to_csv('SimilarityMatrixByPopularProducts_100.csv')
