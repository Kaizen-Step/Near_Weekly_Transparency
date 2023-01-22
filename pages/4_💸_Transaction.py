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
st.set_page_config(page_title='Transactions - Near Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('💸Transactions')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'NearWeeklyTransparency_Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/42255f26-2dea-44e0-ad7f-0e2a3108f6fc/data/latest')
    elif query == 'NEAR_TX3':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d124f6e9-6a76-4a84-bbfc-8cef231add75/data/latest')
    elif query == 'Near_TX_Interval':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/54c4f0e2-95b1-4720-b54d-c1352bd68381/data/latest')
    return None


NearWeeklyTransparency_Transactions = get_data(
    'NearWeeklyTransparency_Transactions')
NEAR_TX3 = get_data('NEAR_TX3')
Near_TX_Interval = get_data('Near_TX_Interval')

st.text(" \n")
st.write("""  ## Daily Transactions ##   """)
st.text(" \n")
st.write("""  The daily number of transactions is a record of how many times the blockchain logged a transaction. This week’s data represents a healthy increase in the number of transactions. From lows of 254,700 transactions on January 1st, to a weekly high of 635,095 transactions per day on January 12. Looking more broadly, NEAR transaction activity has been trending upward in this period.   """)

df11 = NearWeeklyTransparency_Transactions
df2 = NEAR_TX3
df3 = Near_TX_Interval


# Daily Transactions with Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df11["DAY"], y=df11["TOTAL_TRANSACTIONS_OVER_TIME"],
                     name='Daily Transaction'), secondary_y=False)
fig.add_trace(go.Line(x=df11["DAY"], y=df11["CUMULATIVE_TRANSACTIONS_DAILY"],
                      name='CUMULATIVE Transactions'), secondary_y=True)
fig.update_layout(
    title_text='Daily Transactions with Cumulative Value')
fig.update_yaxes(
    title_text='Daily Transaction', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write("""  On weekly charts also there is a significant rise in weekly transactions during December 16, 2022 to Januaru 16, 2023 and almost tripled in this period.  """)


# Weekly Transaction with Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df11["WEEK"], y=df11["TOTAL_TRANSACTIONS_OVER_TIME"],
                     name='Weekly Transaction'), secondary_y=False)
fig.add_trace(go.Line(x=df11["WEEK"], y=df11["CUMULATIVE_BLOCK_WEEKLY"],
                      name='CUMULATIVE Transactions'), secondary_y=True)
fig.update_layout(
    title_text='Weekly Transactions with Cumulative Value')
fig.update_yaxes(
    title_text='Weekly Transaction', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
