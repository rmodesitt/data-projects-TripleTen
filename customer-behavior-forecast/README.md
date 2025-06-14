# Predicting future customer behaviors at Beta Bank
  
Beta Bank customers are leaving: little by little, chipping away every month. Rather than using a lot of effort, energy, and money to replace these customers, the bankers figured out it’s cheaper to try and keep their business. Therefore, it has been requested to present analysis and create a model that helps predict whether a customer will leave the bank soon based on data of the clients’ past behavior and termination of contracts with the bank. The threshold for an acceptable model is a F1 score of <b>59%</b>.

### Project plan

- Download and prepare the data
- Examine the balance of classes. Train the model without taking into account the imbalance
- Improve the quality of the model
  - Use two approaches to fix class imbalance
  - Train different models on training and validation sets
  - Tune and pick the best parameters
- Perform final testing and evaluation

###  Project notebook
This is Jupyter notebook containing the analysis, models, and report write-up of the project.

https://github.com/rmodesitt/data-projects-TripleTen/blob/main/customer-behavior-forecast/customer_behavior_forecast.ipynb

### Data
This is a .csv file containing data of the clients' past behavior and contract information.

https://github.com/rmodesitt/data-projects-TripleTen/blob/main/customer-behavior-forecast/customer_behavior_churn.csv
