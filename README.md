# LangChain Basics: Person Information Summarizer

## Overview

This project is a simple introduction to **LangChain and LLM application development using Python**.

It takes information about a person as input and uses a language model running through Ollama to generate:

- A short summary of the person.
- Two interesting facts based on the provided information.

In this example, the input information is about Indian actress Kriti Sanon.

## Concepts Covered

- **PromptTemplate:** Creates a reusable prompt with an input variable.
- **ChatOllama:** Connects LangChain to a language model running through Ollama.
- **LCEL (LangChain Expression Language):** Uses the pipe (`|`) operator to connect the prompt and the language model into a chain.
- **Chain Invocation:** Uses `chain.invoke()` to send information to the model and receive a response.
- **python-dotenv:** Loads environment variables from a `.env` file.
- **LangSmith:** Supports tracing and debugging when configured.

## Technologies Used

- Python
- LangChain Core
- LangChain Ollama
- Ollama
- python-dotenv
- LangSmith (optional)

## How It Works

1. Store the person's information in a Python string.
2. Define a prompt asking the model to generate a short summary and two interesting facts.
3. Create a `PromptTemplate` using the `information` variable.
4. Initialize the Ollama language model using `ChatOllama`.
5. Connect the prompt and model using the pipe operator.
6. Invoke the chain with the information as input.
7. Print the generated response.

## Installation and Setup

### 1. Install uv

`uv` is a fast Python package and project manager used to manage dependencies and virtual environments.

Install `uv` using pip:

```bash
pip install uv
```

Verify the installation:

```bash
uv --version
```

### 2. Install Project Dependencies

Run the following command inside your project directory:

```bash
uv add black isort langchain langchain-ollama python-dotenv
```

- `black` – Python code formatter.
- `isort` – Organizes Python imports.
- `langchain` – Framework for building LLM applications.
- `langchain-ollama` – Integrates LangChain with Ollama.
- `python-dotenv` – Loads environment variables from a `.env` file.


### 3. Set Up Ollama

Install Ollama from https://ollama.com/.

Download the model used in the code:

```bash
ollama pull gpt-oss
```

Ensure Ollama is running before executing the Python script.

### 4. Configure Environment Variables (Optional)

Create a `.env` file to enable LangSmith tracing:

```env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://apac.api.smith.langchain.com
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=my-first-project
```

Replace the API key placeholder with your own key. Keep your `.env` file private and never commit your actual API key to GitHub.

### 5. Run the Code

```bash
python __init__.py
```

Replace `__init__.py` with the actual filename of your Python script if necessary.


## Learning Outcome

Through this example, I learned how to create a prompt template, connect a local language model with LangChain, build a basic chain, and generate responses from input data.

This is my first step toward understanding how LLM-powered applications work using LangChain.

---

*Part of my hands-on journey to learning LangChain and building LLM applications with Python.*
