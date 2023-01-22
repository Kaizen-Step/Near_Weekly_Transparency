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
st.set_page_config(page_title='Contracts - Near Weekly Transparency Report',
                   page_icon=':bar_chart:', layout='wide')
st.title('🌌Contracts')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'NearWeeklyTransparency_Daily_Contract':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f72e63a1-d9bd-43ba-9d91-6ade2d06d463/data/latest')
    elif query == 'NearWeeklyTransparency_Weekly_Contract':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/04c3d251-69c5-4072-ab59-d026783a3bbd/data/latest')
    elif query == 'Near_TopContracts_Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7893cc65-c539-435e-b7e3-36aaa926db27/data/latest')
    elif query == 'Near_TopNew_Fee':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/786bee4c-7f76-4bcf-a690-01071a24d40b/data/latest')
    elif query == 'NearTop10Contracts_Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/1e7ec242-f80e-4075-b30a-7432ec3cc266/data/latest')
    elif query == 'NearTop_newcontracts_fee':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3861369a-98db-4743-a531-2db1860d5cc8/data/latest')
    elif query == 'NearWeekly_TopContracts_users':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4651d25e-65b6-4fbe-bac1-843c86f093ca/data/latest')
    return None


NearWeeklyTransparency_Daily_Contract = get_data(
    'NearWeeklyTransparency_Daily_Contract')
NearWeeklyTransparency_Weekly_Contract = get_data(
    'NearWeeklyTransparency_Weekly_Contract')


Near_Dev_New_contracts = get_data('Near_Dev_New_contracts')
Near_DevTopnew_weekly_transactions = get_data(
    'Near_DevTopnew_weekly_transactions')
Near_TopContracts_Transactions = get_data('Near_TopContracts_Transactions')
Near_TopNew_Fee = get_data('Near_TopNew_Fee')
NearTop10Contracts_Transactions = get_data('NearTop10Contracts_Transactions')
NearTop_newcontracts_fee = get_data('NearTop_newcontracts_fee')
NearWeekly_TopContracts_users = get_data('NearWeekly_TopContracts_users')

st.text(" \n")
st.write("""  ## New Contracts and Active Contracts ##   """)
st.text(" \n")
st.write("""   Contracts on NEAR are simply programs stored on a blockchain that run when predetermined conditions are met. The Daily Number of New Contracts is a valuable metric for understanding the health and growth of an ecosystem.

 The more active contracts there are, the more projects are actively engaging with the NEAR protocol. The chart below shows a cyclical rhythm to new contracts, with rises and falls. Over the last 30 days(16 December 2022-16 January 2023), the number of new contracts reached a daily high of 16 on December 20, and a low of 1 on January Second. This range is narrower compared to the first two weeks of December, with the highest number of 54 on December 4, to a low of 27 new contracts on December 6.  """)

df11 = NearWeeklyTransparency_Daily_Contract
df12 = NearWeeklyTransparency_Weekly_Contract


df = Near_Dev_New_contracts
df2 = Near_DevTopnew_weekly_transactions
df3 = Near_TopContracts_Transactions
df4 = Near_TopNew_Fee
df5 = NearTop10Contracts_Transactions
df6 = NearTop_newcontracts_fee
df7 = NearWeekly_TopContracts_users


# Daily New Contracts + Cumulative Number
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df11["DATE"], y=df11["NEW_CONTRACTS"],
                     name='NEW Contracts'), secondary_y=False)
fig.add_trace(go.Line(x=df11["DATE"], y=df11["CUM_NEW_CONTRACTS"],
                      name='CUMULATIVE NEW Contracts'), secondary_y=True)
fig.update_layout(
    title_text='Daily New Contracts With Cumulative Value')
