import streamlit as st

st.title("Számológép")

szam1 = st.number_input(label = szam1)
szam2 = st.number_input(label = szam2)

st.write("geci")
muvelet = st.radio("Műveletek", ("összeadás", "kivonás", "szorzás", "osztás"))

vegeredmeny = 0

def kiszámolás():
    if muvelet == "összeadás":
        vegeredmeny == szam1 + szam2
    if muvelet == "kivonás":
        vegeredmeny == szam1 - szam2
    if muvelet == "szorzás":
        vegeredmeny == szam1 * szam2
    if muvelet = "osztás":
        vegeredmény == szam1 / szam2
    else:
        st.error("Valami elromlott :/")

    st.success(f"A végeredmény: {vegeredmeny})

if st.button("Kalkulálj!"):
    kiszámolás()


        
        


