import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_summsrizer();
  return pipeline("summerization",model="sshleifer/distilbart-can-12-6")
 
  
  summarizer=load_summarizer()
  st.title("ai text summarizer")
  st.write("enter a long text below,and get a concise summary!")
  long_text=st.text_area("enter text to summarize:",height=200)
  
