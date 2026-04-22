import scipy.io as sio
import numpy as np

# Let's check Subject 1 (the standard) and Subject 4 (the anomaly)
for sbj in [1, 4]:
    path = f"C:/Users/Garvita/Documents/Thesis/Thesis_DA-BCI/DA-BCI-main/data/raw/A{sbj:02d}T.mat"
    mat = sio.loadmat(path)
    
    # Access the first element of the 'data' container
    # mat['data'][0, 0] usually contains the first session's structured data
    inner_data = mat['data'][0, 0]
    
    print(f"\n--- Deep Audit Subject {sbj} ---")
    print(f"Type of inner data: {type(inner_data)}")
    
    # If it's a structured array, let's see its fields
    if hasattr(inner_data, 'dtype'):
        print(f"Fields found: {inner_data.dtype.names}")
        # Try to find the EEG signal (often named 'X' or 'trial')
        for name in inner_data.dtype.names:
            val = inner_data[name][0,0]
            if hasattr(val, 'shape'):
                print(f"  -> Field '{name}' shape: {val.shape}")