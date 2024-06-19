# Olivia: Your Own Private AI using Ollama

<img src="Ollama/logo.png" alt="Olivia Logo" width="400">

This project is a conversational chatbot named **Olivia**, designed to provide intelligent responses using a combination of a local knowledge base and various offline language models available through Ollama, ensuring privacy and no dependency on external APIs. Olivia first attempts to find a close match to the user's question within a predefined knowledge base. If a match is found, it provides a conversational answer generated by an offline language model (e.g., Llama 2, Llama 3, Mistral, Gemma). If no match is found, the bot utilizes the local model to generate a response dynamically. Just add whatever knowledge you want to add in the json syntax, even if its a one word answer, my chatbot is gonna make it conversational when asked :)

## Features

- **Knowledge Base Integration**: Quickly retrieves answers from a pre-defined set of questions and answers stored locally.
- **Local Language Models**: Utilizes offline models (Llama 2, Llama 3, Mistral, Gemma, etc.) available through Ollama, ensuring privacy and no dependency on external APIs.
- **Real-time Interaction**: Engages in real-time conversations with users.
- **Conversational Enhancement**: Improves static knowledge base answers to be more conversational using offline models.

## How It Works

1. **Load Knowledge Base**: The bot loads questions and answers from a JSON file (`knowledge_base.json`).
2. **User Interaction**: Accepts user input and checks for a close match in the knowledge base.
3. **Best Match Retrieval**: If a close match is found, retrieves the corresponding answer.
4. **Conversational Response**: Enhances the static answer to be conversational using an offline model.
5. **Dynamic Response**: If no match is found, dynamically generates a response using an offline model.
6. **Conversation History**: Maintains a history of the conversation for context.

## Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/Olivia-Chatbot-Ollama.git
    cd Olivia-Chatbot-Ollama
    ```

2. **Install Dependencies**:
    Ensure you have the required dependencies installed. This can include Python libraries and the Ollama software with the necessary models downloaded.

3. **Run the Chatbot**:
    ```bash
    python main.py
    ```

4. **Interact with the Bot**: 
    - Type your questions and receive responses.
    - Type `quit` to end the conversation.

## Files and Directories

- `main.py`: Main script to run the chatbot.
- `knowledge_base.json`: JSON file containing the questions and answers.
- `prompts.py`: Contains prompt strings used in the chatbot.

## Requirements
```install Ollama and Local LLM
- Download: https://ollama.com/
- Download LLM (Example): ollama run llama2
- pip install ollama
```

## Example

```plaintext
You: What is the capital of France?
Olivia: The capital of France is Paris.

You: Tell me something interesting about Paris.
Olivia: Did you know that Paris is known as the "City of Light"? It's a major European city and a global center for art, fashion, and culture.

You: quit
