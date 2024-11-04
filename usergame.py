import random # imports the random module
import streamlit as st
import base64

def initialize_game():# responsible for initialising the game when user press play again
    st.session_state.number_to_guess = random.randint(1, 10)# assigns random integer between 1 to 10
    st.session_state.attempts = 0
    st.session_state.guessed_correctly = False

def abc():#it is the main function  "_name_"
    # Initialize session state variables
    if 'number_to_guess' not in st.session_state or 'attempts' not in st.session_state or 'guessed_correctly' not in st.session_state:
        initialize_game()

    st.title("Guess the Number Game")

    if st.session_state.guessed_correctly:
        st.write(f"Congratulations! You guessed the number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts.")
        if st.button("Play Again"):
            initialize_game()
    else:
        st.write("I have picked a number between 1 and 10. Try to guess it!")
        guess = st.number_input("Enter your guess:", min_value=1, max_value=10)
        
        if st.button("Submit Guess"):
            st.session_state.attempts += 1
            if guess < st.session_state.number_to_guess:
                st.write("Too low! Try again.")
            elif guess > st.session_state.number_to_guess:
                st.write("Too high! Try again.")
            else:
                st.write(f"Congratulations! You guessed the number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts.")
                fi =r"C:\Users\DevadharshiniKumar\Downloads\won.gif"
                with open(fi, "rb") as gif_file:
                     ge = gif_file.read()
                     el = base64.b64encode(ge).decode("utf-8")

# Embed the GIF in HTML and align it to the right
                st.markdown(
                    f"""
                    <div style="display: flex; justify-content: center;">
                        <img src="data:image/gif;base64,{el}" width="900">
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.session_state.guessed_correctly = True



