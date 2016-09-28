###i. Reference

Jiang, Tian, Lin Tan, and Sunghun Kim. "Personalized defect prediction." Automated Software Engineering (ASE), 2013 IEEE/ACM 28th International Conference on. IEEE, 2013.

###ii. Keywords

ii1. Defect prediction: By using machine learning techniques, we can predict whether a particular file has a chance of introducing bugs. The better the techniques used, the more reliable the predictions will be.

ii2. Personalized defect prediction: Consists of building a separate prediction model for each developer to predict software defects, since developers have different coding styles, commit frequencies, and experience levels, which consequently cause different defect patterns.

ii3. Change classification: It tries to predict defects at the change level. A change is the lines modified in one file of a software version control system commit.

###iii. Notes

iii1. Motivational Statements: Different developers have different coding styles, commit frequencies, and experience levels, all of which cause different defect patterns. When the defects of different developers are combined, such differences are obscured, hurting the prediction performance. Therefore, it is desirable to build personalized defect prediction models.

iii2. Hypotheses: By using personalized defect prediction and looking at the file change level, it's possible to discover up to 155 more bugs than the traditional change classification (210 versus 55) if developers inspect the top 20% lines of code that are predicted buggy. In addition, this approach improves the F1-score by 0.01–0.06 when compared to the traditional change classification.

iii3. Statistical tests: First each experiment was repeated several times to obtain several samples for each test subject. Then the Wilcoxon signed-rank test was applied on the samples in each test subject and across subjects. The Wilcoxon signed-rank test does not require the underlying data to follow any distribution, can be applied on pairs of data, and is able to compare the difference against zero. At the 95% confidence level, p-values that are smaller than 0.05 indicates that the differences between PCC and CC are statistically significant. p-values that are 0.05 or larger indicates that we find no evidence that the differences are statistically significant.

iii4. Sampling procedures: Six open-source projects were chosen to be tested because they have enough change history to build and evaluate PCC, and they are commonly used in the literature. For feature selection (features are attributes extracted from a commit which describe the characteristics of the source code, such as LOC), there where three categories of features chosen: characteristic vectors, bag-of-words and metadata.

###iv. Improvements

iv1. The technique presented should be applied against different types of projects too, like closed source projects and medium/small sized projects, in order to assert that the results are generable enough to most software projects

iv2. During the data preprocessing step, the number of developers were narrowed down to the top developers. While that might be a good approach, it doesn't show that the technique will also work with developers who didn't produce as much change but could have introduced defects.
