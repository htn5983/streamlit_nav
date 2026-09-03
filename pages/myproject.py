import streamlit as st

st.title("專案首頁")

with st.sidebar:
    st.page_link(st.Page("pages/project1.py" ), label="財經分析專題" )
    st.page_link("pages/project2.py" , label="市場調查專題" )
    st.page_link(st.Page("pages/projmembers.py"), label="專案成員", icon="🐷" )
    st.page_link("https://github.com/htn5983" , label="github其他專題",icon=":material/merge:" )