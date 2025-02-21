import pickle
import streamlit as st
import urllib.request
from sklearn.linear_model import LogisticRegression
import os

# Set Page Config with a background image
st.set_page_config(page_title="🛒 E-Commerce Spending Predictor", page_icon="📊", layout="centered")

# Load the model correctly
# Raw URL to the model
url = "https://raw.githubusercontent.com/umeshpardeshi9545/Ecommerce-regression/blob/main/Ecom.pkl"

# Load the model
try:
    with urllib.request.urlopen(url) as response:
        model_data = response.read()  # Read bytes
        model = pickle.loads(model_data)  # Load model from bytes
except Exception as e:
    model = None
    st.error(f"Error loading the model: {e}")

# Custom background image styling
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1566207274740-0f6f1a8cbbff");
    background-size: cover;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Streamlit UI
def main():
    st.markdown("# 🛍️ E-Commerce Yearly Spending Prediction")
    st.write("🔮 Predict how much a customer will spend yearly based on their app usage behavior!")

    # Input fields in a styled container
    with st.container():
        st.subheader("📊 Enter Customer Details")
        Avg_Session_Length = st.number_input("🕒 Avg Session Length (minutes)", min_value=0.0, format="%.2f")
        Time_on_App = st.number_input("📱 Time on App (minutes)", min_value=0.0, format="%.2f")
        Time_on_Website = st.number_input("🖥️ Time on Website (minutes)", min_value=0.0, format="%.2f")
        Length_of_Membership = st.number_input("🔗 Length of Membership (years)", min_value=0.0, format="%.2f")

    # Prediction button with enhanced styling
    if st.button("🔍 Predict Spending"):
        try:
            # Make prediction
            inputs = [[Avg_Session_Length, Time_on_App, Time_on_Website, Length_of_Membership]]
            prediction = model.predict(inputs)

            # Display result with success message
            st.success(f"💰 Predicted Yearly Amount Spent: **${prediction[0]:.2f}**")

        except Exception as e:
            st.error(f"❌ Error during prediction: {e}")

if __name__ == '__main__':
    main()
