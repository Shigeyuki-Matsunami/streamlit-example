from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")
