# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Near Weekly Tranparency Report',
                   page_icon=':bar_chart:', layout='wide')
st.title('Near Weekly Tranparency Report')

# Content
c1, c2, c3, c4 = st.columns(4)
c4.image(Image.open('Images/near-logo.png'))


with c1:
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")

    st.write("""  # ♾️Near (Transparency) #   """)
st.write("""

NEAR Protocol is software that aims to incentivize a network of computers to operate a platform for developers to create and launch decentralized applications.  
Central to NEAR Protocol’s design is the concept of sharding, a process that aims to split the network’s infrastructure into several segments in order for computers, also known as nodes, to only have to handle a fraction of the network’s transactions.  
By distributing segments of the blockchain, rather than the complete blockchain across network participants, sharding is expected to create a more efficient way to retrieve network data and scale the platform.  
NEAR operates in a similar manner to other centralized data storage systems like Amazon Web Services (AWS) that serve as the base layer on which applications are built. But rather than being run by a single entity, NEAR is operated and maintained by a distributed network of computers.  
Just as AWS allows developers to deploy code in the cloud without needing to create their own infrastructure, NEAR Protocol facilitates a similar architecture built around a network of computers and its native cryptocurrency, the NEAR token.  

### The Importance of Transparency ###
  
The NEAR Foundation has been committed to transparency since its inception. It values openness to all stakeholders, including investors, builders, and creators. The Foundation’s focus on openness to the entire community will always be a core tenet.    
The Foundation values the community’s continued support and feedback as it publishes these reports. It’s part of the Foundation’s ongoing response to the community to provide as much transparency as possible.
In recent months, in response to community frustration, the Foundation has endeavored to do more.   
**NEAR’s mission is to:**   
**"Remove every barrier for Web3 creators, by creating an ecosystem that is uniquely simple, safe, scalable, and sustainable"**.  
Openness to the community, investors, builders, and creators is one of the core tenets of being a Web3 project.   
This NEAR Weekly On-Chain Data Report is just one of the ways in which the Foundation is being more proactively transparent. """)


st.text(" \n")
st.text(" \n")
st.write("""
  
List of Transparency Reports since September 11, 2022 (first anniversary ):

1.&nbsp; A Year on NEAR &nbsp;&nbsp;&nbsp;                      [Yearly] &nbsp;&nbsp;    (September 11, 2022)  
2.&nbsp; NEAR Foundation Transparency Report &nbsp;&nbsp;&nbsp; [Quarterly] &nbsp;&nbsp;  (September 12, 2022)  
3.&nbsp; Refer-and-Earn 2022 Q2 Report &nbsp;&nbsp;&nbsp;       [Quarterly]&nbsp;&nbsp; (October 12, 2022)  
4.&nbsp; NEAR Transparency Report  &nbsp;&nbsp;&nbsp;           [Weekly]  &nbsp;&nbsp;   (November 21, 2022)  
5.&nbsp; NEAR Foundation Funding Team Report&nbsp;&nbsp;&nbsp;  [Monthly]  &nbsp;&nbsp;  (November 23, 2022)  
6.&nbsp; NEAR Transparency Report   &nbsp;&nbsp;&nbsp;          [Weekly]  &nbsp;&nbsp;   (November 25, 2022)  
7.&nbsp; NEAR Transparency Report     &nbsp;&nbsp;&nbsp;        [Weekly]  &nbsp;&nbsp;   (December 2, 2022)  
8.&nbsp; NEAR Weekly On Chain Data Report &nbsp;&nbsp;&nbsp;    [Weekly] &nbsp;&nbsp;    (December 9, 2022)  
9.&nbsp; NEAR Weekly On-Chain Data Report &nbsp;&nbsp;&nbsp;    [Weekly]   &nbsp;&nbsp;  (December 16, 2022)  
10.&nbsp; NEAR Foundation Transparency Report&nbsp;&nbsp;&nbsp; [Quarterly]  &nbsp;&nbsp;(December 20, 2022)    
11.&nbsp; NEAR Weekly On Chain Data Report&nbsp;&nbsp;&nbsp;    [Weekly]   &nbsp;&nbsp;  (December 23, 2022)    
12.&nbsp; NEAR 2022: A Year in Review     &nbsp;&nbsp;&nbsp;    [Yearly] &nbsp;&nbsp;    (December 23, 2022)  



""")

st.write("""   
##### Sources #####   """)
st.write("""    1.https://www.coindesk.com/learn/what-is-near-protocol-and-how-does-it-work/  
        2.https://www.kraken.com/en-gb/learn/what-is-near-protocol  
        3.https://near.org/blog/near-weekly-on-chain-data-report-december-23/
      
              """)
c1, c2, c3 = st.columns(3)
with c2:
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.notion.site/)**', icon="👨🏻‍💼")
with c1:
    st.info(
        '**Data:  [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
with c3:
    st.info(
        '**GuitHub Link:  [GuitHub](https://github.com/Kaizen-Step/Terra_Price_Run_Investigation)**', icon="💻")
