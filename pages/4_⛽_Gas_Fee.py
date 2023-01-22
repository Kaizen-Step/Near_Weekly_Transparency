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
st.set_page_config(page_title='Supply - Nera Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('⛽Gas Fee')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'NearWeeklyTransparency_Transactions_GasFee':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/42255f26-2dea-44e0-ad7f-0e2a3108f6fc/data/latest')
    elif query == 'NEAR_Top10Validator':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/182bf73e-da3c-4b88-99f1-99e8112dd5f7/data/latest')
    elif query == 'NEAR_supply_richest':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a9de75ce-2ed2-4394-ba02-55921a2b9aa0/data/latest')
    elif query == 'NEAR_Balance_Range':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/070d0011-42bc-465c-896f-d1a3f269e7d2/data/latest')
    elif query == 'TopPools_Volume':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8278c04b-2bc6-4e69-aa80-52d07c7b56cf/data/latest')
    elif query == 'TopPools_Users':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2679458f-3d70-4a6e-a663-8a36d63b93e8/data/latest')
    elif query == 'TopPools_Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ef654823-0f63-4d45-aa43-43a1eafdf43e/data/latest')
    elif query == 'top10_Deligatorsvolume':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/965c0a8e-6700-430c-bbde-11f206754323/data/latest')
    elif query == 'top10_DeligatorsTX':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/908d7341-4b41-48cb-b31c-3f0e6f292050/data/latest')
    return None


NearWeeklyTransparency_Transactions_GasFee = get_data(
    'NearWeeklyTransparency_Transactions_GasFee')

NEAR_supplystaking1 = get_data('NEAR_supplystaking1')
NEAR_Top10Validator = get_data('NEAR_Top10Validator')
NEAR_supply_richest = get_data('NEAR_supply_richest')
NEAR_Balance_Range = get_data('NEAR_Balance_Range')
TopPools_Volume = get_data('TopPools_Volume')
TopPools_Users = get_data('TopPools_Users')
TopPools_Transactions = get_data('TopPools_Transactions')
top10_Deligatorsvolume = get_data('top10_Deligatorsvolume')
top10_DeligatorsTX = get_data('top10_DeligatorsTX')

st.text(" \n")
st.write("""  ## Used Gas and Gas Fee ##   """)
st.text(" \n")
st.write("""  Gas Fees is a term used to describe the cost of making transactions on the NEAR network. These fees are paid to validators for the network services they provide to the NEAR blockchain. Gas fees incentivize validators to secure the network. 

In the last week, Used Gas on NEAR (PetaGas) was measured at a high of 7,569 on December 11th and 6,758 on the 14th. To learn more about Gas on NEAR, check out the NEAR White Paper. (Rises in gas used can be attributed to many factors, with a common one being increased user activity on the NEAR network.) 


   """)

df11 = NearWeeklyTransparency_Transactions_GasFee
df = NEAR_supplystaking1
df2 = NEAR_Top10Validator
df3 = NEAR_supply_richest
df4 = NEAR_Balance_Range
df5 = TopPools_Volume
df6 = TopPools_Users
df7 = TopPools_Transactions
df8 = top10_Deligatorsvolume
df9 = top10_DeligatorsTX

# Daily Gas Fees with Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df11["DAY"], y=df11["TOTAL_FEES_OVER_TIME"],
                     name='Daily Fee'), secondary_y=False)
fig.add_trace(go.Line(x=df11["DAY"], y=df11["CUMULATIVE_FEE_DAILY"],
                      name='CUMULATIVE Fee'), secondary_y=True)
fig.update_layout(
    title_text='Daily Gas Fees with Cumulative Value')
fig.update_yaxes(
    title_text='Daily Gas Fee', secondary_y=False)
fig.update_yaxes(title_text='Cumulative Fee', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write("""  Over the last week, there has been a slight drop in the Gas Fee (in NEAR), which correlates with a drop in Used Gas. On December 11th, the Gas Fee was measured at 756, before falling to 675 on the 14th. 


   """)


# Weekly Gas Fees with Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df11["WEEK"], y=df11["TOTAL_FEES_OVER_TIME"],
                     name='Weekly Fee'), secondary_y=False)
fig.add_trace(go.Line(x=df11["WEEK"], y=df11["CUMULATIVE_FEE_WEEKLY"],
                      name='CUMULATIVE Fee'), secondary_y=True)
fig.update_layout(
    title_text='Weekly Gas Fees with Cumulative Value')
fig.update_yaxes(
    title_text='Weekly Gas Fee', secondary_y=False)
fig.update_yaxes(title_text='Cumulative Fee', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
