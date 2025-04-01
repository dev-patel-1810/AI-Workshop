import os
from openai import OpenAI

key=1
# Initialize the OpenAI client
client = OpenAI(key)

# Optional: Test the connection
try:
    models = client.models.list()
    print("✅ Successfully connected to OpenAI!")
except Exception as e:
    print(f"❌ Error connecting to OpenAI: {e}")
    
def get_completion(prompt, model="gpt-4o-mini"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages, # type: ignore
        temperature=0
    )
    return response.choices[0].message.content


# Example usage
while True:
  l1=['Jee Mains', 'NEET', 'CUET']
  l2=['Gate','CSIR-NET']
  l3=['CAT', 'UPSC','XAT']
  l11=['FIIT JEE','PW', 'Allen','VMC']
  l21=['MADE-EASY', 'PIE-AIM','DIPS','Unacademy','PW']
  l32=['Drishti IAS', 'Vision IAS', 'Vajirao']
  l31=['TIME','IMS']
  prompt = input("Enter: ")
  if prompt == "" or prompt==" ":
    break;
  if prompt.lower()=='jee mains' or prompt.lower()=='jee main':
    response = get_completion(prompt)
    print(response)
    print(get_completion(prompt='What are the expeted dates of JEE Mains 2025? '))
    print("If you are an Undergraduate from science background then you can also apply for ",l1)
    print("Some known institutes" ,l11)
  elif prompt.lower()=='neet':
    response = get_completion(prompt)
    print(response)
    print(get_completion(prompt='What are the expeted dates of NEET 2025'))
    print("If you are an Undergraduate from science background then you can also apply for ",l1)
    print("Some known institutes" ,l11)
  elif prompt.lower()=='cuet':
    response = get_completion(prompt)
    print(response)
    print(get_completion(prompt='What are the expeted dates of CUET 2025? '))
    print("If you are an Undergraduate from science background then you can also apply for ",l1)
    print("Some known institutes" ,l11)
  elif prompt.lower()=='gate':
    response = get_completion(prompt)
    print("THIS IS FOR NATIONAL AS WELL AS INTERNATIONAL EXAMS")
    print(response)
    print(get_completion(prompt='What are the expeted dates of GATE 2025? '))
    print("If you are an graduate from science background then you can also apply for ",l2)
    print("Some known institutes" ,l21)
  elif prompt.lower()=='csir-net':
    response = get_completion(prompt)
    print(response)
    print(get_completion(prompt='What are the expeted dates of CSIR-NET 2025? '))
    print("If you are an graduate from science background then you can also apply for ",l2)
    print("Some known institutes" ,l21)
  elif prompt.lower()=='cat':
    response = get_completion(prompt)
    print(response)
    print(get_completion(prompt='What are the expeted dates of CAT 2025? '))
    print("If you are an graduate from any background then you can also apply for ",l3)
    print("Some known institutes" ,l31)
  elif prompt.lower()=='upsc':
    response = get_completion(prompt)
    print(response)
    print(get_completion(prompt='What are the expeted dates of UPSC 2025? '))
    print("If you are an graduate from any background then you can also apply for ",l3)
    print("Some known institutes", l32)
  elif prompt.lower()=='xat':
    response = get_completion(prompt)
    print(response)
    print(get_completion(prompt='What are the expeted dates of XAT 2025? '))
    print("If you are an graduate from any background then you can also apply for ",l3)
    print("Some known institutes" ,l32)



  if 'science' in prompt.lower():
    print("For UG your options are",l1)
    print("For Post Graduate your options are",l2,l3)
  elif 'commerce' in prompt.lower():
    print("For UG your options is CUET",)
    print("For Post Graduate your options are",l3)
  elif 'arts' in prompt.lower():
    print("For UG your options is CUET",)
    print("For Post Graduate your options are",l3)
  else:
    response = get_completion(prompt)
    print(response)
