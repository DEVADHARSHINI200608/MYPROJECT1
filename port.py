import streamlit as st

st.markdown(
    """
    <style>
    .container {
        text-align: center;
        position: relative;
        margin: 20px 0;
    }
    .container::before {
        content: '';
        display: block;
        width: 100%;
        height: 2px;
        background-color: #000;
        position: absolute;
        top: 0;
    }
    .title {
        display: inline-block;
        padding: 0 10px;
        background: #fff;
        position: relative;
        z-index: 1;
    }
    </style>
    <div class="container">
        <span class="title"><b>MY PORTFOLIO</b></span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .container {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        margin-left: 5px;
        margin-right: 10px;

    }
    .content {
        margin: 2px; /* Adjust the spacing between content and line */
    }
    .centered-vertical-line {
        height: 500px; /* Adjust the height as needed */
        width: 10px;
        background-color: #000;
        margin-left:70px;
    }
    </style>
    <div class="container">
        <div class="content">
            <p><br><br><br><b>NAME:K.DEVADHARSHINI</b><br><br><br><b>PHONE:1234567890</b><br><br><br><b>EMAIL:ABC@gmail.com</b></p>
        </div>
        <div class="centered-vertical-line"></div>
        <div class="content">
            <p><br><br><br><b>SKILLS AND LANGUAGES:PYTHON PROGRAMMING LANGUAGE</b><br><br><br><b>ACHIEVEMENTS/CERTIFICATION:CERTIFIED IN CISCO COURSES</b></p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)





