#we will complete this very soon in this we have to find out the differency privacy for mean ,threshold,sum

pdb= get_parallel_db(db,remove_index=10)
db[10]
sum(db)

#differencing privacy using sum

sum(db)-sum(pdb)

#differencing privacy using mean function

(sum(db).float()/len(db))-(sum(pdb).float()/len(pdb))

#differencing privacy using threshold

(sum(db)>53)-(sum(pdb)>53)

#differencing privacy using threshold
#if we take greater than hte sum(db) the output will be 0

(sum(db)>55)-(sum(pdb)>55)
