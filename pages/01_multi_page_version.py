import streamlit as st

"""
# Streamlit Keyed Widget State Issue
"""
st.info("""
    This app shows an issue with how state of widgets with `key=` is persisted across multipage apps,
    and the same class of issue in a single page app format.
""")

st.caption("View the app source code [here](https://github.com/sfc-gh-jcarroll/multipage-state-demo)")

"""
---
## Multi-page app version (Part 1)

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

This session state should remain stable across page views.
"""
with st.echo():
    st.write(st.session_state)

"""
---
### **Step 4:** Go to the other page.

:point_left: Click on `another page`, and see how the value of foo is preserved.
"""
