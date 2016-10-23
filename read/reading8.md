###i. Reference

Wang, Song, Taiyue Liu, and Lin Tan. "Automatically learning semantic features for defect prediction." Proceedings of the 38th International Conference on Software Engineering. ACM, 2016.	

###ii. Keywords

ii1. Software Defect: Parts of the software (certain files or lines within the file) can have unwanted and unplanned errors in them, usually called bugs. Those defects often were put in by mistake, or can also be that different programs were not appropiatedly connected together. There can be multiple reasons for a defect to appear, but while some might be minor, others can be crucial to the correct behavior of the program.

ii3. Prediction Model: We can use machine learning algorithms and techniques, combined with a dataset, to build a prediction model that can be reused multiple times for different datasets, in order to predict an unknown value.

ii2. Defect Prediction: By using machine learning, data mining and statistics techniques it's possible to predict, within a degree of certainty, whether certain parts of a software is likely to have defects. Defect prediction is a primordial research topic, as it's crucial to assign personnel and/or resources to areas of a software system with a higher probable quantity of bugs.

ii4. Deep Belief Network: Deep Belief Network is a generative graphical model, which learns a representation that can reconstruct training data with a high probability. It automatically learns high-level representation of data by constructing a deep architecture.

###iii. Notes

iii1. Motivational statements: To build accurate prediction models, studies usually focus on manually designing features that encode the characteristics of programs and exploring different machine learning algorithms. Existing traditional features often fail to capture the semantic differences of programs, and such a capability is needed for building accurate prediction models.

iii2. Hypothesis: To bridge the gap between programs’ semantics and defect prediction features, the paper proposes to leverage a powerful representation-learning algorithm, deep learning, to learn semantic representation of programs automatically from source code. Specifically, we leverage Deep Belief Network (DBN) to automatically learn semantic features from token vectors extracted from programs’ Abstract Syntax Trees (ASTs).

iii3. Informative visualizations: 

![alt text](https://github.com/gui-rangel/fss16gui/edit/master/read/r8p1.png "")

![alt text](https://github.com/gui-rangel/fss16gui/edit/master/read/r8p2.png "")


iii4. Datasets:

![alt text](https://github.com/gui-rangel/fss16gui/edit/master/read/r8p3.png "")


###iv. Improvements

iv1. The results might differ if the approach is used on closed-source projects.

iv2. The current implementation of the technique presented focuses only on Java projects. It's unclear wether the technique can be used for other languages, or produce the same results.

