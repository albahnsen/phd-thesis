Example-Dependent Cost-Sensitive Classification
============================
## Applications in Financial Risk Modeling and Marketing Analytics


PhD dissertation, Alejandro Correa Bahnsen, September 2015.

_Permanent URL (PDF):_ TBD (orbilu link)

_Mirror (PDF):_ [Thesis](https://github.com/albahnsen/phd-thesis/raw/master/Thesis_ExampleDependentCostSensitiveClassification.pdf)

_Source code:_ [costcla](https://github.com/albahnsen/CostSensitiveClassification)

_Slides:_ [Slides](https://github.com/albahnsen/phd-thesis/raw/master/slides/Thesis_ExampleDependentCostSensitiveClassification_slides.pdf)

_License:_ BSD 3 clause

_Contact:_ Alejandro Correa Bahnsen (<al.bahnsen@gmail.com>) [@albahnsen](https://twitter.com/albahnsen) [LinkedIn](https://www.linkedin.com/in/albahnsen)

---

## Abstract

Several real-world binary classification problems are example-dependent cost-sensitive in nature, where the 
costs due to misclassification vary between examples and not only within classes. However, standard binary
classification methods do not take these costs into account, and assume a constant cost of 
misclassification errors. This approach is not realistic in many real-world applications. For  
example in credit card fraud detection, failing to detect a fraudulent transaction may have an 
economical impact from a few to thousands of Euros, depending on the particular transaction and card 
holder. In churn modeling, a model is used for predicting which customers are more likely to 
abandon a service provider. In this context, failing to identify a   profitable or unprofitable 
churner has a significant different economic   result. Similarly, in direct marketing, wrongly 
predicting that a customer   will not accept an offer when in fact he will, may have different 
financial impact, as not all   customers generate the same profit. Lastly, in credit scoring, 
accepting   loans from bad customers does not have the same economical loss, since customers have 
different   credit lines, therefore, different profit.

Accordingly, the goal of this thesis is to provide an in-depth analysis of example-dependent 
cost-sensitive classification. We analyze four real-world classification problems, namely, 
credit card fraud detection, credit scoring, churn modeling and direct marketing. For each problem, 
we propose an example-dependent cost-sensitive evaluation measure.

We propose four example-dependent cost-sensitive methods; the first method is a cost-sensitive 
Bayes minimum risk classifier which consists in quantifying tradeoffs between various decisions 
using probabilities and the costs that accompany such decisions. Second, we propose a
cost-sensitive logistic regression technique. This algorithm is based on a new logistic regression 
cost function; one that takes into account the real costs due to misclassification and correct 
classification. Subsequently, we propose a cost-sensitive decision trees algorithm which is based 
on incorporating the different example-dependent costs into a new cost-based impurity measure and a 
new cost-based pruning criteria. Lastly, we define an example-dependent cost-sensitive framework 
for ensembles of decision-trees. It is based on training example-dependent cost-sensitive 
decision trees using four different random inducer methods and then blending them using three 
different combination approaches. Moreover, we present the library \mbox{\textit{CostCla}} developed 
as part of the thesis. This library is an open-source implementation of all the algorithms covered 
in this manuscript.

Finally, the experimental results show the importance of using the real example-dependent financial 
costs associated with real-world applications. We found that there are significant differences 
in the results when evaluating a model using a traditional cost-insensitive measure such as  
accuracy or F1Score, than when using the financial savings. Moreover, the results show that the 
proposed algorithms have better results for all databases, in the sense of higher savings.
