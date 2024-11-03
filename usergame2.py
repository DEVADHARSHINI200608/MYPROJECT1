import streamlit as st
import base64

def initialize_game():
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.mid = (st.session_state.low + st.session_state.high) // 2
    st.session_state.react = ''
    st.session_state.num1 = 0
    st.session_state.guessed = False

def bcd():
    if 'low' not in st.session_state:
        initialize_game()

    st.title("Guess the Number Game")

    if st.session_state.guessed:
        st.write(f"Yay! I guessed it. Your number is {st.session_state.mid}.")
        st.write(f"We found the output in {st.session_state.num1} attempts.")
        st.title("I WON !!!!!!!")
        f =r"C:\Users\DevadharshiniKumar\Downloads\shinchan.gif"
        with open(f, "rb") as gif_file:
            g = gif_file.read()
            e = base64.b64encode(g).decode("utf-8")
            st.markdown(
                f"""
                <div style="display: flex; justify-content: center;">
                    <img src="data:image/gif;base64,{e}" width="900">
                </div>
                """,
                unsafe_allow_html=True
                )
        if st.button("Play Again"):
            initialize_game()
    else:
        st.write("Think of a number between 1 and 100.")
        st.write(f"My guess is {st.session_state.mid}.")
        reaction_options = ["higher", "lower", "correct"]
        react = st.selectbox("Select your response:", reaction_options)

        if st.button("Submit"):
            if react == 'correct':
                st.session_state.guessed = True
            elif react == 'lower':
                st.session_state.low = st.session_state.mid + 1
            elif react == 'higher':
                st.session_state.high = st.session_state.mid - 1
            else:
                st.write("Invalid input, please enter 'higher', 'lower', or 'correct'.")
                return
            
            st.session_state.mid = (st.session_state.low + st.session_state.high) // 2
            st.session_state.num1 += 1

if __name__ == "__main__":
    bcd()