fig.update_yaxes(
    title_text='Number of NEW Contracts', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Value', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.text(" \n")
st.write(""" Smart contracts created on NEAR are programs stored on a blockchain that run when predetermined conditions are met. As you can see in the above chart, during this period, the Weekly number of New Contracts has been trending downward; however, since the new year, the upward trend has started. In this period, A low of 23 New weekly Contracts was measured on December 25th, while it had been rosen to 47 on Week started from jan 9.   
 """)

# Weekly New Contracts + Cumulative Number
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df12["DATE"], y=df12["NEW_CONTRACTS"],
                     name='NEW Contracts'), secondary_y=False)
fig.add_trace(go.Line(x=df12["DATE"], y=df12["CUM_NEW_CONTRACTS"],
                      name='CUMULATIVE NEW Contracts'), secondary_y=True)
fig.update_layout(
    title_text='Weekly New Contracts With Cumulative Value')
fig.update_yaxes(
    title_text='Number of NEW Contracts', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Value', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.text(" \n")
st.write("""  ## Active Contracts ##   """)
st.text(" \n")
st.write("""   Active contracts is a measure of contracts that execute in a 24 hour period. This number has remained realitively consistent throughout the last 4 week with an average of 692 active contracts on the NEAR network. In this period, Firs day of 2023 year figure is the lowest Number with 357 Active contract, while that for January 9 is highest number with 744.

  """)


# Daily Active Contracts + Cum Number
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df11["DATE"], y=df11["ACTIVE_CONTRACTS"],
                     name='Number of Active Contracs'), secondary_y=False)
fig.add_trace(go.Line(x=df11["DATE"], y=df11["CUM_CONTRACTS"],
                      name='CUMULATIVE ACTIVE Contracts'.title()), secondary_y=True)
fig.update_layout(
    title_text='Daily Active Contracts With Cumulative Value')
fig.update_yaxes(
    title_text='Number of ACTIVE Contracts', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Active Contracts', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.text(" \n")
st.write("""   In Weekly chart Active contracts flactuated over this period and remain relatively unchanged.
  """)
# Weekly Active Contracts + Cumulative Number
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df12["DATE"], y=df12["ACTIVE_CONTRACTS"],
                     name='Number of Active Contracts'), secondary_y=False)
fig.add_trace(go.Line(x=df12["DATE"], y=df12["CUM_CONTRACTS"],
                      name='CUMULATIVE ACTIVE Contracts'.title()), secondary_y=True)
fig.update_layout(
    title_text='Weekly Active Contracts With Cumulative Value')
fig.update_yaxes(
    title_text='Number of ACTIVE Contracts', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Active Contracts', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.text(" \n")
st.text(" \n")
st.text(" \n")
st.subheader('Overall Contract Metrics')

# Top new contracts Based on average transactions fee
fig = px.area(df6, x="DATE", y="AVG_TX_FEE", color="TX_RECEIVER",
              title='Top new contracts Based on average transactions fee')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='AVG TX Fee')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Top New Contracts Based on Total Transactions Fee
fig = px.bar(df4, x="TX_RECEIVER", y="TOTAL_TX_FEE", color="TX_RECEIVER",
             title='Top New Contracts Based on Total Transactions Fee')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="TOTAL TX FEE".title())
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Top Contracts Based on Transactions
fig = px.bar(df3.sort_values(["DATE", "COUNT"], ascending=[
    True, False]), x="DATE", y="COUNT", color="CONTRACT", title='Weekly Top Contracts Based on Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Transactions')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Top Contracts Based on users
fig = px.bar(df7.sort_values(["DATE", "USERS"], ascending=[
    True, False]), x="DATE", y="USERS", color="CONTRACT", title='Weekly Top Contracts Based on Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Transactions')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Most popular Contracts Based on Transactions
fig = px.pie(df3, values="COUNT",
             names="CONTRACT", title='Most popular Contracts Based on Transactions')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Most popular Contract based on users
fig = px.pie(df7, values="USERS",
             names="CONTRACT", title='Most popular Contract based on users')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Near Dev- Top 10 Contracts Based on Transactions
fig = px.bar(df5, x="CONTRACT_ADDRESS", y="TRANSACTIONS", color="CONTRACT_ADDRESS",
             title='Top 10 Contracts Based on Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="TRANSACTIONS".title())
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
