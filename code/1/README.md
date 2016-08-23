# Week 1 - Explaning the eg's of Ninja

### eg0

eg0 first prints only the __attributes__ in the weather.arf dataset. It then prints all of the contents of the dataset, using the following parameters: _gawk_ to process the patterns and _-F_ to set the field separator and _"NF==5"_ to set the number of fields, _sort_ to sort the table, and _column_ _-s_ _-t_ to make a table with separators. Finally it prints a decision tree that was generated using the j48 algorithm.

### eg1

eg1 simply prints all of the contents of the weather dataset, using the same parameters as eg0.

### eg2

eg2 prints the decision tree generated from the j48 algorithm alongside various information, such as the confuson matrix and statistics like precision and recall. It also prints the same information for when the algorithm is used alongside cross-validation. With it we can clearly see that, if we use the same training dataset for testing we'll get a biased result. With cross-validation, we can get a more realistic result.

### eg3

eg3 runs the j48 algorithm on the weather dataset, using whole dataset for both training and testing. Because of that, the results are biased, producing a false _perfect_ prediction rate.

### eg4

eg4 shows that eg3 produced perfect results, when we compared the first column (output of j48) with the second (real dataset).

### eg5

eg5 prints a table where a,b,c,d are the number of true negatives, false negatives, false positives and true positives respectively, and the adjacent columns show the accuracy, recall, precision, and other statistics.

### eg6

eg6 is executing a stratified cross validation, since it's dividint the set in subgrups and randomly selecting the elements proportionally from the different groups. We can see that's the case because when an algorithm ran multiple times, it produced different results (for instance, j48 had different predictions for each of it's 3 runs, because each subgroup had different elements on eah run).

### eg7

eg7 runs j48 and jrip 5 times each, randomizing the cross validation also 5 times. It also saves the output of the prediction into an _out_ file, and also saves the recall and precision values for both learners in fies called _out.pd_ and _out.pf_ respectively.

### eg8

eg8 does the same as eg7, but instead of saving the recall and precision information using _gawk_, it uses column names to make it more readable.

### eg9

eg9 shows the recall and fall-out rates for both algorithms, and also on which percentile the values fall. The advantage of separating the report from the execution is that you can quickly see the report whenever you want, whereas the execution can take a while to finish, especially for big datasets. 

### eg10

eg10 runs 4 different algorithms, with those being j48, jrip, nb, rbfnet and bnet. It also uses a new dataset called jedit-4.1.arff, and as in eg8, it uses _gawk_ to store the precision and recall information for each algorithm. It also prints a table similar to the one in eg9, where we can see in which percentile the values for precision and recall fall for each algorithm.

j48 is actually an open source java implementation of the C4.5 algorithm, and it works by building decision trees based on the entropy of every attribute from the training set and recursively splitting the set into subsets based on the smallest entropy.

nb is the weka implementation of the naive bayes classifier, which is based on the Bayes Theorem with an assumption of independence among the features. It works by estimating the probability of a specific feature belonging to a class, and it then pics the one with the highest probability. 

