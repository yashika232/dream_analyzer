import streamlit as st
import pandas as pd
from utils.gemini_api import generate_interpretation
from utils.sentiment import analyze_sentiment
from utils.vizualizations import plot_pie, plot_bar

st.set_page_config(page_title="🌙 Dream Analyzer", layout="wide")

st.title("🌙 Dream Analysis with Cognitive Theory")
st.markdown("Enter your dream below to receive an insightful, psychology-based interpretation using Calvin Hall’s Cognitive Theory.")

# Load preloaded dream dictionary
@st.cache_data
def load_dream_dictionary():
    df = pd.read_csv("dreams_interpretations.csv")
    df.columns = df.columns.str.strip()
    return df

dream_df = load_dream_dictionary()

# Input
user_dream = st.text_area("📝 Describe your dream:", height=200)
analyze = st.button("🔍 Analyze Dream")

if analyze and user_dream.strip():
    # Match symbols
    matched = []
    for symbol in dream_df['Dream Symbol']:
        if str(symbol).lower() in user_dream.lower():
            meaning = dream_df.loc[dream_df['Dream Symbol'] == symbol, 'Interpretation'].values[0]
            matched.append(f"**{symbol}**: {meaning}")
    matched_text = "\n".join(matched) if matched else "⚠️ No matching symbols found."

    st.subheader("🔑 Matched Symbols")
    st.markdown(matched_text)

    # Gemini interpretation
    interpretation = generate_interpretation(user_dream, matched_text)
    st.subheader("🧠 Dream Interpretation")
    st.markdown(interpretation)

    # Sentiment analysis
    polarity, sentiment = analyze_sentiment(interpretation)
    pos_ratio = round((polarity + 1) / 2, 2) * 100
    neg_ratio = 100 - pos_ratio

    st.subheader("📊 Sentiment Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Sentiment", sentiment)
        st.metric("Polarity Score", f"{polarity:.2f}")
    with col2:
        plot_pie(pos_ratio, neg_ratio)
        plot_bar(pos_ratio, neg_ratio)

from utils.gemini_api import generate_interpretation

# Later in app.py
interpretation = generate_interpretation(user_input, matched_symbol_text)
