from collections import namedtuple
import altair as alt
import math
import pandas as pd


"""
# Calculadora de puntos (beta)
Edit `/ensayo1.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
"""


a = 0
doct = 0
papers = 0

print("Papers: ")
papers = int(input())
print("Título de doctorado: Si: 1, No: 0")
doct = int(input())

print("Puntos = ",3*papers+doct*10)
   
