###i. Reference

Hassan, Ahmed E. "Predicting faults using the complexity of code changes" Proceedings of the 31st International Conference on Software Engineering. IEEE Computer Society, 2009.

###ii. Keywords

ii1. Code fault: During the development process, developers might accidentally code a functionality that they did not intend to put there initially. Likewise, sometimes when you add pieces of different software together, they might present a behavior that was different than the expected one. That and other cases can be classified as code faults, or more colloquially code bugs, where parts of the software are malfunctioning in a way that is different than the expected outcome.

ii2. Fault prediction: By using many different techniques, such as data mining, machine learning, etc., one can try to predict whether a particular piece of software is likely or not to present a code fault in the future. Such application is primal for early detection of defects that can have a high impact on the overall functionality of the system in the future.

ii3. Complex code change process: Modifications are done by developers to implement new features and repair faults. By studying these patterns and quantifying their degree of complexity over time, it's possible to achieve a better understanding of the complexity facing developers who are evolving and working on a project. 

###iii. Notes

iii1. Motivational Statements: Predicting the incidence of faults in code has been commonly associated with measuring code complexity. While managing the complexity of a project is a paramount goal while striving to meet user needs, little attention has been paid to measuring and controlling the complexity of the code change process. A software system with a complex code change process is undesirable since it will likely produce a system which has many faults and the project will face delays.

iii2. Hypotheses: It is believed that a complex code change process negatively affects its product, the software system. The more complex changes to a file, the higher the chance the file will contain faults. Therefore, by using the complexity of code changes one can better predict the incidence of faults in a software system.

iii3. Briand et al., Graves et al., Khoshgoftaar et al., Leszak et al., and Nagappan and Ball indicate that prior modifications to a file are a good predictor of its fault potential (i.e., the more a file is changed, the more likely it will contain faults). Graves et al. and Leszak et al. and by Herraiz et al. show that most code complexity metrics highly correlate with LOC, a much simpler metric. Moser et al. show that process metrics outperform code metrics as predictors of
future faults, while Yu et al. indicate that prior faults are good predictors of future faults.

iii4. Baseline Results: 
![alt text](https://github.com/gui-rangel/fss16gui/blob/master/read/R1.png "")
![alt text](https://github.com/gui-rangel/fss16gui/blob/master/read/R2.png "")
![alt text](https://github.com/gui-rangel/fss16gui/blob/master/read/R3.png "")


###iv. Improvements

iv1. Using a dataset that contains defects could help improve the analysis performed. Especially if such a dataset can contain the relationship between defects and commits/lines changed.

iv2. Perform the same analysis to other types of systems, such as commercial systems and small/medium sized systems, to see if the results hold.

iv3. Rather than just show the statistical relationship between complex code change process and the appearance of faults, also show the temporal precedence, meaning proving that certain complex code change process are the culprit for the appearance of faults.
