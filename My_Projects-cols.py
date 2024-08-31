import streamlit as st


st.markdown("<h1 style='text-align: center; '>My Projects</h1>", unsafe_allow_html=True)
st.subheader("",divider='rainbow')
c1,c2,c3 = st.columns(3)

with c1:
    st.markdown( """
    <div style="display: flex; justify-content: center;">
        <img src="https://www.idfcfirstbank.com/content/dam/idfcfirstbank/images/blog/finance/what-is-atm-717x404.jpg" width="200" height="200"style="border-radius: 30px;">
    </div>
    """,unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: black;'> ATM App</h4>", unsafe_allow_html=True)

    st.write('''
             An ATM app that allows users to deposit, withdraw, and check balance.
             ''')
    st.markdown("###### Github: [Click here](#)")
    
with c2:
    
    st.markdown( """
    <div style="display: flex; justify-content: center;">
        <img src="https://m.media-amazon.com/images/I/61N8dO3ebvL._AC_UF1000,1000_QL80_.jpg" width="220" height="200"style="border-radius: 30px;">
    </div>
    """,unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: black;'> Shopping App</h4>", unsafe_allow_html=True)
    st.write('''
             A shopping app that allows users to search for products and add them to their cart. The app also allows users to view their shopping cart and checkout.
             ''')
    st.markdown("###### Github: [Click here](#)")

with c3:
    st.markdown( """
    <div style="display: flex; justify-content: center;">
        <img src="https://unitedguidestravel.com/wp-content/uploads/2020/06/Top-Traditional-Egyptian-Food-Drinks.jpg" width="200" height="200" style="border-radius: 30px;">
    </div>
    """,unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center; color: black;'>Meal Planner App</h4>", unsafe_allow_html=True)

    st.write('''
             A meal planner app that allows users to generate a random meal plan for the week.
             ''')
    st.markdown("###### Github: [Click here](#)")