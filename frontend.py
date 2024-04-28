import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
accuracy = 50

chart = generate_pie_chart(accuracy)
chart_placeholder.pyplot(chart)


selected_features = st.multiselect(
    "Select features",
    ("Independent Expenditures", "Party Expenditures", "Electioneering Costs")
)

if selected_features:
    def calculate_accuracy(selected_features):
        #where model code goes to calc accuracy based off features
        accuracy = 90  # placeholder accuracy value
        return accuracy

    accuracy = calculate_accuracy(selected_features)
    new_chart = generate_pie_chart(accuracy)
    chart_placeholder.pyplot(new_chart)

if st.button('Rank Features'):
    st.empty()
    st.write("""
    # Features, ranked
    # 1. Electioneering Costs
    # 2. Independent Expenditures
    # 3. Party Expenditures
             """)