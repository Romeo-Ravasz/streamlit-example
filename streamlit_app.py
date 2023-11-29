import streamlit as st

st.title("Számológép")
st.write("---")

num1 = st.number_input(label = "Első szám:")
num2 = st.number_input(label = "Második szám:")

st.write("geci")
muvelet = st.radio("Műveletek", ("összeadás", "kivonás", "szorzás", "osztás"))

vegeredmeny = 0

def kiszámolás():
    if muvelet == "összeadás":
        vegeredmeny == num1 + num2
    if muvelet == "kivonás":
        vegeredmeny == num1 - num2
    if muvelet == "szorzás":
        vegeredmeny == num1 * num2
    if muvelet == "osztás":
        vegeredmény == num1 / num2
    else:
        st.error("Valami elromlott :/")

    st.success(f"A végeredmény: {vegeredmeny}")

if st.button("Kalkulálj!"):
    kiszámolás()


        
        


