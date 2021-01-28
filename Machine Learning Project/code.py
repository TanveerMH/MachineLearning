import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import classification_report


#read dataset into dataframe
path = "D:/SEM 5/CSC 3304 - Machine Learning/Assignment/Dataset 1/dataset.csv"
df = pd.read_csv(path)

#print columns and total number of columns (inclusive of label)
#print(df.columns.values)
#print(len(df.columns.values))

#getting subset with selected features and target variable
subset_list = ["sex", "Spay/Neuter", "outcome_age_(days)", "breed1", "breed2", "cfa_breed", "coat","outcome_type"]
subset = df[subset_list]

#checking for visual cues in column name, and missing values
#print(subset.columns)
#print(subset.info())
#print(subset.shape)
#print(subset.isnull().sum())

#removing records with no outcome_type (only 3 records out of 29421) 
subset = subset.dropna(subset=["outcome_type"])
#print(subset.isnull().sum())

#normalizing outcome_type based on outcome into 1 (if adopted), 0 otherwise
subset.loc[subset.outcome_type != "Adoption", "outcome_type"] = 0
subset.loc[subset.outcome_type == "Adoption", "outcome_type"] = 1

#normalizing Spay/Neuter into 1 (if Yes), 0 otherwise
subset.loc[subset["Spay/Neuter"] != "Yes", "Spay/Neuter"] = 0
subset.loc[subset["Spay/Neuter"] == "Yes", "Spay/Neuter"] = 1

#normalizing cfa_breed into 1 (if TRUE), 0 otherwise
subset.loc[~subset["cfa_breed"], "cfa_breed"] = 0
subset.loc[subset["cfa_breed"], "cfa_breed"] = 1

#defining data types
subset.sex = subset.sex.astype('category')
subset["Spay/Neuter"] = pd.to_numeric(subset["Spay/Neuter"])
subset.breed1 = subset.breed1.astype('category')
subset.breed2 = subset.breed2.astype(str)
subset["cfa_breed"] = pd.to_numeric(subset["cfa_breed"])
subset.coat = subset.coat.astype('category')
subset["outcome_type"] = pd.to_numeric(subset["outcome_type"])

#to double check data types
print(subset.info())

#encoding strings into numbers for model input using labelEncoder
le = preprocessing.LabelEncoder()
subset.sex=le.fit_transform(subset.sex)
subset.breed1=le.fit_transform(subset.breed1)
subset.breed2=le.fit_transform(subset.breed2)
subset.coat=le.fit_transform(subset.coat)

#delineating labels and selected features
features_list = ["sex", "Spay/Neuter", "outcome_age_(days)", "breed1", "breed2", "cfa_breed", "coat"]
features = subset[features_list]
labels = subset.outcome_type

#splitting dataset into testing and training sets
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

#decalring model and fitting it on training data
rf = RandomForestClassifier()
rf.fit(x_train, y_train)

#accuracy on training data and testing data
print("score on test: " + str(rf.score(x_test, y_test)))
print("score on train: "+ str(rf.score(x_train, y_train)))

#printing confusion matrix
y_pred = rf.predict(x_test)
matrix = confusion_matrix(y_test, y_pred)
print(matrix)

#printing accuracy, recall, and precision
print (accuracy_score(y_test, y_pred))
print (recall_score(y_test, y_pred))
print (precision_score(y_test, y_pred))
