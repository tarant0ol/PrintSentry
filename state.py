import streamlit as st


@st.cache_resource
def get_global_state():
    return {
        "Task" : 1,
        "Stage": 1,
    }