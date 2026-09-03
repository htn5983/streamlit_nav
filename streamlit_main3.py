import streamlit as st

menuList={
    "功能A":[
        st.Page("pages/home.py",title="首頁",icon=":material/home:"),
        st.Page("pages/mycv.py",title="我的履歷",icon=":material/assignment_ind:"),
        ],
    "功能B":[
        st.Page("pages/project1.py",title="執行專案1"),
        st.Page("pages/project2.py",title="執行專案2"),
        st.Page("pages/myproject.py",title="執行專案"),
        st.Page("https://htn5983.github.io/myproject/",title="我的GitHub.io專案"),
        st.Page("https://github.com/htn5983/",title="GitHub其他專案")
        ]
}

pageList=[
    st.Page("pages/home.py" , title="Home" ),
    st.Page("pages/mycv.py" , title="我的履歷" ),   
    st.Page("pages/myproject.py" , title="執行專案")    
]

# st.navigation 建立後回傳一個 pages 物件 , 並不會直接執行
pgnav = st.navigation(
    pages=menuList,
    position="top"
    )

# 呼叫 pages 物件的 run() 方法 , 會依照使用者選擇的頁面 , 執行對應的程式碼
pgnav.run()