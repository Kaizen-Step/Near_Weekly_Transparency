# Libraries
import streamlit as st
from PIL import Image

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Report Suggestion - Near Weekly Transprancy Report',
                   page_icon=':bar_chart:', layout='wide')
st.title('📜Report Suggestion')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.text(" \n")
st.write("""  ## Last Weekly Reports ##   """)
st.text(" \n")
st.write(""" In this section we reviewed last weekly transparemcy report and tried to share some opinion that might help to improve the overall report.   """)


st.text(" \n")
st.write("""  ### Static Charts with Lack of Attention to Details ##   """)
st.text(" \n")

st.write("""  Almost in all Weekly transparency reports, there are static charts with no Y and X axis titles; it is better to use the date axis with the name of the week when weekly charts are presented. There are a few charts that the date on them are not suited for the report, like (the November 25, 2022-Daily Number of New Accounts chart) as you can see below the charts only cover the last days of October and the first couple of days of November while the report and the context were about 25th of November. 
   """)

st.image(Image.open('Images/25_November_Date.png'))

st.write(""" Additionally, the transaction charts pertaining to December 16 are missing.
   """)

st.image(Image.open('Images/16December_Missing_Chart.jpg'))

st.write("""  Repeating the same sentences in a couple of reports is not bad at all (we actually did it in our report), but when using Q3 information in the last week of Q4 with wrong info, I guess it is not appropriate.
   """)

st.image(Image.open('Images/2December_Same_Sentence.jpg'))

st.image(Image.open('Images/December9_same_sentence.jpg'))


st.write("""  We are not trying to be pedants who are seeking small details, just as users who try to find a weekly pattern in a couple of consecutive reports. We just notice these small things at first glance. And we believe these are not bad to share with you.

   """)
