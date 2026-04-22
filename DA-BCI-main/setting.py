import os

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path

# current_folder = os.path.dirname(os.path.abspath(__file__))
path = "C:/Users/Garvita/Documents/Thesis/Thesis_DA-BCI/DA-BCI-main/"
data_path = "C:/Users/Garvita/Documents/Thesis/Thesis_DA-BCI/data/processed/"
model_path = create_dir(path + "model/")

# Hyperparameters
channel_cnt = 22
window_size = 512
learning_rate = 0.0001
total_epoch = 50
eval_epoch = 1
window_number = 189
fs= 32

low = 8
high = 30

batch_size_tr = 32
batch_size_val = window_number

tgt = 1
src = 2