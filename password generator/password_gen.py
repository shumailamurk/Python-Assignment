import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    
    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

st.title("🔒 Password Generator")

length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"🔑 Generated Password: `{password}`")

# 🎨 Pyara Footer Message
st.markdown("---")  # Line separator for styling
st.markdown(
    "<p style='text-align:center; font-size:18px; color:#FF5733;'>"
    "🚀 Built with ❤️ by <b>Shumaila Murk</b> </p>",
    unsafe_allow_html=True
)
