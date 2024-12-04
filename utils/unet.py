class P_UNet(UNet2DConditionModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 添加并初始化PTCA和PICA模块
        self.ptca = PTCA(self.config.block_out_channels[-1])
        self.pica = PICA(self.config.block_out_channels[-1])

    def forward(self, x, timesteps, context=None, **kwargs):
        # 实现P-UNet的前向传播逻辑
        hidden_states = x
        
        # 执行原始UNet的前向传播
        hidden_states = super().forward(hidden_states, timesteps, context, **kwargs).sample
        
        # 应用PTCA模块
        hidden_states = self.ptca(hidden_states)
        
        # 应用PICA模块
        hidden_states = self.pica(hidden_states, context)
        
        return hidden_states
