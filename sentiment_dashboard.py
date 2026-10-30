import streamlit as st

st.set_page_config(page_title="AI Sentiment Dashboard", page_icon="📊", layout="wide")

st.title("📊 AI Sentiment & Customer Feedback Analyzer")
st.markdown("Developed by **Rabia Khan** | Python & AI Developer")
st.write("Analyze customer reviews and feedback instantly using rule-based and AI sentiment evaluation.")

feedback = st.text_area("Paste customer review or feedback here:", height=150, placeholder="This app is amazing and works like magic!")

if st.button("Analyze Sentiment"):
    if feedback.strip() == "":
        st.warning("Please enter some feedback text.")
    else:
        text_lower = feedback.lower()
        if any(word in text_lower for word in ["amazing", "great", "love", "awesome", "best", "fantastic"]):
            sentiment = "Positive 🌟"
            st.success(f"Sentiment Result: {sentiment}")
            st.balloons()
        elif any(word in text_lower for word in ["bad", "poor", "worst", "hate", "terrible", "slow"]):
            sentiment = "Negative ⚠️"
            st.error(f"Sentiment Result: {sentiment}")
        else:
            sentiment = "Neutral ℹ️"
            st.info(f"Sentiment Result: {sentiment}")
