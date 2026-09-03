import streamlit as st
import time

st.page_link("pages/myproject.py", label="回專案首頁", icon=":material/arrow_back:")

if st.button("返回專案首頁2"):
    st.switch_page("pages/myproject.py")

st.title("股票財經分析專題")
st.divider()

st.subheader("三秒後返回專案主畫面")

st.write("三秒後呼叫 st.switch_page() , 會依照使用者選擇的頁面 , 執行對應的程式碼")
st.code("""
time.sleep(3)
st.switch_page("pages/myproject.py")
""")

time.sleep(3)
st.switch_page("pages/myproject.py")