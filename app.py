import streamlit as st

# Apply Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
        color: white;
    }

    .stApp {
        background: #c0c0c0;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }

    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }

    .description {
        text-align: center;
        font-size: 18px;
        color: #333333;
        margin-top: 10px;
        margin-bottom: 30px;
}
    

    .stButton > button {
        font-size: 18px;
        background: #008000;
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
        border: none;
    }

    .stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    }
    </style>
""", unsafe_allow_html=True)


#title and description:

st.markdown("<h1>🔁 Unit Converter</h1>",unsafe_allow_html=True)
st.markdown("<p class='description'>Convert between different units of Length, Weight, and Temperature.</p>", unsafe_allow_html=True)

# Conversion logic
def convert_length(value, from_unit, to_unit):
    factor = {
        'Meter': 1,
        'Kilometer': 1000,
        'Mile': 1609.34,
        'Foot': 0.3048,
        'Centimeter': 100,
        'Milimeter': 0.001,
        'Yard': 0.9144,
        'Inch': 2.54
    }
    return value * factor[from_unit] / factor[to_unit]

def convert_weight(value, from_unit, to_unit):
    factor = {
        'Kilogram': 1,
        'Gram': 0.001,
        'Pound': 0.453592,
        'Ounce': 0.0283495,
        'Miligram': 1000000
    }
    return value * factor[from_unit] / factor[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    # Celsius to others
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

# Main UI
conversion_type = st.sidebar.selectbox("Select conversion type:", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    units = ["Meter", "Kilometer", "Mile", "Foot", "Centimeter", "Milimeter", "Inch", "Yard"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0)
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Weight":
    units = ["Kilogram", "Gram", "Pound", "Ounce", "Miligram",]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0)
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter temperature:", format="%.2f")
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")
