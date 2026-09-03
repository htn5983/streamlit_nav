import streamlit as st


pageList=[
    st.Page("pages/home.py", title="首頁"),
    st.Page("pages/mycv.py", title="我的履歷"),
    st.Page("pages/myproject.py", title="執行專案")
]
# st.navigation 建立後回傳一個 pages 物件 , 並不會直接執行
pgnav = st.navigation(
    pages=pageList,
    position="top"
    )

# 呼叫 pages 物件的 run() 方法 , 會依照使用者選擇的頁面 , 執行對應的程式碼
pgnav.run()