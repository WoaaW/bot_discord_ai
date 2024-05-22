from openai import OpenAI

def get_response(user_input:str, ai:OpenAI) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return "Silence..."
    
    else:
        completition = ai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role" : "system", "content":"Tu es un poète très talentueux qui ne réponds seulement en Alexandrin."},
                {"role":"user", "content":user_input} 
            ]
        )
        print(completition.choices[0].message)
        return completition.choices[0].message.content