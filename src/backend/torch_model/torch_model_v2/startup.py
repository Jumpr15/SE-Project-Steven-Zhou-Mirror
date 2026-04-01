from modelConfig import ModelConfig

from model import Model
from dataloader import DataLoader

from tokenizer import train_bpe_tokenizer
from training import model_pretraining

import torch
import datasets
from datasets import load_dataset
from transformers import PreTrainedTokenizerFast

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# entrypoint
## example model config
model_config = ModelConfig(
     dataset="roneneldan/TinyStories", # ds, or "ajibawa-2023/Children-Stories-Collection"
     vocab_size=8000, # vocab size
     batch_size=192, # batch size,
     seq_len=256, # seq len
     head_size=64, # head_size
     embed_dims=512, # embed dims
     block_num=6, # block nums
     lr=1e-3, # lr
     iterations=1000
)

if __name__ == "__main__":
     # sets internal precision of torch float32 matmul
     torch.set_float32_matmul_precision('high')
     
     # load and joins HF downloaded dataset
     ds = load_dataset(model_config.dataset)
     joined_ds = ''.join(ds['train']['text'][:3000])

     # trained custom BPE tokenizer on dataset
     # tokenizer = train_bpe_tokenizer(
     #      model_config.dataset, 
     #      model_config.vocab_size
     # )

     tokenizer = PreTrainedTokenizerFast.from_pretrained("TinyStories_BPE_8K")
     
     # initialize dataloader
     dataloader = DataLoader(
          tokenizer,
          joined_ds
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
     
     torch.save(model.state_dict(), "model_state/TinyStories2.pt")
     
# input = helper.encode("lorem ipsum ")
# input_toks = torch.unsqueeze(input, dim=0).to(device)
# out_toks = model.generate(input_toks, 50)
# print(helper.encoder.decode(out_toks[0].tolist()))

# torch.save(model.state_dict(), "workspace/server/children_stories_model_weights2.pt")