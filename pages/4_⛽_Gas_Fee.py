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
st.write("""  ##### Gas Fees are a catch all term for the cost of making transactions on the NEAR network. These fees are paid to validators for their services to the blockchain. Without these fees, there would be no incentive for anyone to keep the network secure.

##### Over the last week, the daily amount of gas, expressed here as PetaGas, which is the equivalent of 0.1 $NEAR, has maintained a fairly consistent value between 5,949 PetaGas and 6,743 PetaGas. To learn more about Gas on NEAR, there is an excellent explainer in the NEAR White Paper. Compared with last week, the Daily Amount of Used Gas has decreased, from highs of more than 8,000 PetaGas.

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

# Daily net stake volume
fig = px.bar(df.sort_values(["DATE_STAKE", "DAILY_NET"], ascending=[
             True, False]), x="DATE_STAKE", y="DAILY_NET", title='Daily net stake volume'.title())
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="DAILY NET")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Stake volume and With cumulative stake volume
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE_STAKE"], y=df["NEAR Staked"],
                     name="NEAR Staked".title()), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE_STAKE"], y=df["TOTAL_STAKED"],
                      name="TOTAL STAKED".title()), secondary_y=True)
fig.update_layout(
    title_text='Stake volume and With cumulative stake volume')
fig.update_yaxes(
    title_text="NEAR Staked".title(), secondary_y=False)
fig.update_yaxes(title_text="TOTAL STAKED".title(),
                 secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily stakers vs Unstakers
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE_STAKE"], y=df["Stakers"],
                     name="Stakers".title()), secondary_y=False)
fig.add_trace(go.Bar(x=df["DATE_STAKE"], y=df["Unstakers"],
                     name="Unstakers".title()), secondary_y=False)
fig.update_layout(
    title_text='Daily stakers vs Unstakers')
fig.update_yaxes(
    title_text="Stakers".title(), secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Near stake vs Unstake
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE_STAKE"], y=df["NEAR Staked"],
                     name="NEAR Staked".title()), secondary_y=False)
fig.add_trace(go.Bar(x=df["DATE_STAKE"], y=df["NEAR Unstaked"],
                     name="NEAR Unstaked".title()), secondary_y=False)
fig.update_layout(
    title_text='Near stake vs Unstake')
fig.update_yaxes(
    title_text="Stakers".title(), secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Stake vs Unstake Volume per User
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE_STAKE"], y=df["Stake Volume per User"],
                     name="Stake Volume per User".title()), secondary_y=False)
fig.add_trace(go.Bar(x=df["DATE_STAKE"], y=df["Unstake Volume per User"],
                     name="Unstake Volume per User".title()), secondary_y=False)
fig.update_layout(
    title_text='Stake vs Unstake Volume per User')
fig.update_yaxes(
    title_text="Stake Volume per User".title(), secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Stake vs Unstake Transactions per User
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE_STAKE"], y=df["Stake Transactions per User"],
                     name="Stake Transactions per User".title()), secondary_y=False)
fig.add_trace(go.Bar(x=df["DATE_STAKE"], y=df["Unstake Transactions per User"],
                     name="Unstake Transactions per User".title()), secondary_y=False)
fig.update_layout(
    title_text='Stake vs Unstake Transactions per User')
fig.update_yaxes(
    title_text="Stake Transactions per User".title(), secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.text(" \n")
st.text(" \n")
st.text(" \n")
st.subheader('Pool & Validators')

# Weekly Top Pools Based on Volume
fig = px.bar(df5.sort_values(["DATE", "Volume"], ascending=[
    True, False]), x="DATE", y="Volume", color="Pool name", title='Weekly Top Pools Based on Volume')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Volume")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Top Pools Based on Users
fig = px.bar(df6.sort_values(["DATE", "Unique wallet"], ascending=[
    True, False]), x="DATE", y="Unique wallet", color="Pool name", title='Weekly Top Pools Based on Users')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Unique wallet")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Top Pools Based on Transactions
fig = px.bar(df7.sort_values(["DATE", "tx count"], ascending=[
    True, False]), x="DATE", y="tx count", color="Pool name", title='Weekly Top Pools Based on Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="tx count")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Top 10 Validator
fig = px.bar(df2, x="VALODATOR", y="AMOUNT",
             color="VALODATOR", title='Top 10 Validator')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Validator')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Top 10 Delegator Based on Volume
fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
fig.add_trace(go.Bar(x=df8["STAKERS"], y=df8["AMOUNT"],
                     name='Volume'), secondary_y=False)
fig.update_layout(title_text='Top 10 Delegator Based on Volume'.title())
fig.update_yaxes(title_text='Volume', secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Top 10 Delegator Based on Transactions
fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
fig.add_trace(go.Bar(x=df9["STAKERS"], y=df9["STAKES"],
                     name="STAKES"), secondary_y=False)
fig.update_layout(title_text='Top 10 Delegator Based on Transactions'.title())
fig.update_yaxes(title_text="STAKES", secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
