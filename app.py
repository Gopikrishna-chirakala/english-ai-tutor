import streamlit as st
from grammar import check_grammar
from vocabulary import get_meaning

st.title("AI English Learning Tutor")

st.write("Type a sentence to check grammar or type 'meaning word' to learn vocabulary.")

user_input = st.text_input("You:")

if user_input:

    if user_input.startswith("meaning"):
        word = user_input.split()[-1]
        st.write("📘", get_meaning(word))

    else:
        result = check_grammar(user_input)

        if isinstance(result, list):
            st.write("❌ Possible corrections:")
            for r in result:
                st.write("-", r)
        else:
            st.write(result)