import torch.amp as amp

def model_pretraining(model, dataloader, iterations, batch_size, seq_len):
     for epoch in range(iterations):
          X, y = dataloader.load(batch_size, seq_len)
          with amp.autocast(device_type="cuda"):
               output = model.forward(X, targets=y)
               