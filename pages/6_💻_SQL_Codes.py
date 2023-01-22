# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Glossory - Terra Price Run Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('💻Codes')

st.write(""" ## Flipside SQL Codes ## """)
# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.write("""    In this Dashboard data frames are gathered  from comprehensive Data Base [Flipside Crypto](https://flipsidecrypto.xyz/earn).

At the following links, you can find the SQL codes that are used in this dashboard: 

""")

# SQL Codes
st.write("""
1. https://app.flipsidecrypto.com/velocity/queries/99e2c787-f6d5-47cd-b1af-a83212cc505a
2. https://app.flipsidecrypto.com/velocity/queries/64d79e08-ef94-475f-a4ad-f9e476044fbe
3. https://app.flipsidecrypto.com/velocity/queries/070d0011-42bc-465c-896f-d1a3f269e7d2
4. https://app.flipsidecrypto.com/velocity/queries/f72e63a1-d9bd-43ba-9d91-6ade2d06d463
5. https://app.flipsidecrypto.com/velocity/queries/04c3d251-69c5-4072-ab59-d026783a3bbd
6. https://app.flipsidecrypto.com/velocity/queries/42255f26-2dea-44e0-ad7f-0e2a3108f6fc
7. https://app.flipsidecrypto.com/velocity/queries/d124f6e9-6a76-4a84-bbfc-8cef231add75
8. https://app.flipsidecrypto.com/velocity/queries/54c4f0e2-95b1-4720-b54d-c1352bd68381
9. https://app.flipsidecrypto.com/velocity/queries/a23a11a3-4fc4-4297-ab8b-9b2800f9a3e9
10. https://app.flipsidecrypto.com/velocity/queries/8f1d8254-2387-4631-ab6d-6f487c5187e3


""")
