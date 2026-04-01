import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
class DataLoader():
     def __init__(self, tokenizer, dataset):
          self.tokenizer = tokenizer
          self.dataset = dataset
          encodings = tokenizer(
              dataset,
              return_tensors='pt'
          )
          self.enc_ds = encodings['input_ids'].squeeze(0)
          
     def load(self, batch_size, seq_len):
          B = batch_size
          T = seq_len
          ix = torch.randint(len(self.enc_ds) - T, (B,))
          indices = ix.view(-1, 1) + torch.arange(T)
          X = self.enc_ds[indices]
          y = self.enc_ds[indices+1]
          return X.to(device), y.to(device)
     