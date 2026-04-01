from modelConfig import ModelConfig
from model import Model

import torch
from transformers import PreTrainedTokenizerFast

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_config = ModelConfig(
     dataset="roneneldan/TinyStories", # ds, or "ajibawa-2023/Children-Stories-Collection"
     vocab_size=8000, # vocab size
     batch_size=16, # batch size,
     seq_len=256, # seq len
     head_size=64, # head_size
     embed_dims=512, # embed dims
     block_num=6, # block nums
     lr=1e-3, # lr
     iterations=1000
)

if __name__ == "__main__":
    model = Model(
        model_config.batch_size,
        model_config.seq_len,
        model_config.embed_dims,
        model_config.head_size,
        model_config.block_num,
        model_config.vocab_size,
        model_config.lr
    )
    
    model = model.to(device)
    model.load_state_dict(torch.load("model_state/TinyStories1.pt"))
    
    tokenizer = PreTrainedTokenizerFast.from_pretrained("TinyStories_BPE_8K")  
    encoded_prompt = tokenizer("The brick building ", return_tensors='pt')
    input_toks = encoded_prompt['input_ids'].squeeze(0)
    input_toks = torch.unsqueeze(input_toks, dim=0).to(device)
    out_toks = model.generate(input_toks, 500)
    print(tokenizer.decode(out_toks[0].tolist()))
