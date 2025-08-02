import chainlit as cl
from agents import agent
from dotenv import load_dotenv
import os

load_dotenv()

@cl.on_chat_start
async def start():
    await cl.Message("👋 Hello! I’m your Smart Task Routing Assistant. Ask me anything!").send()

@cl.on_message
async def handle_message(msg: cl.Message):
    response = agent.run(msg.content)
    await cl.Message(response).send()
