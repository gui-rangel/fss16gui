###i. Reference

Ghotra, Baljinder, Shane McIntosh, and Ahmed E. Hassan. "Revisiting the impact of classification techniques on the performance of defect prediction models" Proceedings of the 37th International Conference on Software Engineering-Volume 1. IEEE Press, 2015.

###ii. Keywords

ii1. Software Defect: Parts of the software (certain files or lines within the file) can have unwanted and unplanned errors in them, usually called bugs. Those defects often were put in by mistake, or can also be that different programs were not appropiatedly connected together. There can be multiple reasons for a defect to appear, but while some might be minor, others can be crucial to the correct behavior of the program.

ii3. Prediction Model: We can use machine learning algorithms and techniques, combined with a dataset, to build a prediction model that can be reused multiple times for different datasets, in order to predict an unknown value.

ii2. Defect Prediction: By using machine learning, data mining and statistics techniques it's possible to predict, within a degree of certainty, whether certain parts of a software is likely to have defects. Defect prediction is a primordial research topic, as it's crucial to assign personnel and/or resources to areas of a software system with a higher probable quantity of bugs.

ii4. Classification Models: In machine learning and statistics, classification is the problem of identifying to which of a set of categories (sub-populations) a new observation belongs, on the basis of a training set of data containing observations (or instances) whose category membership is known. By creating a classification model, one can classify new data points as they come in.

###iii. Notes

iii1. Motivational Statements: Recent research on the NASA dataset suggests that the performance of a defect prediction model is not significantly impacted by the classification technique that is used to train it. However, the dataset that is used in the prior study is both: (a) noisy, i.e., contains erroneous entries and (b) biased, i.e., only contains software developed in one setting.

iii2. Hypotheses: The paper intends to verify that the choice of classification technique indeed has an impact on the performance of defect prediction models, suggesting that some classification techniques tend to produce defect prediction models that outperform others. These classification techniques can be further clustered in statistically distinct groups of techniques, where one group clearly performs better than the other.

iii3. Statistical tests: To compare the performance of defect prediction models, the Area Under the receiver operating characteristic Curve (AUC) was used, which plots the false positive rate (i.e., FP/FP+TN) against the true positive rate (i.e., TP/FN+TP). Larger AUC values indicate better performance. AUC values above 0.5 indicate that the model outperforms random guessing. In order to group classification techniques into statistically distinct ranks, the Scott-Knott test was used. The Scott-Knott test uses hierarchical cluster analysis to partition the classification techniques into ranks. The Scott-Knott test was used to overcome the confounding issue of overlapping groups that are produced by several other post hoc tests.

iii4. Informative visualizations: 

The figure below provides an overview of the steps in the approach.

![alt text](https://github.com/gui-rangel/fss16gui/blob/master/read/r6_1.png "Model Overview")

The figure below provides an overview of the Scott-Knott test approach.

![alt text](https://github.com/gui-rangel/fss16gui/blob/master/read/r6_2.png "Ranking")


###iv. Improvements

iv1. The datasets that were analyzed are part of two corpora (i.e., NASA and PROMISE), which each provide a different set of predictor metrics. Since the metrics vary, this is a point of variation between the studied corpora, which may explain some of the differences that we observe when drawing comparisons across the corpora.

iv2. The experiments were performed on 29 datasets, which may threaten the generalization of the results of our study. The consistency of the results are based on two studied data corpora. The results may vary in other corpora that were not analyzed. 

iv3. The tuning of the parameters of the K-means (k = 2) and KNN (K = 8) techniques that were used may influence the results. Moreover, the remaining techniques were used with the out-the-shelf configurations, without any additional configuration or tuning whatsoever. Optimal paremeter tuning of the other algorithms may alter results obtained.

