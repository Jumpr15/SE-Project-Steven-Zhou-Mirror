# from model_inference.modelInference import model_inference
from modelInference import model_inference #### change later

model = model_inference()

prompt = input("Text prompt: ")

streamed_response = model.streamed_text_generation("sam860/LFM2:350m", prompt)

for chunk in streamed_response:
     print(chunk['message']['content'], end="")