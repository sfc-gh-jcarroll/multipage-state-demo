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
## Discussion

A few github issues that describe this with various examples and discussion:
- [#5813 - Preserve widget state when a widget disappears from the page (demoed via Multipage Apps)](https://github.com/streamlit/streamlit/issues/5813)
- [#4458 - An option to keep component values in the session state](https://github.com/streamlit/streamlit/issues/4458)
- [#5620 - text_input hidden by checkbox doesn't load from session state](https://github.com/streamlit/streamlit/issues/5620)
- [#4989 - widget state not synced between multiple pages](https://github.com/streamlit/streamlit/issues/4989)
"""

"""
---
### Questions

- Do you have a full working public app where you had to hack around this (such as duplicating or using "shadow keys")? Please share with us!
- Do you have an app or use case where you rely on the current transient state behavior, that will break if we change this? We **really** want
  to hear about these! Please share!

### Possible fixes

- It seems like most developers we hear from find the current behavior very unintuitive, and we see a lot more use cases that have to
  work around this rather than benefit from it.
  - Given that, should we just do a breaking change to change the default behavior to the intuitive one?
  - If so: We should still provide a path to clear keyed widget state when needed.
- If not a breaking change: most proposals seem to prefer something like a `persist=` key. For example, both `whitphx` and `MathCatsAnd` propose
  something like this in [#4458](https://github.com/streamlit/streamlit/issues/4458). Thoughts on this?

"""