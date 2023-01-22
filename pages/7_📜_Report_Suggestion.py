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
st.write("""  ## Former Weekly Reports ##   """)
st.text(" \n")
st.write("""  ##### Contracts on NEAR are simply programs stored on a blockchain that run when predetermined conditions are met. The Daily Number of New Contracts is a valuable metric for understanding the health and growth of an ecosystem.

##### The more active contracts there are, the more projects are actively engaging with the NEAR protocol. The chart below shows a cyclical rhythm to new contracts, with rises and falls. Over the last seven days, the number of new contracts reached a daily high of 54 on December 4, and a weekly low of 27 on December 6. This range is broader compared to the week before, with last week’s highest number of 44 on November 30, to a low of 12 new contracts on November 27.   """)


st.image(Image.open('Images/Dec23Trend.jpg'))

st.header("""  Contracts on NEAR are simply programs stored on a blockchain that run when predetermined conditions are met. The Daily Number of New Contracts is a valuable metric for understanding the health and growth of an ecosystem.

##### The more active contracts there are, the more projects are actively engaging with the NEAR protocol. The chart below shows a cyclical rhythm to new contracts, with rises and falls. Over the last seven days, the number of new contracts reached a daily high of 54 on December 4, and a weekly low of 27 on December 6. This range is broader compared to the week before, with last week’s highest number of 44 on November 30, to a low of 12 new contracts on November 27.   """)

st.image(Image.open('Images/Dec23Trend.jpg'))
