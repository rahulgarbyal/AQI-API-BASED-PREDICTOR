import streamlit as st

st.title("AQI FORECASTING AND TREND ANALYSIS")
st.header("AQI FORECASTING")
st.caption("""**The objective of this project is to analyze"
           Air quality trends across multiple indian cities
            and predict future aqi values using historical 
            time-series data.**""")

st.subheader('PROBLEM STATEMENT')
st.caption("""**Air Pollution is one of the major
            environmental concerns in India.
            AQI varies Significantly across cities
            and seasons** """)
st.markdown("""_MARKDOWN_""")

code = """
    def greet():
        print("hello friend")
    """
st.code(code, language="python")
st.divider()
