###i. Reference

Posnett, Daryl, Vladimir Filkov, and Premkumar Devanbu. "Ecological inference in empirical software engineering." Proceedings of the 2011 26th IEEE/ACM International Conference on Automated Software Engineering. IEEE Computer Society, 2011.

###ii. Keywords

ii1. Software hierarchy: Software systems can be decomposed hierarchically into modules, packages and files. This has a great influence on the evolvability and maintainability of a software product, and on defining work assignment. 

ii2. Empirical software engineering: ESE is mainly concerned with running experiments that can gather data regarding outcomes that are observable, like quality and productivity. Such outcomes are subject to large-sample studies, so that statistical methods can be brought to bear for hypothesis testing, and machine learning methods on past data can be built into tools that support programming tasks.
    
ii3. Ecological inference (in the SE context): Ecological inference is when an empirical finding at an aggregated level (for instance, packages) can be applied at the disaggregated level (files). When this inference is mistaken, we
have the ecological fallacy.
    
ii4. Ecological fallacy (in the SE context): Ecological fallacy is when an empirical finding at an aggregated level cannot be applied at the disaggregated level, therefore only being true for the specific aggregated level.

###iii. Notes

iii1. Motivational Statement: Software systems can be decomposed hierarchically, for instance, into modules, packages and files. This hierarchical decomposition has an immense influence on software evolvability, maintainability and work assignment. Hierarchical decomposition is thus clearly of central concern for empirical software engineering researchers. 
    
iii2. Hypotheses: Lay out a conceptual framework of ecological inference risk in software engineering, and empirically demonstrate the existence of this risk, while studying the incidence of ecological inference in various open source projects.
    
iii3. Statistical tests: Logistic regression was used to classify files and packages as defective using certain metrics, like LOC, churn and number of lines and commits, as predictors. For each predictor the z-test statistic, which is a measure of the likelihood that the actual value of the parameter is not zero, is computed by dividing the estimated value of the parameter by its standard error and used to asses the significance of the variable.
    
iii4. Sampling procedures: Data was extracted from the JIRA defect tracking system and associated git repositories for 87 distinct versions of 18 different Apache projects. For each release an XML report of JIRA issues was extracted. After that the associated JIRA webpage was crawled for each issue found in the XML report and the commits related to that issue were extracted. Lastly this data was linked to the git log to determine which commits, and consequently which files and packages, are associated with defects. 

###iv. Improvements

iv1. 

iv2. 

iv3. 
