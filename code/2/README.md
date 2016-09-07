# Homework 2

## Active Shooter Exercise


### List two things not to do during an active shooter event:

Don't panic.

Don't huddle together, better to spread out.

### List two things best to do during an active shooter event

Be aware of your surroundings and the nearest exits/hiding spots.

Trust you instincts and get out if you can.


## ZeroR

For the ```jedit-4.1.arff``` dataset Zeror finds that ```false``` is the majority class, thus predicting ```false``` for everything. Because of that, c=d=0, causing pd and pf to also be 0.

```
pd

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,         myzr ,       0  ,     0 (*              |              ), 0.00,  0.00,  0.00,  0.00,  0.00
   2 ,           nb ,      45  ,    18 (        ---   *| --           ),25.00, 36.00, 45.00, 53.00, 60.00
   2 ,       rbfnet ,      47  ,    20 (        ------ *   ---        ),25.00, 43.00, 47.00, 60.00, 67.00
   3 ,         bnet ,      60  ,    17 (             --|-- *  -       ),40.00, 55.00, 60.00, 67.00, 71.00
   3 ,         jrip ,      60  ,    23 (          -----|   *   ---    ),33.00, 50.00, 60.00, 71.00, 80.00
   4 ,          j48 ,      72  ,    16 (               |-----  *  --  ),50.00, 65.00, 72.00, 81.00, 87.00
pf

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,         myzr ,       0  ,     0 (*              |              ), 0.00,  0.00,  0.00,  0.00,  0.00
   2 ,          j48 ,       7  ,     6 (     --   *  --|---           ), 4.00,  5.00,  7.00,  9.00, 13.00
   2 ,           nb ,       7  ,     6 (     --   *   -|-             ), 4.00,  5.00,  7.00, 10.00, 12.00
   2 ,         jrip ,       9  ,    10 (  ---        * |------        ), 2.00,  4.00,  9.00, 11.00, 15.00
   2 ,       rbfnet ,       9  ,     5 (     -----   * |----          ), 4.00,  7.00,  9.00, 11.00, 14.00
   2 ,         bnet ,      11  ,     6 (        -----  |*   ------    ), 6.00,  9.00, 11.00, 14.00, 18.00

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
