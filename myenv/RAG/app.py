import streamlit as st
from rag_with_palm import RAGPaLMQuery

# Instantiate the class
rag_palm_query_instance = RAGPaLMQuery()

# Set page title and favicon
st.set_page_config(
    page_title="CodeWave Assistant",
    page_icon="🛍",
)

# Set app title and description
st.markdown("""
    <h1 style='text-align: center;'>FIND RIGHT <span style='color: lightblue;'>PRODUCT !!🛍</span></h1>
    <hr style='border: 2px solid lightblue;'>
""", unsafe_allow_html=True)
st.markdown("""
    <h2 style='text-align: center;font-size: 18px;'>Welcome to the Product Recommendation Chatbot for an Online Fashion Retailer.</h2>
""", unsafe_allow_html=True)
st.markdown("""
    <h3 style='text-align: center;font-size: 18px;'>Please enter your question in the chatbox on the left.</h3>
""", unsafe_allow_html=True)

# Add sidebar for additional functionality or information
st.sidebar.markdown("""
    <h3 style=' text-align: left;'>😎 Settings</h3>
    <hr style='border: 1px solid white; margin-bottom: 10px; margin-top: 5px;'>
""", unsafe_allow_html=True)
# You can add more widgets to the sidebar based on your requirements
user_name = st.sidebar.text_input("Your Name", "User")
show_info = st.sidebar.checkbox("Show Additional Info")



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



# React to user input
if prompt := st.chat_input("Need info? Drop your question here!",):
    # Display user message in chat message container
    st.chat_message("user").markdown(f"{user_name}: {prompt}")
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": f"{user_name}: {prompt}"})
    response = rag_palm_query_instance.query_response(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})



# Optionally, show additional info based on sidebar checkbox
if show_info:
    st.sidebar.markdown("Additional information goes here.")