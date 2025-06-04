import matplotlib.pyplot as plt
import streamlit as st

def plot_pie(pos, neg):
    fig, ax = plt.subplots()
    ax.pie([pos, neg],
           labels=["Positive", "Negative"],
           colors=['#66bb6a', '#ef5350'],
           autopct='%1.1f%%',
           explode=(0.1, 0),
           shadow=True,
           startangle=140)
    ax.axis('equal')
    st.pyplot(fig)

def plot_bar(pos, neg):
    fig, ax = plt.subplots()
    ax.bar(["Positive", "Negative"], [pos, neg], color=['#66bb6a', '#ef5350'])
    ax.set_ylim(0, 100)
    ax.set_ylabel("Sentiment %")
    ax.set_title("Positive vs Negative Sentiment Ratio")
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    st.pyplot(fig)
