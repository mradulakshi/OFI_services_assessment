import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="NexGen Warehouse Optimization Tool", layout="wide")
st.title("NexGen Warehouse Optimization Tool")
st.markdown("""This dashboard uses **data analytics + IoT insights** to optimize warehouse operations,
reduce storage costs, and maintain ideal inventory balance across locations.""")

# Load Data
@st.cache_data
def load_data():
    warehouse_df = pd.read_csv('warehouse_inventory.csv')
    iot_df = pd.read_csv('sample_iot.csv')
    routes_df = pd.read_csv('routes_distance.csv')
    delivery_df = pd.read_csv('delivery_performance.csv')
    cost_df = pd.read_csv('cost_breakdown.csv')
    feedback_df = pd.read_csv('customer_feedback.csv')
    vehicle_df = pd.read_csv('vehicle_fleet.csv')
    return warehouse_df, iot_df, routes_df, delivery_df, cost_df, feedback_df, vehicle_df

warehouse_df, iot_df, routes_df, delivery_df, cost_df, feedback_df, vehicle_df = load_data()

# Data Preprocessing
warehouse_df.columns = warehouse_df.columns.str.strip()
iot_df.columns = iot_df.columns.str.strip()

# Derived metrics
warehouse_df['Utilization_%'] = 100 * (warehouse_df['Current_Stock_Units'] / (warehouse_df['Current_Stock_Units'] + warehouse_df['Reorder_Level'] + 1))

# Merge IoT and warehouse data for environment monitoring
iot_summary = iot_df.groupby('warehouse').agg({
    'temperature': 'mean',
    'humidity': 'mean',
    'shelf_weight_pct': 'mean'
}).reset_index()

warehouse_summary = warehouse_df.groupby('Location').agg({
    'Current_Stock_Units': 'sum',
    'Reorder_Level': 'mean',
    'Storage_Cost_per_Unit': 'mean',
    'Utilization_%': 'mean'
}).reset_index()

# Sidebar Controls
st.sidebar.header(" Filter Options 🔍")
selected_location = st.sidebar.multiselect("Select Warehouse Locations", warehouse_summary['Location'].unique(), default=warehouse_summary['Location'].unique())

filtered_data = warehouse_summary[warehouse_summary['Location'].isin(selected_location)]

# Visualization 1: Warehouse Utilization
st.subheader("Warehouse Utilization Overview")
fig1 = px.bar(filtered_data, x='Location', y='Utilization_%', color='Location', title='Warehouse Utilization (%)', text_auto=True)
st.plotly_chart(fig1, use_container_width=True)


# Visualization 2: Storage Cost per Unit
fig2 = px.line(filtered_data, x='Location', y='Storage_Cost_per_Unit', markers=True, title='Average Storage Cost per Unit (INR)')
st.plotly_chart(fig2, use_container_width=True)


# Visualization 3: IoT Monitoring Dashboard
st.subheader("IoT Environment Monitoring (Smart Sensors)")
fig3 = px.scatter_3d(iot_summary, x='temperature', y='humidity', z='shelf_weight_pct', color='warehouse',
                     title='Warehouse IoT Metrics', size='shelf_weight_pct', symbol='warehouse')
st.plotly_chart(fig3, use_container_width=True)

# Visualization 4: Stock vs Reorder Level
st.subheader("Stock vs Reorder Analysis")
fig4 = px.bar(warehouse_df, x='Product_Category', y=['Current_Stock_Units', 'Reorder_Level'], barmode='group',
              color_discrete_sequence=['#636EFA', '#EF553B'], title='Stock Levels vs Reorder Thresholds by Product')
st.plotly_chart(fig4, use_container_width=True)


# Insights & Recommendations
st.subheader(" Smart Insights & Recommendations 💡")

# Identify low-stock warehouses
low_stock = warehouse_df[warehouse_df['Current_Stock_Units'] < warehouse_df['Reorder_Level']]

# Identify high storage cost warehouses
high_cost = warehouse_df[warehouse_df['Storage_Cost_per_Unit'] > warehouse_df['Storage_Cost_per_Unit'].mean()]

# IoT alerts
anomalies = iot_df[(iot_df['temperature'] > 28) | (iot_df['humidity'] > 75)]

st.markdown("#### 🔴 Low Stock Warehouses")
st.dataframe(low_stock[['Warehouse_ID', 'Location', 'Product_Category', 'Current_Stock_Units', 'Reorder_Level']])

st.markdown("#### 🟠 High Storage Cost Warehouses")
st.dataframe(high_cost[['Warehouse_ID', 'Location', 'Storage_Cost_per_Unit']])

st.markdown("#### ️IoT Environmental Alerts ⚠  ")
st.dataframe(anomalies[['warehouse', 'temperature', 'humidity', 'shelf_weight_pct']])


# Downloadable Summary
st.download_button(
    label="📥 Download Warehouse Summary",
    data=warehouse_summary.to_csv(index=False).encode('utf-8'),
    file_name='warehouse_summary.csv',
    mime='text/csv'
)


# Footer
st.markdown("""---
✅ **Developed for NexGen Logistics Pvt. Ltd.** | Powered by **Python + Streamlit + IoT Analytics**
""")



