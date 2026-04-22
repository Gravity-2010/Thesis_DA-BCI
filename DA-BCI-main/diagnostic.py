import scipy.io as sio
import numpy as np

# HARDCODED PATH for the final check
file_path = "C:/Users/Garvita/Documents/Thesis/Thesis_DA-BCI/DA-BCI-main/data/processed/A04TClass4.mat"

try:
    mat_data = sio.loadmat(file_path)
    # Find the key (Class1, Class2, etc.)
    key = [k for k in mat_data.keys() if not k.startswith('__')][0]
    actual_shape = mat_data[key].shape

    print("--- FINAL SHAPE AUDIT ---")
    print(f"File: {file_path}")
    print(f"Key found: {key}")
    print(f"Your Data Shape: {actual_shape}")

    # Expectations
    expected = (22, 1000, 72)
    
    if actual_shape == expected:
        print("\n✅ PERFECT MATCH! The data is exactly what the paper needs.")
    else:
        print("\n❌ MISMATCH FOUND.")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual_shape}")

except Exception as e:
    print(f"Error: Could not find or read the file. {e}")