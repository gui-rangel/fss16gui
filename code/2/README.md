## Active Shooter Exercise


### List two things not to do during an active shooter event:
Don't panic.
Don't huddle together, better to spread out.

### List two things best to do during an active shooter event
Be aware of your surroundings and the nearest exits/hiding spots.
Trust you instincts and get out if you can.


## ZeroR

Zeror is working but integration with eg11 isn't yet.

Below is my zeror output:

```
Guilhermes-MBP:2 grferrei$ python zeror.py weather.arff weather.arff 
=== Predictions on test data ===
inst#	actual	predicted	error_prediction
1	2:no	1:yes		0
2	2:no	1:yes		0
3	1:yes	1:yes		1
4	1:yes	1:yes		1
5	1:yes	1:yes		1
6	2:no	1:yes		0
7	1:yes	1:yes		1
8	2:no	1:yes		0
9	1:yes	1:yes		1
10	1:yes	1:yes		1
11	1:yes	1:yes		1
12	1:yes	1:yes		1
13	1:yes	1:yes		1
14	2:no	1:yes		0

```


## Table reader

Below is the output of my table reader:

```
Guilhermes-MBP:2 grferrei$ python reader.py weather.csv 
outlook - Mode: sunny; Entropy: 1.57740628285
?temperature- - Mean: 73.5714285714; Standard Deviation: 6.57166745863
<humidity - Mean: 81.6428571429; Standard Deviation: 10.285218242
windy - Mode: FALSE; Entropy: 0.985228136034
=play - Mean: 1.07142857143; Standard Deviation: 0.997248963151
```