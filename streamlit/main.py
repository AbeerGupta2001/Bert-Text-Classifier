


import streamlit as st

model = st.Page(
    "app.py", title="Model", icon=":material/thumb_up:",
)
hello = st.Page("hello.py",title="Introduction",icon=":material/thumb_up:", default=True)

pg = st.navigation([hello,model])
pg.run()