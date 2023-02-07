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
## Multi-page app version (Part 2)

### Step 5: Look at the state again.

**You should see your state for `foo` written here.**

"""
with st.echo():
    st.write(st.session_state)

"""
---
### Step 6: Look at the state again.

:point_left: Click back to `multi page version` to **see the value of "foo" disappear. This is the
bug!**

"""

