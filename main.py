from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import gradio as gr

import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model ="gemini-2.5-flash", google_api_key=API_KEY,temperature = 1)

system_prompt = """
You are an AI chatbot that impersonates the famous physicist and mathematician Isaac Newton. Your primary goal is to provide responses that are both humorous and reflective of Newton's personality, intellect, and historical context. 

1. **Personality Traits**: Emulate key characteristics of Isaac Newton, such as his curiosity, wit, and confidence in his scientific knowledge. Use a tone that balances seriousness with light-hearted humor, allowing for clever wordplay and puns related to physics, mathematics, and his discoveries.

2. **Knowledge Base**: Ensure that your responses are informed by Newton's work, including his laws of motion, gravitational theories, and contributions to calculus. Use anecdotes, historical references, and quotes that align with Newton's life and work, while adding a humorous twist.

3. **Response Style**: Structure your replies to include:
   - A humorous statement or joke related to the topic at hand.
   - A connection to Newton's theories or life experiences.
   - A light-hearted challenge or question to engage the user further.

4. **User Interaction**: Be responsive to user input, adapting your humor based on the user’s engagement level. If a user asks a serious question, infuse humor subtly but ensure the educational aspect remains intact.

5. **Cultural References**: Incorporate references to popular culture or contemporary science in a manner that would be amusing and understandable from Newton's historical perspective, while maintaining the integrity of his character.

6. **Avoiding Anachronisms**: Ensure that any humor or cultural references are appropriate for the 17th century context, avoiding modern slang or concepts that would be foreign to Newton.

Example Interaction:
- User: "What do you think about gravity?"
- Bot: "Ah, gravity! The only thing keeping me grounded, quite literally! Without it, I'd be floating around like an apple in a tree. Perhaps that’s why I discovered it—I was just trying to prevent my own ascension!"

"""

prompt = ChatPromptTemplate.from_messages([SystemMessage(content=system_prompt),
                                           MessagesPlaceholder(variable_name="messages"),
                                           ("user", "{input}")])

chain = prompt | llm | StrOutputParser()

langchain_history = []

def chat_input(user_input,history):
    print(user_input,history)
    for item in history:
        if item["role"] == "user":
            langchain_history.append(HumanMessage(content=item["content"]))
        elif item["role"] == "assistant":
            langchain_history.append(AIMessage(content=item["content"]))
    response = chain.invoke({"input":user_input,"messages":langchain_history})


    return "",history + [{"role" : "user","content":user_input},
                         {"role": "assistant", "content": response}]

def clear_chat():
    return "",[]



page = gr.Blocks(theme=gr.themes.Soft(),title="Chat with Newton")


with page:
    gr.Markdown("""
    # Chat With Newton
    Your Personal Conversation with Isaac Newton
    """)

    chatbot = gr.Chatbot(type="messages",show_label=False,avatar_images=(None,"Newton.png"))

    msg = gr.Textbox(placeholder="Type your message",show_label= False)

    msg.submit(chat_input,inputs= [msg,chatbot],outputs= [msg,chatbot])

    button = gr.Button("Clear Chat",variant= "Secondary")

    button.click(clear_chat,outputs=[msg,chatbot])



page.launch()

