import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_summsrizer();
  return pipeline("summerization",model="sshleifer/distilbart-can-12-6")
