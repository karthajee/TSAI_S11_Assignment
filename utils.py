import torch
import torch.nn as nn
import torch.functional as F

def get_device():
    device = 'cuda' if torch.cuda.is_available() else "cpu"
    return device

def print_summary():
    ...