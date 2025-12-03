import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize secret number in session state
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)

if "message" not in st.session_state:
    st.session_state.message = ""

guess = st.number_input("Enter your guess (1–100):", min_value=1, max_value=100, step=1)

if st.button("Guess"):
    if guess < st.session_state.secret:
        st.session_state.message = "📉 Too low! Try again."
    elif guess > st.session_state.secret:
        st.session_state.message = "📈 Too high! Try again."
    else:
        st.session_state.message = "🎉 Correct! You guessed the number!"
        
    st.rerun()

st.write(st.session_state.message)

if st.button("Reset Game"):
    st.session_state.secret = random.randint(1, 100)
    st.session_state.message = "🔄 Game reset! Guess again."
    st.rerun()
