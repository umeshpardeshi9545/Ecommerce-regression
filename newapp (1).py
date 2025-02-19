import pickle
import streamlit as st
import urllib.request
from sklearn.linear_model import LogisticRegression


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

def main():
    st.title("Titanic Survival Prediction ")
    
    # Input variables
    Avg_Session_Length = st.text_input("Avg Session Length : ")
    Time_on_App = st.text_input("Time on App")
    Time_on_Website = st.text_input(" Time on Website ")
    Length_of_Membership = st.text_input("Length of Membership")
    
    if st.button("Predict"):
        if model is None:
            st.error("Model could not be loaded. Please check the file URL or format.")
            return

        try:
            # Convert inputs to floats
            inputs = [float(Avg_Session_Length), float(Time_on_App), float(Time_on_Website), float(Length_of_Membership)]
            
            # Make prediction
            prediction = model.predict([inputs])
            st.success(f"Prediction: { prediction}")
        except ValueError:
            st.error("Please enter valid numeric inputs for all fields.")
        except Exception as e:
            st.error(f"Error during prediction: {e}")

if __name__ == '__main__':
    main()
