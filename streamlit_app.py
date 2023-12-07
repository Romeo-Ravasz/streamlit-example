import streamlit as st

st.title("Regisztráció")
st.write("---")

email = st.input(label = "Add meg az email címed:")
nev = st.input(label = "Add meg a neved:")
pencil = st.radio("Add meg a nemed:", ("férfi", "Nő"))
eletkor = st.slider("Add meg az életkorodat:", (0, 100))

        
        


