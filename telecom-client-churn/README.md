# Telecom client churn analysis for Interconnect

The telecom operator Interconnect would like to be able to forecast their churn of clients. If it's discovered that a user is planning to leave, Interconnect 
can offer promotional deals and special plan options to perhaps prevent the user from leaving their services. Based on information 
of each client, including information about their plans, contracts, and personal characteristics, can machine learning assist in accurately predicting which users are close to discontinuing 
service? An acceptable model much yield an AUC-ROC of at least 0.75 to be promoted to production.

### Project plan
This is a Jupyter notebook of in-depth data analysis that led to the project plan. The plan outline can be seen at the end of the notebook.

https://github.com/rmodesitt/data-projects-TripleTen/blob/main/telecom-client-churn/client_churn_project_plan.ipynb


### Project notebook
This is a Jupyter notebook that contains the exploratory data analysis, modeling, and final evaluation of the project.

https://github.com/rmodesitt/data-projects-TripleTen/blob/main/telecom-client-churn/telecom_client_churn.ipynb

### Data 
The data consists of 4 .csv files obtained from different sources.

- contract.csv — contract information<br>
  https://github.com/rmodesitt/data-projects-TripleTen/blob/main/telecom-client-churn/contract.csv  
- personal.csv — the client's personal data<br>
  https://github.com/rmodesitt/data-projects-TripleTen/blob/main/telecom-client-churn/internet.csv
- internet.csv — information about Internet services<br>
  https://github.com/rmodesitt/data-projects-TripleTen/blob/main/telecom-client-churn/personal.csv
- phone.csv — information about telephone services<br>
  https://github.com/rmodesitt/data-projects-TripleTen/blob/main/telecom-client-churn/phone.csv

In each file, the column customerID contains a unique code assigned to each client.
