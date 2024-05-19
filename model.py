import pandas as pd
#from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
#from sklearn.decomposition import PCA
from sklearn.svm import SVC
#from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
#from sklearn.pipeline import make_pipeline
import joblib

#Load breast cancer dataset
data = pd.read_csv("/home/linux/Downloads/ML/breast_cancer.csv")
X = data.drop(['id','diagnosis'], axis=1)
y = data['diagnosis']

#Select only the first 10 features
X = X.iloc[:, :10]

#Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=60)

#Replace NaN values with the mean of each feature
imputer = SimpleImputer(strategy='mean')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

#Create an SVM model
#svm_model = make_pipeline(StandardScaler(), PCA(n_components=10), SVC(kernel='linear', C=1.0))
svm_model = SVC(kernel='linear', C=1.0)
#Train the SVM model
svm_model.fit(X_train, y_train)

#Evaluate the model
accuracy = svm_model.score(X_test, y_test)
print("Test Accuracy:", accuracy)

#Save the trained model to a file
joblib.dump(svm_model, 'bc_model.pkl')
