import streamlit as st

# st.navigation 建立後回傳一個 pages 物件 , 並不會直接執行
# pgnav = st.navigation(
#     pages=[st.Page("pages/home.py", title="首頁")],
#     position="sidebar"
#     )

pgnav = st.navigation(
    pages=["pages/home.py", "pages/mycv.py", "pages/myproject.py"],
    position="top"
)

# 呼叫 pages 物件的 run() 方法 , 會依照使用者選擇的頁面 , 執行對應的程式碼
pgnav.run()