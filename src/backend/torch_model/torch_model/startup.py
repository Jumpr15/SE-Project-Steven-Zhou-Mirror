from backend.torch_model.torch_model.modelConfig import ModelConfig

from model import Model
from dataloader import DataLoader

from tokenizer import train_bpe_tokenizer
from training import model_pretraining

import torch
import datasets
from datasets import load_dataset

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# entrypoint
## example model config
model_config = ModelConfig(
     "roneneldan/TinyStories", # ds, or "ajibawa-2023/Children-Stories-Collection"
     8000, # vocab size
     16, # batch size,
     1024, # seq len
     64, # head_size
     512, # embed dims
     6, # block nums
     1e-3, # lr
     10000
)

if __name__ == "__main__":
     # sets internal precision of torch float32 matmul
     torch.set_float32_matmul_precision('high')
     
     # load and joins HF downloaded dataset
     ds = load_dataset(model_config.dataset)
     joined_ds = ''.join(ds['train']['text'])
     
     # length of dataset
     print(len(joined_ds))
     
     # trained custom BPE tokenizer on dataset
     tokenizer = train_bpe_tokenizer(
          model_config.dataset, 
          model_config.vocab_size
     )
     
     # initialize dataloader
     dataloader = DataLoader(
          tokenizer,
          ds
     )
     
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

     model_pretraining(
          model, 
          dataloader, 
          model_config.iterations,
          model_config.batch_size,
          model_config.seq_len
     )
     
     torch.save(model.state_dict(), "model_state/TinyStories1.py")
     
# input = helper.encode("lorem ipsum ")
# input_toks = torch.unsqueeze(input, dim=0).to(device)
# out_toks = model.generate(input_toks, 50)
# print(helper.encoder.decode(out_toks[0].tolist()))

# torch.save(model.state_dict(), "workspace/server/children_stories_model_weights2.pt")