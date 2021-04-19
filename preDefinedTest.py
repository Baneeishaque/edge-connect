import os
from shutil import copyfile
from src.config import Config
from src.edge_connect import EdgeConnect
import cv2
import random
import numpy as np
import torch

# Default Config. on places2
places2CheckPointsPath = './checkpoints/places2'
config_path = os.path.join(places2CheckPointsPath, 'config.yml')
# create checkpoints path if doesn't exist
if not os.path.exists(places2CheckPointsPath):
    os.makedirs(places2CheckPointsPath)
copyfile('./config.yml.example', config_path)
# load config file
config = Config(config_path)

config.MODE = 2
config.MODEL = 3
config.INPUT_SIZE = 0

config.TEST_FLIST = './compositeImage_01.png'
config.TEST_MASK_FLIST = './invertedBinaryDepthMapImageWithClosingOpeningAndErosion_01.png'
config.RESULTS = './checkpoints/results'

# cuda visible devices
os.environ['CUDA_VISIBLE_DEVICES'] = ','.join(str(e) for e in config.GPU)

# init device
if torch.cuda.is_available():
    config.DEVICE = torch.device("cuda")
    torch.backends.cudnn.benchmark = True  # cudnn auto-tuner
else:
    config.DEVICE = torch.device("cpu")

# set cv2 running threads to 1 (prevents deadlocks with pytorch dataloader)
cv2.setNumThreads(0)

# initialize random seed
torch.manual_seed(config.SEED)
torch.cuda.manual_seed_all(config.SEED)
np.random.seed(config.SEED)
random.seed(config.SEED)

# build the model and initialize
model = EdgeConnect(config)
model.load()

print('\nstart testing...\n')
model.test()
