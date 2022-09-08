#Source for the code example:
#Dey, Victor, https://analyticsindiamag.com/how-to-paraphrase-text-using-pegasus-transformer/

#importing the PEGASUS Transformer model
import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

model_name = 'tuner007/pegasus_paraphrase'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(
  model_name).to(torch_device)

#setting up the model


def get_response(input_text, num_return_sequences):
  batch = tokenizer.prepare_seq2seq_batch(
    [input_text], truncation=True, padding='longest', max_length=60, return_tensors="pt").to(torch_device)
  translated = model.generate(**batch, max_length=60, num_beams=10,
                              num_return_sequences=num_return_sequences, temperature=1.5)
  tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
  return tgt_text

#Another test for commit
#Test for a commit
#test input sentence
text = "I will be showing you how to build a web application in Python using the SweetViz and its dependent library."

#printing response
get_response(text, 5)
