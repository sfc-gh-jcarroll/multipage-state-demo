import streamlit as st

"""
# Streamlit Keyed Widget State Issue
"""

st.info("""
    This app shows an issue with how state of widgets with `key=` is persisted across multipage apps,
    and the same class of issue in a single page app format.
""")

"""
---
## Single-page app version

In the example below, the `text_input` widgets have a key set. Many developers expect that, by setting
the key, it will persist the text input when you toggle from one view to the other and back. However,
as you can see, currently the value is reset each time.
"""

with st.echo():
    view = st.radio("View", ["view1", "view2"])

    if view == "view1":
        st.text_input("Text1", key="text1")
        "☝️ Enter some text, then click on view2 above"
    elif view == "view2":
        "☝️ Now go back to view1 and see if your text is still there"

with st.expander(':eyes: Now see the "fixed" version'):
    'This shows the behavior many developers expect for the above code (using "shadow keys" approach)'
    key = "text"
    shadow_key = "_text"
    if shadow_key not in st.session_state:
        st.session_state[shadow_key] = st.session_state.get(key, "")

    view2 = st.radio("View ", ["view1", "view2"])
    if view2 == "view1":
        value = st.text_input("Text1", key=shadow_key)
        st.session_state[key] = value
        "☝️ Enter some text, then click on view2 above"
    elif view2 == "view2":
        "☝️ Now go back to view1 and see if your text is still there"

"👈 Now click on `multi page version` to see another version of this behavior"
