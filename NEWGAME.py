import streamlit as st
import time
from usergame import abc
from usergame2 import  bcd
from PIL import Image
import base64
from io import BytesIO
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as file:
        binary_data = file.read()
    base64_data = base64.b64encode(binary_data).decode('utf-8')
    return base64_data

# Path to your local image
image_path = r"C:\Users\DevadharshiniKumar\Downloads\cloud.jpg"  # Replace with your local image path

# Convert the image to Base64
base64_image = get_base64_of_bin_file(image_path)

# CSS to set the background image
page_bg_img = f'''
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{base64_image}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
def paper():
    if 'page' not in st.session_state:
        st.session_state.page = 'page1'

    if st.session_state.page == 'page1':
        page1()
    elif st.session_state.page == 'page2':
        page2()
    elif st.session_state.page=='page3':
        page3()
    elif st.session_state.page=='page4':
        page4()
    elif st.session_state.page=='page5':
        page5()
    elif st.session_state.page=='page6':
        page6()
def page1():
    st.title("GUESS THE NUMEROS")
#gif1
    p=r"C:\Users\DevadharshiniKumar\Downloads\play.gif"
    with open(p, "rb") as gif_file:
        data = gif_file.read()
        gif = base64.b64encode(data).decode("utf-8")

# Embed the GIF in HTML and align it to the right
    st.markdown(
        f"""
        <div style="display: flex; justify-content: flex-start;">
            <img src="data:image/gif;base64,{gif}" width="260">
        </div>
        """,
        unsafe_allow_html=True
    )
#image kiddo

    filepath =r"C:\Users\DevadharshiniKumar\Downloads\kiddo.jpg"
    with open(filepath, "rb") as gif_file:
        gifdata = gif_file.read()
        encodedgif = base64.b64encode(gifdata).decode("utf-8")

# Embed the GIF in HTML and align it to the right
    st.markdown(
        f"""
        <div style="display: flex; justify-content: flex-end;">
            <img src="data:image/gif;base64,{encodedgif}" width="260">
        </div>
        """,
        unsafe_allow_html=True
    )
#gif
    f =r"C:\Users\DevadharshiniKumar\Downloads\rainbow.gif"
    with open(f, "rb") as gif_file:
        g = gif_file.read()
        e = base64.b64encode(g).decode("utf-8")

# Embed the GIF in HTML and align it to the right
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/gif;base64,{e}" width="900">
        </div>
        """,
        unsafe_allow_html=True
    )
#image left
    f =r"C:\Users\DevadharshiniKumar\Downloads\d3.jpg"
    with open(f, "rb") as gif_file:
        g = gif_file.read()
        e = base64.b64encode(g).decode("utf-8")

# Embed the GIF in HTML and align it to the right
    st.markdown(
        f"""
        <div style="display: flex; justify-content: flex-start;">
            <img src="data:image/gif;base64,{e}" width="600">
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("NEXT"):
        with st.spinner ("LOADING"):
            time.sleep(2)
            st.success("LET'S GO,CLICK NEXT AGAIN TO ENSURE YOU'RE IN")
            st.session_state.page = 'page2'

def page2():
    st.title("INSTRUCTIONS:")
    image = Image.open(r"C:\Users\DevadharshiniKumar\Downloads\brainy.jpg")
    st.markdown(
        """
        <style>
        .centered-image {
            display: flex;
            justify-content:flex-start; 
         }
        </style>
        """, 
        unsafe_allow_html=True
    )

# Display the image in the center with a custom size
    st.markdown('<div class="centered-image">', unsafe_allow_html=True)
    st.image(image, width=300)  # Adjust width or height as needed
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("--------------------------------------------------------------------- GAME 1----------------------------------------------------------")
    st.markdown("""- CHOOSE THE GUESSER OPTION AS ME""")
    st.markdown("""-THE COMPUTER GUESSES A NUMBER.NOW, ENTER THE NUMBER YOU GUESSED INSIDE THE BOX""")
    st.markdown("""- IF YOUR NUMBER GUSSED IS TOO LOW THAN THE NUMBER, GUESSED BY THE COMPUTER IT PRINTS TOO LOW""")
    st.markdown("""- IF YOUR NUMBER GUSSED IS TOO HIGH THAN THE NUMBER, GUESSED BY THE COMPUTER IT PRINTS TOO HIGH""")
    st.markdown("""- IF YOUR NUMBER GUSSED  BY THE COMPUTER IS EQUAL TO  THE NUMBER  GUESSED BY  YOU IT PRINTS YOU WON""")
    if st.button("NEXT"):
        st.session_state.page='page3'
def page3():
    st.write("--------------------------------------------------------------------- GAME 2----------------------------------------------------------")
    st.markdown("""- CHOOSE THE GUESSER OPTION AS COMPUTER""")
    st.markdown("""-YOU SHOULD GUESSES A NUMBER.NOW,  THE COMPUTER DISPLAYS  NUMBER IT GUESSED AND ASKS YOU WHETHER THE NUMBER IT IS GUESSED IS RIGHT""")
    st.markdown("""- IF YOUR NUMBER IT GUSSED IS TOO LOW THAN THE NUMBER, GUESSED BY YOU WRITE l""")
    st.markdown("""- IF YOUR NUMBER GUSSED IS TOO HIGH THAN THE NUMBER, GUESSED BY  YOU WRITE h""")
    st.markdown("""- IF NUMBER YOU GUESSED IS EQUAL TO NUMBER GUESSED BY THE COMPUTER THEN IT PRINTS IT WON """)
    if st.button("NEXT"):
        st.session_state.page='page4'
def page4():
    st.title("CHOOSE WHO IS THE GUESSER")
    i = Image.open(r"C:\Users\DevadharshiniKumar\Downloads\ppplay.gif")
    st.markdown(
        """
        <style>
        .centered-image {
            display: flex;
            justify-content:flex-end; 
         }
        </style>
        """, 
        unsafe_allow_html=True
    )

# Display the image in the center with a custom size
    st.markdown('<div class="centered-image">', unsafe_allow_html=True)
    st.image(i, width=500)  # Adjust width or height as needed
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("ME"):
        st.session_state.page='page5'
    if st.button("COMPUTER"):
        st.session_state.page='page6'
def page5():
    st.title("LET'S PLAY")
    if __name__ == "__main__":
        abc()
def page6():
    st.title("LET'S PLAY")
    if __name__ == "__main__":
        bcd()
if __name__ == "__main__":
    paper()
