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
    X, y, test_size=0.2, random_state=42
)

gbm_model = GradientBoostingClassifier()
gbm_model.fit(X_train, y_train)

y_pred = gbm_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred) * 100

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
    # 1. Electioneering Costs
    # 2. Independent Expenditures
    # 3. Party Expenditures
             """)