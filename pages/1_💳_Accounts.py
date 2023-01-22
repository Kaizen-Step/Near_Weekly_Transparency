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
st.set_page_config(page_title='Accounts - Near Weekly Transprancy Report',
                   page_icon=':bar_chart:', layout='wide')
st.title('💳Accounts')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'NearWeeklyTransparency_DailyAccount':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/99e2c787-f6d5-47cd-b1af-a83212cc505a/data/latest')
    elif query == 'NearWeeklyTransparency_WeeklyAccount':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/64d79e08-ef94-475f-a4ad-f9e476044fbe/data/latest')
    elif query == 'NEAR_Balance_Range':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/070d0011-42bc-465c-896f-d1a3f269e7d2/data/latest')
    return None


NearWeeklyTransparency_DailyAccount = get_data(
    'NearWeeklyTransparency_DailyAccount')
NearWeeklyTransparency_WeeklyAccount = get_data(
    'NearWeeklyTransparency_WeeklyAccount')

NEAR_Wallet1 = get_data('NEAR_Wallet1')
NEAR_supply_richest = get_data('NEAR_supply_richest')
NEAR_Balance_Range = get_data('NEAR_Balance_Range')

st.text(" \n")
st.write("""  ## New Accounts and Active Accounts ##   """)
st.text(" \n")
st.write("""  New Accounts are new wallets being created on the NEAR blockchain. In almost all days of December and the first days of January, the daily number of new accounts had been declining. This week (9-16_Jan;) however, activity has been enormously trending up, with the average number of new accounts 23,000 per day, which is almost three times higher than the last week's average (8,420), with a weekly peak of 38,185 recorded on January 13.

 This is down on November’s figure of 24,000 wallets per 24 hours, on average, but it could be a good start for 2023. Put into context, roughly 14,300 wallets were being created daily at the start of December, and less than 10,000 daily for the last two weeks shows how significant this rise is.

 Looking more broadly, the peak for account creation in Q3 was September 13, 2022, where 130,000 new wallets were created in one day, and this week's peak of 38,185 is not a full potential, and surely brighter days will be ahead.  
  


    """)

df11 = NearWeeklyTransparency_DailyAccount
df12 = NearWeeklyTransparency_WeeklyAccount


df = NEAR_Wallet1
df3 = NEAR_supply_richest
df4 = NEAR_Balance_Range


# Daily New Wallets + Cumulative Number
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df11["DAY"], y=df11['NEW_WALLETS'],
                     name='NEW Accounts'), secondary_y=False)
fig.add_trace(go.Line(x=df11["DAY"], y=df11['CUMULATIVE_NEW_WALLET'],
                      name='CUMULATIVE NEW Accounts'), secondary_y=True)
fig.update_layout(
    title_text='Daily New Accounts With Cumulative Value')
fig.update_yaxes(
    title_text='Number of NEW Accounts', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Value', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly New Wallets + Cumulative Number
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df12["WEEK"], y=df12['NEW_WALLETS'],
                     name='NEW Accounts'), secondary_y=False)
fig.add_trace(go.Line(x=df12["WEEK"], y=df12['CUMULATIVE_NEW_WALLET'],
                      name='CUMULATIVE NEW Accounts'), secondary_y=True)
fig.update_layout(
    title_text='Weekly New Accounts With Cumulative Value')
fig.update_yaxes(
    title_text='Number of NEW Accounts', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Value', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.text(" \n")
st.write("""  ## Active Accounts ##   """)
st.text(" \n")

st.write("""  If a NEAR wallet makes an on-chain transaction, it’s counted in the Daily Number of Active Accounts metric. This past week, Daily Active Accounts ranged between 352,147 on January 9th to 635,095 on the 12th of the month.Over the last week, despite an enormouse rise, after hiting a high of 635,095 Active Accounts trending down to about 399,501 on January 15. 



    """)


# Daily Active Wallets + Cumulative Number
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df11["DAY"], y=df11["ACTIVE_WALLETS"],
                     name='Number of Active Accounts'), secondary_y=False)
fig.add_trace(go.Line(x=df11["DAY"], y=df11["CUMULATIVE_ACTIVE_WALLET"],
                      name='CUMULATIVE ACTIVE Accounts'.title()), secondary_y=True)
fig.update_layout(
    title_text='Daily Active Accounts With Cumulative Value')
fig.update_yaxes(
    title_text='Number of ACTIVE Accounts', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Active Accounts', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write("""  As you can see in the below weekly chart the Monthly downtrend was breaked and new uprising trend was started by the new year.
The Number of Weekly Active Accounts rise more than 70 percent in one week from 2.15m in first week of 2023 to 3.53m in the second week of Jan 2023.



    """)


# Weekly Active Wallets + Cumulative Number
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df12["WEEK"], y=df12["ACTIVE_WALLETS"],
                     name='Number of Active Accounts'), secondary_y=False)
fig.add_trace(go.Line(x=df12["WEEK"], y=df12["CUMULATIVE_ACTIVE_WALLET"],
                      name='CUMULATIVE ACTIVE Accounts'.title()), secondary_y=True)
fig.update_layout(
    title_text='Weekly Active Accounts With Cumulative Value')
fig.update_yaxes(
    title_text='Number of ACTIVE Accounts', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Active Accounts', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
