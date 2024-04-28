from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt

# will change to final_financial_data.csv, currently this is like a temp file
df = pd.read_csv("ML Model/new_csv2.csv")

# preprocess and stuff
X = df[["party expenditures", "independent expenditures", "electioneering costs"]]
y = df["won"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=None
)

gbm_model = GradientBoostingClassifier()
gbm_model.fit(X_train, y_train)

y_pred = gbm_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


feature_importance = gbm_model.feature_importances_
feature_names = df.columns  

# Get feature names
feature_names = ['party expenditures', 'independent expenditures', 'electioneering costs']  # Assuming X is a pandas DataFrame with column names

# Create a dictionary mapping feature names to importance scores
feature_importance_dict = dict(zip(feature_names, feature_importance))
sorted_features = sorted(
    feature_importance_dict.items(), key=lambda x: x[1], reverse=True
)

features, importances = zip(*sorted_features)

# Creating the bar graph
plt.figure(figsize=(10, 8))  # You can adjust the figure size as needed
plt.bar(features, importances, color='skyblue')  # You can change the color
plt.xlabel('Features')
plt.ylabel('Importance')
plt.title('Relative Importance of Features')
plt.xticks(rotation=45)  # Rotates the x-axis labels to avoid overlap
plt.show()

# Print or visualize the ranking of features
for feature, importance in sorted_features:
    print(f"{feature}: {importance}")

prediction = gbm_model.predict(X_test)
df2 = pd.DataFrame(prediction, columns=["output"])


df2_filtered = df2[df2["output"] == 1]

print(df2_filtered)
