from dotenv import load_dotenv
load_dotenv() # .env 파일이 있다면, 환경변수로써 로딩


from openai import OpenAI
client = OpenAI()  

stream = client.responses.create(
    model="gpt-4o",
    input="make python code for factorial. 코드로만 응답해.",
    stream=True,
)

for event in stream:
    if hasattr(event, "delta"):
        print(event.delta , end="", flush=True)