from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Calculadora de puntos (beta)
Edit `/ensayo1.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
"""


with st.echo(code_location='below'):
    papers = st.slider("Number of points in spiral", 0, 100)
    doctorado = st.slider("Number of turns in spiral", 0, 1)

    print("puntos totales: ",papers*2 + doctorado*10)
    
   
