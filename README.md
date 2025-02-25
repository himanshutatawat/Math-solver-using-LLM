# Math Solver & Wikipedia Search App  

## Overview  
This is a **Streamlit-based web application** that allows users to:  
- **Solve mathematical problems step-by-step**  
- **Perform Wikipedia searches for information**  
- **Use an AI-powered agent to provide logical reasoning**  

The app utilizes **LangChain**, **Groq API**, and **Wikipedia API Wrapper** to provide an interactive experience.  

## Features  
- 🧮 **Solves math problems with step-by-step reasoning**  
- 📖 **Searches Wikipedia for relevant information**  
- 🚀 **Uses Groq’s Gemma2-9B-IT LLM for natural language understanding**  
- 💡 **AI-powered reasoning tool for math problems**  
- 🔄 **Maintains chat history for smooth interactions**  

## Installation  

### Prerequisites  
Ensure you have **Python 3.8+** installed.  

### Install Dependencies  
Run the following command to install the required libraries:  

```sh
pip install streamlit langchain langchain_groq langchain_community
```

## Usage  

### 1️⃣ Run the Streamlit App  
Execute the following command:  

```sh
streamlit run app.py
```

### 2️⃣ Enter Details  
- **Groq API Key:** Enter your **Groq API Key** in the sidebar.  
- **Ask a Question:** Provide a **math problem** or a **Wikipedia search query**.  
- Click **"Find my answer"** to generate a response.  

## Environment Variables  
Set up your **Groq API Key** before running the app:  

```sh
export GROQ_API_KEY="your_groq_api_key"
```

Alternatively, enter it manually in the Streamlit sidebar.  

## Project Structure  

```
📂 math-wiki-chatbot
│── app.py              # Main Streamlit application
│── README.md           # Project documentation
│── requirements.txt    # Dependencies
```

## Future Enhancements  
- ✅ Add **support for multi-turn conversations**  
- ✅ Improve **math explanations with diagrams**  
- ✅ Integrate **voice input for queries**  

## License  
This project is open-source and available under the **MIT License**.  
