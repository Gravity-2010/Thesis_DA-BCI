import scipy.io as sio
import os
import setting as st

def audit_raw_data():
    raw_folder = "C:/Users/Garvita/Documents/Thesis/Thesis_DA-BCI/DA-BCI-main/data/raw/"
    subjects = range(1, 10)
    
    print(f"{'Subj':<5} | {'Keys':<20} | {'Shape':<20} | {'Status'}")
    print("-" * 65)

    for sbj in subjects:
        file_name = f"A{sbj:02d}T.mat"
        full_path = os.path.join(raw_folder, file_name)
        
        if not os.path.exists(full_path):
            print(f"{sbj:<5} | {'FILE NOT FOUND':<40}")
            continue
            
        try:
            mat = sio.loadmat(full_path)
            # Filter out metadata keys like __header__
            data_keys = [k for k in mat.keys() if not k.startswith('__')]
            
            # We assume the main data is in the first non-metadata key
            main_key = data_keys[0]
            shape = mat[main_key].shape
            
            # Check for dimension consistency (Expecting 22 channels, ~1000+ time, 288 trials)
            status = "OK" if shape[0] == 22 else "WARN: CHANNELS"
            
            print(f"{sbj:<5} | {str(data_keys):<20} | {str(shape):<20} | {status}")
            
        except Exception as e:
            print(f"{sbj:<5} | Error: {str(e)}")

if __name__ == "__main__":
    audit_raw_data()