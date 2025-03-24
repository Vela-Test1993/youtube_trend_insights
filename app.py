import streamlit as st
from src.frontend.utils import logger

logger = logger.get_logger()

def render_chat_bot():
    logger.info("Starting conversation")
    user_query = st.chat_input("Ask me about youtube trends")

render_chat_bot()