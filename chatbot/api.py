from google import genai
from config import MODEL_NAME

client = genai.Client()

def create_chat(system_prompt):
    return client.chats.create(
        model = MODEL_NAME, 
        config = genai.types.GenerateContentConfig(
            system_instruction = system_prompt))

def send_message(chat_app, user_input):
    response = chat_app.send_message(user_input)
    return response.text

def generate_summary(chat_app, messages, exist=None):
    if not messages:
        return ''
    
    summary_prompt = ''
    if exist:
        summary_prompt += f'Summary : {exist}'

    summary_prompt = 'Summarize:\n'
    summary_prompt += '\n'.join(f'{role}: {msg}' for role, msg in messages)
    response = chat_app.send_message(summary_prompt)
    return response.text.strip()