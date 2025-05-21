import streamlit as st
from read_data import read_data 
from kpis import number_sells, total_revenue, bigs

df = read_data()

chart_data = bigs

def layout():
    st.markdown("# Dashboard Revenue 2024")
    st.markdown("Simple Dashboard to display revenue 2024 import from CSV files")

    labels = ("TOTAL SELLS", "TOTAL REVENUE")
    cols = st.columns(2)
    kpis = (number_sells, total_revenue)
    
    for col, label,kpi in zip(cols, labels, kpis):
        with col:
            st.metric(label=label, value=kpi)

    st.title("Big Customers")

    st.bar_chart(chart_data, x="customer", y="revenue")

    st.markdown("# Raw Data")
    st.dataframe(df)

if __name__=="__main__":
    layout()
