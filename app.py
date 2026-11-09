
import joblib
import pandas as pd
import streamlit as st


# Load the trained model once per session
@st.cache_resource
def load_model():
    return joblib.load("superkart_sales_model.joblib")


model = load_model()

st.title("SuperKart Sales Prediction")

# Input fields for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = st.number_input("Product Allocated Area (share of display area)", min_value=0.0, max_value=1.0, value=0.069, format="%.3f")
Product_MRP = st.number_input("Product MRP", min_value=0.0, value=147.03)
Store_Size = st.selectbox("Store Size", ["Medium", "High", "Small"])
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Tier 2", "Tier 1", "Tier 3"])
Store_Type = st.selectbox("Store Type", ["Supermarket Type2", "Supermarket Type1", "Departmental Store", "Food Mart"])
Product_Id_char = st.selectbox("Product code prefix (FD = food, DR = drink, NC = non-consumable)", ["FD", "NC", "DR"])
Store_Age_Years = st.number_input("Store Age (Years)", min_value=0, value=23, step=1)
Product_Type_Category = st.selectbox("Product Type Category", ["Non Perishables", "Perishables"])

product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category,
}

if st.button("Predict"):
    input_df = pd.DataFrame([product_data])
    prediction = model.predict(input_df)
    st.markdown(f"Predicted Product Store Sales Total: **{prediction[0]:,.2f}**")
