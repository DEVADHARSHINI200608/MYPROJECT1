import os
import random
import streamlit as st
from PIL import Image
image_path = r"C:\Users\DevadharshiniKumar\Desktop\g.jpg"

# Check if the file exists
if os.path.exists(image_path):
    try:
        image = Image.open(image_path)
        st.image(image, caption='Sample Image')
    except Exception as e:
        st.write(f"Error loading image: {e}")
else:
    st.write("File does not exist at the specified path.")
# Loading CSS file
c = """
<style>
[data-testid="stAppViewContainer"]{background-color: #87CEEB;}
</style>
"""
st.markdown(c, unsafe_allow_html=True)

st.title("GUESS THE NUMEROS")
a = st.text_input("YOUR NAME:")

st.write("SELECT THE OPTIONS")
st.write("THE GUSSER IS:")
'''if st.button("ME"):
    with st.spinner("LOADING"):
        time.sleep(2)
        st.success("YOUR GAME STARTS NOW")

    def guessnumber():
        n = random.randint(1, 10)
        l = 0
        attempts = 0
    
        while l != n:
            l = st.number_input("Guess a number between 1 and 10: ", min_value=1, max_value=10, key="hello")
            attempts += 1
        
            if l < n:
                st.write("Too low!")
            elif l > n:
                st.write("Too high!")
    
    st.write(f"Congratulations! You found the number in {attempts} attempts.")
    guessnumber()
if st.button("computer"):
    with st.spinner("LOADING"):
        time.sleep(2)
        st.success("YOUR GAME STARTS NOW")
        def user():
            print("Think of a number between 1 and 100.")
            less = 1
            high = 100
            react = ''
            num1=0

            while less <= high:
                mid = (less + high)// 2
                react = input(f"Is your number {mid}? (Enter 'h' if it's higher, 'l' if it's lower, 's' if it's correct): ")

            if react == 's':
                print(f"Yay! I guessed it. Your number is {mid}.")
                return
            elif react == 'l':
                less = mid +1
            elif react == 'h':
                high = mid -1
            else:
                print("Invalid input, please enter 'h', 'l', or 'c'.")
        num1+=1
        print(f"We have founded the output in {num1} attempts")
        user()'''