###i. Reference

D'Ambros, Marco, Michele Lanza, and Romain Robbes. "An extensive comparison of bug prediction approaches." 2010 7th IEEE Working Conference on Mining Software Repositories (MSR 2010). IEEE, 2010.

###ii. Keywords

ii1. Software Defect - Parts of the software (certain files or lines within the file) can have unwanted and unplanned errors in them, usually called bugs. Those defects often were put in by mistake, or can also be that different programs were not appropiatedly connected together. There can be multiple reasons for a defect to appear, but while some might be minor, others can be crucial to the correct behavior of the program.
    
ii2. Defect prediction - By using machine learning, data mining and statistics techniques it's possible to predict, within a degree of certainty, whether certain parts of a software is likely to have defects. Defect prediction is a primordial research topic, as it's crucial to assign personnel and/or resources to areas of a software system with a higher probable quantity of bugs.
    
ii3. Model performance evaluation - As there are many different models and approaches to tackle the software defect prediction problem, there needs to be guidelines and indicators on how to evaluate these approaches. Some of these indicators include classification of entities as defect-prone or not, ranking of the entities, with and without taking into account the effort to review an entity.
    
ii4. Bug prediction metrics - Most defect prediction approaches could be classified into three groups: code metrics, such as lines of codes and the complexity of the code; process changes, like number of changes and recent activities; or the use of previous defects information.

###iii. Notes

iii1. Motivational statements: There has been a lot of work done in the area of defect prediction, as it is one of the most important topics in software engineering research. However, there hasn't been an established benchmark on the relative performance of these approaches. Not only have they mostly been evaluated in isolation or in comparison with only a few other approaches, but most of the evaluations can't be reproduced since the data used for their evaluation came from commercial systems and is not available publicly. Therefore, there is a dire need for a baseline against which these approaches can be compared.
    
iii2. Hypotheses: This paper presents a public benchmark for defect prediction, containing data from multiple open-source software systems. It also presents two new bug prediction approaches, one measuring code churn and the other using a concept of entropy changes. Lastly, an extensive evaluation of several defect prediction approaches, aimed at comparing the performance of the approaches across different systems, testing whether the differences are statistically significant, and studying the stability of approaches across learners.
    
iii3. Data: The prediction dataset used is a collection of models and metrics of five software systems and their histories, composed of the change, bug and version information. The goal of such a dataset is to allow researchers to compare different defect prediction approaches and to evaluate whether a new technique is an improvement over existing ones. The criteria for choosing these specific systems are: size and lifetime, homogeneous language and the availability of the data.
    
iii4. Informative visualizations: Table 5
to be finished...

###iv. Improvements

iv1. Bugs are only linked with files that have a bug reference in a commit comment message. For a more representative benchmark, it would be needed to include bugs that are not referenced in a commit comment. 
    
iv2. The results might be different when compared to industrial systems, because some industrial settings enforce standards of code quality.
    
iv3. The benchmark is only for code written in Java. For a ore comprehensive study, the benchmark should be language independent. 
