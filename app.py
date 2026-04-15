import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_summsrizer();
  return pipeline("summerization",model="sshleifer/distilbart-can-12-6")
 
  
  summarizer=load_summarizer()
  st.title("ai text summarizer")
  st.write("enter a long text below,and get a concise summary!")
  long_text=st.text_area("enter text to summarize:",height=200)
  summarizer = load_summarize()

# Summary Parameters
max_length = st.slider("Max Summary Length", min_value=50, max_value=300, value=130)
min_length = st.slider("Min Summary Length", min_value=20, max_value=100, value=30)

# Summarize Button
if st.button("Summarize"):
    if long_text:
        summary = summarizer(long_text, max_length=max_length, min_length=min_length, do_sample=False)
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text!")
  
