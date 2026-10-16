import joblib
import streamlit as st

st.set_page_config(page_title="SMS Spam Detector", page_icon="📩")

@st.cache_resource
def load():
    return joblib.load("spam_model.joblib")

bundle = load()
model, threshold = bundle["model"], bundle["threshold"]

st.title("📩 SMS Spam Detector")
st.write("Type or paste an SMS message to check whether it is spam.")

text = st.text_area("Message", height=140, placeholder="e.g. Congratulations! You won a free prize...")

if st.button("Check Message"):
    if not text.strip():
        st.warning("Please enter a message.")
    else:
        prob = float(model.predict_proba([text])[0][1])
        if prob >= threshold:
            st.error(f"🚫 SPAM  (spam probability: {prob:.1%})")
        else:
            st.success(f"✅ HAM – genuine message  (spam probability: {prob:.1%})")
        st.progress(min(prob, 1.0))