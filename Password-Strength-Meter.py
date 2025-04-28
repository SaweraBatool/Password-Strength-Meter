import re
import streamlit as st

# Password Strength Meter
def check_password_strength(password):
    score = 0  # Password ki overall strength ko measure karta hai.
    feedback = []  # Weak passwords ko improve karne ke liye help karta hai

    # Length Check
    if len(password) >= 8:  # Password ki length check karta hai, minimum 8 characters
        score += 1
    else:
        feedback.append("\u274C Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):  # Upper aur lowercase letters check karta hai
        score += 1
    else:
        feedback.append("\u274C Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):  # Password me numbers check karta hai
        score += 1
    else:
        feedback.append("\u274C Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):  # Password me special characters check karta hai
        score += 1
    else:
        feedback.append("\u274C Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:  # Strong password condition
        return "strong", "\u2705 Strong Password!"
    elif score == 3:  # Moderate password condition
        return "moderate", "\u26A0\uFE0F Moderate Password - Consider adding more security features."
    else:  # Weak password condition
        return "weak", feedback

# Streamlit App
def main():
    st.title("🔐 Password Strength Meter with SAWERA")
    st.write("Welcome to the Login Form! Please enter your details below.")

    # User Inputs
    name = st.text_input("Enter your name:")
    password = st.text_input("Enter your password:", type="password")

    # Check Password Strength
    if st.button("Submit"):
        if name and password:
            strength, message = check_password_strength(password)
            if strength == "strong":
                st.success(f"🎉 Welcome {name}!")
                st.balloons()
            elif strength == "moderate":
                st.warning(message)
            else:
                st.error("❌ Weak Password. Please improve it using the suggestions below:")
                for suggestion in message:
                    st.write(f"  - {suggestion}")
        else:
            st.error("❌ Please fill in both fields.")

if __name__ == "__main__":
    main()