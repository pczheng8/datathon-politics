import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("ML Model/new_csv2.csv")
X = df[["party expenditures", "independent expenditures", "electioneering costs"]]
y = df["won"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=None
)

gbm_model = GradientBoostingClassifier()
gbm_model.fit(X_train, y_train)

y_pred = gbm_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred) * 100


feature_importance = gbm_model.feature_importances_
feature_names = df.columns  

feature_names = ['party expenditures', 'independent expenditures', 'electioneering costs']  

feature_importance_dict = dict(zip(feature_names, feature_importance))
sorted_features = sorted(
    feature_importance_dict.items(), key=lambda x: x[1], reverse=True
)


st.write("""
# Accuracy  
""")

def generate_pie_chart(accuracy):
    empty_percentage = 100 - accuracy
    sizes = [accuracy, empty_percentage]
    labels = ['Accurate', 'Inaccurate']
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'pink'])
    ax.axis('equal') 
    return fig

chart_placeholder = st.empty()

chart = generate_pie_chart(accuracy)
chart_placeholder.pyplot(chart)



if st.button('Rank Features'):
    st.empty()
    st.write("""
    # Features, ranked
    """)
    for i, (feature, importance) in enumerate(sorted_features, start=1):
        st.write(f"{i}. {feature}")

    fig, ax = plt.subplots(figsize=(10, 8))
    features, importances = zip(*sorted_features)
    ax.bar(features, importances, color='skyblue')
    ax.set_xlabel('Features')
    ax.set_ylabel('Importance')
    ax.set_title('Relative Importance of Features')
    plt.xticks(rotation=45)
    st.pyplot(fig)
