import streamlit as st

"""
# Streamlit Multipage State Issue 
"""

st.info("""
    This app shows an error in how state is stored across multipage apps in Streamit
    1.15.2, and potentially since the beginning of mulitpage apps.
""")

"""
---
### **Step 1:** Type "ABC" into this dialog box

**Do no skip this step or the demo won't work!** Note that your text is stored in the
state variable `foo`. This is the "correct behavior" for this page, since the semantics
of key="foo" is that this dialog is now bound to that state variable.

"""
with st.echo():
    st.text_input("Set the state variable foo", key="foo")

"""
---
### **Step 2:** Click this button to manually add bar to the is page.

Note again how this is reflected below in the state.
"""
with st.echo():
    def set_bar():
        st.session_state.bar = 42
    st.button("Set bar state", on_click = set_bar)

"""
---
### **Step 3:** Look at the session state.

**This session state should remain stable across page views.
"""
with st.echo():
    st.write(st.session_state)

"""
---
### **Step 4:** Go to the other page.

:point_left: Click on the next page, and see how the value of foo is preserved.
"""

