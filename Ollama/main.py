import json
from difflib import get_close_matches
from ollama import chat
from prompts import ep, prompt, jp

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.8) # Adjust cut-off to set accuracy of matching the queries with the knowledge base
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
        

def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')
    conversation_history: list[dict] = []

    while True:
        user_input: str = input('\n\nYou: ')

        if user_input.lower() == 'quit':
            break

        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            conversational_answer = make_conversational_with_llama(prompt + user_input + answer)
            conversation_history.append({'role': 'user', 'content': user_input})
            conversation_history.append({'role': 'assistant', 'content': conversational_answer})
            print()

        else:
            messages = [{'role': 'user', 'content': jp + user_input}]
            llama_answer = ''
            for part in chat('llama3', messages=messages, stream=True):
                print(part['message']['content'], end='', flush=True)
                llama_answer += part['message']['content']
            conversation_history.append({'role': 'user', 'content': user_input})
            conversation_history.append({'role': 'assistant', 'content': llama_answer})    
            print()
            continue

def make_conversational_with_llama(answer: str) -> str:
    # Passing the answer to LLM for further processing to make it conversational
    messages = [{'role': 'user', 'content': answer}]
    llama_conversational_answer = ''
    for part in chat('llama2', messages=messages, stream=True):
        print(part['message']['content'], end='', flush=True)
        llama_conversational_answer += part['message']['content']
    print()


if __name__ == '__main__':
    chat_bot()
