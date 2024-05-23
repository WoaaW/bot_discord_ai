from openai import OpenAI

messages = []

def get_response(user_input:str, ai:OpenAI) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return "Silence..."
    
    else:
        messages.append({"role":"user", "content":user_input})
        completition = ai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages
        )
        print(completition.choices[0].message.role)
        messages.append({"role" : completition.choices[0].message.role, "content":completition.choices[0].message.content})
        return completition.choices[0].message.content
