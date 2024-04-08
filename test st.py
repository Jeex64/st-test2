import streamlit as st
import streamlit_antd_components as sac


 

st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

import streamlit as st

with st.popover("Open popover"):
    st.markdown("Hello World 👋")
    name = st.text_input("What's your name?")

st.write("Your name:", name)

sac.tree(items=[
    sac.TreeItem('item1', tag=[sac.Tag('Tag', color='red'), sac.Tag('Tag2', color='cyan')]),
    sac.TreeItem('item2', icon='apple', description='item description', children=[
        sac.TreeItem('tooltip', icon='github', tooltip='item tooltip'),
        sac.TreeItem('item2-2', children=[
            sac.TreeItem('item2-2-1'),
            sac.TreeItem('item2-2-2'),
            sac.TreeItem('item2-2-3'),
        ]),
    ]),
    sac.TreeItem('disabled', disabled=True),
    sac.TreeItem('item3', children=[
        sac.TreeItem('item3-1'),
        sac.TreeItem('item3-2'),
    ]),
], label='label', index=0, align='center', size='md', icon='table', open_all=True, checkbox=True)

