import torch
import torch.nn as nn

class FC(nn.Module):
    def __init__(self, in_features, out_features, activation='relu'):
        super(FC, self).__init__()
        self.fc = nn.Linear(in_features, out_features)
        if activation == 'relu':
            self.act = nn.ReLU(inplace=True)

    def forward(self, x):
        x = self.fc(x)
        if self.act is not None:
            x = self.act(x)
        return x

class Conv2d(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=1, stride=1, padding=0, bn=True, activation='relu'):
        super(FC, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size, stride=stride, padding=padding)
        if self.bn:
            self.bn = nn.BatchNorm2d(out_channels)
        if self.activation == 'relu':
            self.act = nn.ReLU(inplace=True)
        
    def forward(self, x):
        x = self.conv(x)
        if self.bn:
            x = self.bn(x)
        if self.act:
            x = self.act(x)
        return x
