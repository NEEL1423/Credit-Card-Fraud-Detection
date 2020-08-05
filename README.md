# Credit-Card-Fraud-Detection

ABSTRACT - Credit card fraudulent happens through the account holders card number, card details and personal information. E-commerce payment system is providing the payment for online transaction. The model is used to identify whether a new transaction is fraudulent or not. Aim is to detect 100% of the fraudulent transactions while minimizing the incorrect fraud classifications. A standard scalar model is initially trained with the normal behavior of a card holder. If an incoming credit card transaction is not accepted by the trained standard scalar model with sufficiently high probability, it is considered to be fraudulent. The significance of the application technique reviewed in the minimization of credit card fraud. Still some issues when genuine credit card customers are misclassified as fraudulent. Random forest builds multiple decision trees and integrate them together to get stable prediction and accuracy of about 98.6%.

SOFTWARE REQUIREMENTS - Python, Anaconda, OS - Windows 7/8/10 (32 and 64 bit).

ALGORITHM USED - Random Forest Random forest is a type of supervised machine learning algorithm based on ensemble learning. Ensemble learning is a type of learning where you join different types of algorithms or same algorithm multiple times to form a more powerful prediction model. The random forest algorithm combines multiple algorithm of the same type i.e. multiple decision trees, resulting in a forest of trees, hence the name "Random Forest". The random forest algorithm can be used for both regression and classification tasks.

ADVANTAGES OF USING RANDOM FOREST -

The random forest algorithm is not biased.
This algorithm is very stable. Even if a new data point is introduced in the dataset, the overall algorithm is not affected much.
The random forest algorithm works well when you have both categorical and numerical features.
The random forest algorithm also works well when data has missing values or it has not been scaled well.

CONCLUSION - The Random forest algorithm will perform better with a larger number of training data, but speed during testing and application will suffer. Application of more pre-processing techniques would also help. Others algorithm still suffers from the imbalanced dataset problem and requires more preprocessing to give better results at the results shown by other algorithms is great but it could have been better if more preprocessing have been done on the data.
