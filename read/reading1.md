###i. Reference

    Bettenburg, Nicolas, Meiyappan Nagappan, and Ahmed E. Hassan. "Think locally, act globally: Improving defect and effort prediction models." Proceedings of the 9th IEEE Working Conference on Mining Software Repositories. IEEE Press, 2012.

###ii. Keywords

    ii1. Defect Prediction: By using machine learning techniques, we can predict whether a particular file has a chance of introducing bugs. The better the techniques used, the more reliable the predictions will be.
    
    ii2. Effort Estimation: By also using machine learning techniques, it tries to predict how much effort (for instance programmer's hours) it'll take for a determined problem or issue to be resolved.
    
    ii3. Prediction Model: We can use machine learning algorithms and techniques, combined with a dataset, to build a prediction model that can be reused multiple times for different datasets, in order to predict an unknown value.
    
    ii4. Local X Global Models: To build a prediction model, we need a dataset. However, there are differences and advantages in either using the entire dataset (to build a global model) or using particular subsets of the dataset (to build local models).

###iii. Notes

    iii1. Motivational Statements: There has been many recent efforts on the creation of effort and defect prediction models, but they mainly use the entire dataset to build the model. It has been shown that software engineering data contains a large amount of variability, which can lead to poor fit of machine learning models to the underlying data. Although there are recent research showing that there is benefit in partitioning datasets into smaller subsets, it is still not known whether this holds for goodness of fit and for statistical techniques like linear regression.
    
    iii2. Hypothesis: This paper hypothesizes that using local models instead of global ones can result in a better fit, which is beneficial for researchers and practitioners when using regression model for understanding. This would also  increase the predictive power of statistical models. Moreover, a mix between local and global models, a hybrid, could unite the best of both worlds by using patterns from global models together with local characteristics.
    
    iii3. Related Work: Much work has been done on creating prediction models for software engineering data. Nagappan et al. used source code complexity metrics, Mockus et al. studied the use of linear regression models to predict the risk of source code change, Andreou et al. used decision trees to model and predict the costs involved in software development, among others. The one that relates the most in the work by Menzies et al. where he starts to explore the difference in what can be learned between individual subsets and the whole dataset. This paper builds on the information learned from said work.
    
    iii4. Informative Visualizations: Among the figures and tables presented, a very informative one was Table III, which compares the experimental results for the 3 methods (global, local and hybrid) for the 4 datasets. Through it we can clearly see that hybrid approach outperforms the others. Another interesting figure is figure 2, which shows how they built the global and local regression models. Although the global one can be straightforward, for the local one they use a clustering algorithm to find subsets that have similarities between them. 

###iv. Improvements

    iv1. Show comparisons between their results and results with other techniques from other papers.
    
    iv2. Explain better why one would still prefer to use to use a local or global approach instead of the hybrid one.
    
    iv3. See if different clustering algorithms can affect the prediction outcome of local models.
