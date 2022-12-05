import streamlit as st

"""
# Streamlit Multipage State Issue (Page 2)
"""

st.info("""
    This app shows an error in how state is stored across multipage apps in Streamit
    1.15.2, and potentially since the beginning of mulitpage apps.
""")

"""
---
### **Step 5: Look at the state again.

**You should see your state for `foo` written here.**

"""
with st.echo():
    st.write(st.session_state)

"""
---
### **Step 6: Look at the state again.

:point_left: Click back to the main page to **see the value of "foo" dissappear. This is the
bug!**

"""

