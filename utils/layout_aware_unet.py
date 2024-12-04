import torch
from diffusers import UNet2DConditionModel

class LayoutAwareUNet(UNet2DConditionModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout_encoder = torch.nn.Conv2d(5, self.config.in_channels, kernel_size=3, padding=1)

    def forward(self, sample, timestep, encoder_hidden_states, layout=None, return_dict=True):
        if layout is not None:
            layout_encoding = self.layout_encoder(layout)
            sample = torch.cat([sample, layout_encoding], dim=1)
        
        return super().forward(sample, timestep, encoder_hidden_states, return_dict=return_dict)