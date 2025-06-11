# Forecasting gold (Au) concentration from ore mixture

A company named <b>Zyfra</b> wants to be able to predict the total amount of gold concentrate recovered from gold ore before it is extracted and purified. However, the variability of the contents from ore mixture to ore mixture makes it difficult to easily predict the total concentration of gold. Some variables include the concentrations of other elements in the feed, the different solutions used during the cleaning process, and the particle feed size in the mixture. Zyfra has requested a model be built that assesses the different variables / features of each mixture and then predicts the amount of gold in the mixture, ultimately optimizing the production of gold for the future. 

### Project plan
- Prepare the data
- Clean the data and perform preprocessing
- Analyze the data
  - Concentrations of metals (Au, Ag, Pb) changes during purification stage
  - Feed particle size distribution comparison
  - Total concentrations of all elements at different stages
- Build the model
  - Create a function to calculate final *sMAPE*
  - Train and tune different models. Evaluate using cross-validation
  - Evaluate model using final *sMAPE* metric
- Perform final testing and evaluation

### Project notebook
This is a notebook containing the exploratory analysis and model building for the project.

https://github.com/rmodesitt/data-projects-TripleTen/blob/main/gold-mine-recovery/gold_recovery_test.csv

### Data
These are three .csv files containing data of each ore mixture - training, test, and source. Data is indexed with the date and time of acquisition (<mark>date</mark>) feature. Parameters that are next to each other in terms of time are often similar.

Some parameters are not available because they were measured and / or calculated much later. That's why, some of the features that are present in the training are absent from the test set. The test set also doesn't contain targets.

The source dataset contains the training and test datasets with all the features. 

Training - https://github.com/rmodesitt/data-projects-TripleTen/blob/main/gold-mine-recovery/gold_recovery_train.csv</br>
Test - https://github.com/rmodesitt/data-projects-TripleTen/blob/main/gold-mine-recovery/gold_mine_recovery.ipynb</br>
Source (full) - https://github.com/rmodesitt/data-projects-TripleTen/blob/main/gold-mine-recovery/gold_recovery_full.csv
