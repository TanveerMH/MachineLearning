### GRID SEARCHING SNIPPET

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
import random

# Define te range of values for the grid search
param_grid = {
    'bootstrap': [True],
    'max_depth': [60, 70, 80, 90],
    'max_features': [3, 4, 5],
    'min_samples_leaf': [4, 5, 6],
    'min_samples_split': [6, 8, 10],
    'n_estimators': [150, 200, 250]
}

# Create the random forest classifier model
rf = RandomForestClassifier(random_state = 42)

# Create the grid search model
grid_search = GridSearchCV(estimator = rf, param_grid = param_grid, cv = 3, n_jobs = -1, return_train_score=True)

# Fit the grid search to the data
grid_search.fit(x_train, y_train);

#Retrieve best parameter values
best_params = grid_search.best_params_

###RE-TRAINING THE MODEL USING THE PARAMETERS

#declaring model and fitting it on training data
rf = RandomForestClassifier(**best_params)
#rf = RandomForestClassifier()
rf.fit(x_train, y_train)