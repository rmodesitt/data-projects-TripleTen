# Oil well development location analysis

OilyGiant mining company is building a new oil well development, but there are 3 potential regions to where the development can be 
built. Each region has different characteristics and volume of oil reserves that determine its sustainability and profitability. Which 
region is most suitable and will bring in the most profit based on their characteristics? The request is to perform analysis and create a model 
that accurately predicts the volume of oil reserves in each region, to calculate the profitability of each region, and recommend a 
region for the new oil well development.

### Project plan

- Download and prepare the data
- Train and tune a linear regression model for each region
  - Predict the average volume of reserves in the new wells
  - Evaluate model using RMSE
- Prepare for profit calculation
  - Calculate the volume of reserves needed for developing a new well without losses. Compare with the average volume of reserves in each region
- Calculate profit from the highest volume of reserves from predictions
  - Use the bootstrapping technique to find the distribution of profit
  - Find average profit, 95% confidence interval, and risk of losses
- Recommend a region for development

### Data
There are three .csv files containing geological exploration data for the three regions.

Region 0 - https://github.com/rmodesitt/data-projects-TripleTen/blob/main/oil-well-location-analysis/geo_data_0.csv</br>
Region 1 - https://github.com/rmodesitt/data-projects-TripleTen/blob/main/oil-well-location-analysis/geo_data_1.csv</br>
Region 2 - https://github.com/rmodesitt/data-projects-TripleTen/blob/main/oil-well-location-analysis/geo_data_2.csv</br>

_id_ — unique oil well identifier</br>
_f0, f1, f2_ — three features of points</br>
_product_ — volume of reserves in the oil well (thousand barrels)</br>
