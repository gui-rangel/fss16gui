###i. Reference

Nam, Jaechang, and Sunghun Kim. "Heterogeneous defect prediction." Proceedings of the 2015 10th joint meeting on foundations of software engineering. ACM, 2015.
APA	

###ii. Keywords

ii1. Software Defect: Parts of the software (certain files or lines within the file) can have unwanted and unplanned errors in them, usually called bugs. Those defects often were put in by mistake, or can also be that different programs were not appropiatedly connected together. There can be multiple reasons for a defect to appear, but while some might be minor, others can be crucial to the correct behavior of the program.

ii3. Prediction Model: We can use machine learning algorithms and techniques, combined with a dataset, to build a prediction model that can be reused multiple times for different datasets, in order to predict an unknown value.

ii2. Defect Prediction: By using machine learning, data mining and statistics techniques it's possible to predict, within a degree of certainty, whether certain parts of a software is likely to have defects. Defect prediction is a primordial research topic, as it's crucial to assign personnel and/or resources to areas of a software system with a higher probable quantity of bugs.

ii4. Crossproject Defect Prediction: Crossproject Defect Prediction is normally used for new projects lacking in historical data by reusing prediction models built by other project datasets. By using models and data from other, similar projects, one can sucessfully predict defects for a project that doesn't have enough project history.

###iii. Notes

iii1. Motivational Statements: Crossproject Defect Prediction requires projects to have a similar metric set, meaning the metric sets should be identical between projects. As a result, current techniques for Crossproject Defect Prediction are difficult to apply across projects with heterogeneous metric sets.

iii2. Hypotheses: To address this limitation, the paper proposes heterogeneous defect prediction (HDP) to predict defects across projects with heterogeneous metric sets. The HDP approach conducts metric selection and metric matching to build a prediction model between projects with heterogeneous metric sets.

iii3. Datasets Used: 

![alt text](https://github.com/gui-rangel/fss16gui/edit/master/read/r7data.png "Dataset Used")
 

iii4. Baseline Results: 

![alt text](https://github.com/gui-rangel/fss16gui/edit/master/read/r7results.png "Results Obtained")


###iv. Improvements

iv1. Results obtained might not hold if industrial projects were used instead of open source projects.

iv2. While area under curve (AUC) is a good measure for comparing different prediction models, more experiments nee to be done to see if precision and recall values are also desirable.

iv3. Instead of using a 50/50% split between training and testing sets, cross-validation might be more desirable.

