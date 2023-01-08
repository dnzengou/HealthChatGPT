import os
import openai
import gradio as gr

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
openai.api_key = "xxx"

start_sequence = "\nAI:"
restart_sequence = "\nDu: "

prompt = "\n\nDu: Hej, vem är du?\nAI: Jag är en AI skapad av OpenAI. Hur kan jag hjälpa dig idag?\nMänniskan:"

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks(css=".gradio-container {background-color: lightblue; background-image: url('https://static.nichehuset.dk/annoncer/jobannoncer/images/annoncoerer/logoer_thumbnails/2123/1323.png'); background-repeat:no-repeat; width=100%; height=100%}")


with block:
    gr.Markdown("""<h1 style="color:#ffffff"><center>Personlig Hälsorådgivare</center></h1> \n\n<i style="color:#ffffff"><center>Byggd med OpenAI ChatGPT API & Gradio</center></i>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SKICKA")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True, share = True)
