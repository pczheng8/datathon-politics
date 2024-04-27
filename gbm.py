from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#preprocess and stuff
X = ...
y = ...

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Gradient Boosting Machine (GBM) model
gbm_model = GradientBoostingClassifier()
gbm_model.fit(X_train, y_train)

# Evaluate model
y_pred = gbm_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# Get feature importance scores
feature_importance = gbm_model.feature_importances_

# Get feature names
feature_names = X.columns  # Assuming X is a pandas DataFrame with column names

# Create a dictionary mapping feature names to importance scores
feature_importance_dict = dict(zip(feature_names, feature_importance))

# Sort features by importance score in descending order
sorted_features = sorted(feature_importance_dict.items(), key=lambda x: x[1], reverse=True)

# Print or visualize the ranking of features
for feature, importance in sorted_features:
    print(f"{feature}: {importance}")