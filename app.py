# LangChain
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate

# Environment Variables
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key="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"

llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key, model_name='gpt-3.5-turbo')

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")

# Example usage
file_path = 'tiny_shakespear.txt'
file_contents = read_text_file(file_path)
#file_contents= file_contents[0:10000]

def shakespeare(task):
  file_contents=read_text_file("tiny_shakespear.txt")
  file_contents=file_contents[0:10000]
  template = """
  % INSTRUCTIONS
  - You are an AI Bot that has knowledge in every field.
  - Do not use hashtags or emojis
  - Respond in the tone of Shakespeare.
  % Authors writing samples
  {file_contents}
  % YOUR TASK
  {task}.
  """
  #task=input("Ask me anything: ")
  #file_contents=file_contents[0:10000]

  prompt = PromptTemplate(
      input_variables=["file_contents","task"],
      template=template,
  )

  final_prompt = prompt.format( file_contents=file_contents,task=task)

  return llm.predict(final_prompt)

import gradio as gr
task = gr.inputs.Textbox(lines=5, label="Input Text")
output_text = gr.outputs.Textbox(label="Generated Text")
iface = gr.Interface(
    fn=shakespeare,
    inputs=task,
    outputs=output_text,
    title="TINY SHAKESPEARE",
    description="",
    theme="default"
)

# Run the interface
iface.launch()
