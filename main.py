import torch
from pytorch_lightning import LightningModule, Trainer
import torchaudio
from torchaudio.models import Tacotron2
from torch.utils.data import DataLoader
from pathlib import Path

class Tacotron2TTS(LightningModule):

    def __init__(self, cfg):
        super().__init__()
        self.model = Tacotron2(cfg)
        self.dataset = torchaudio.datasets.LJSPEECH(root=str(Path("dataset").absolute()), download = False)

    def forward(self, text):
        mel_spectrogram = self.model(text)
        return mel_spectrogram

    def training_step(self, batch, batch_idx):
        text, mel_spectrogram = batch
        mel_spectrogram_pred = self(text)
        loss = torch.nn.functional.mse_loss(mel_spectrogram_pred, mel_spectrogram)
        self.log("train_loss", loss)
        return loss
    
    def train_dataloader(self):
        return DataLoader(self.dataset, batch_size=1, shuffle=True)

    def validation_step(self, batch, batch_idx):
        text, mel_spectrogram = batch
        mel_spectrogram_pred = self(text)
        loss = torch.nn.functional.mse_loss(mel_spectrogram_pred, mel_spectrogram)
        self.log("val_loss", loss)

    def test_step(self, batch, batch_idx):
        text, mel_spectrogram = batch
        mel_spectrogram_pred = self(text)
        loss = torch.nn.functional.mse_loss(mel_spectrogram_pred, mel_spectrogram)
        self.log("test_loss", loss)

    def configure_optimizers(self):
        return torch.optim.Adam(self.model.parameters(), lr=1e-3)

if __name__ == "__main__":
    cfg = {
        "model": {
            "num_mels": 80,
            "hidden_channels": 128,
            "attention_dim": 128,
        },
        "trainer": {
            "max_epochs": 10,
        },
    }

    model = Tacotron2TTS(cfg)
    trainer = Trainer(accelerator='cpu') # use gpu when
    trainer.fit(model)