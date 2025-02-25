import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_types import AgentType

# Streamlit App
st.set_page_config(page_title="Math Solver & Data Search", page_icon="=", layout="wide")
st.title("Text to Math Problem Solver & Wikipedia Search")

# Sidebar for API key
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

if not groq_api_key:
    st.info("Please provide the Groq API Key to use the model")
    st.stop()

# Initialize LLM
llm = ChatGroq(groq_api_key=groq_api_key, model="gemma2-9b-it")

# Wikipedia Tool
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(name="Wikipedia Tool", func=wikipedia_wrapper.run, description="Search Wikipedia for information")

# Math Solver
math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(name="Calculator", func=math_chain.run, description="Solve math problems")

# Prompt Template for Reasoning
prompt_template = """
You are an agent tasked with solving users' mathematical questions. Logically arrive at the solution and display it step by step for the question below:

Question: {question}
Answer:
"""

prompt = PromptTemplate(template=prompt_template, input_variables=["question"])

# Reasoning Tool
LLMChain1 = LLMChain(llm=llm, prompt=prompt)
reasoning_tool = Tool(name="Reasoning Tool", func=LLMChain1.run, description="Solve math problems step by step.")

# Initialize Agent
assistant_agent = initialize_agent(
    tools=[calculator, wikipedia_tool, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Hello! I can help you solve math problems and search for information on Wikipedia. How can I assist you today?"
        }
    ]

# Display chat history
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# User Input
question = st.text_input("Ask me anything", label_visibility="collapsed")

# Function to generate the response
def generate_response(user_question):
    response = assistant_agent.invoke({'input': user_question})
    return response

# Start the chat
if question and st.button("Find my answer"):
    with st.spinner("Wait, it's loading..."):
        st.session_state["messages"].append({"role": "user", "content": question})
        st.chat_message("user").write(question)
        response = generate_response(question)
        st.session_state["messages"].append({"role": "assistant", "content": response})
        st.write("### Response ###")
        st.success(response)
