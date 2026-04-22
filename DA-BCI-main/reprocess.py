import scipy.io as sio
import numpy as np
import os

# --- PATH CONFIGURATION ---
# We define these explicitly here to ensure the script works independently
RAW_DIR = "C:/Users/Garvita/Documents/Thesis/Thesis_DA-BCI/DA-BCI-main/data/raw/"
PROCESSED_DIR = "C:/Users/Garvita/Documents/Thesis/Thesis_DA-BCI/DA-BCI-main/data/processed/"

# Ensure the processed folder exists
if not os.path.exists(PROCESSED_DIR):
    os.makedirs(PROCESSED_DIR)
    print(f"Created folder: {PROCESSED_DIR}")

def extract_subject_data(sbj):
    raw_path = os.path.join(RAW_DIR, f"A{sbj:02d}T.mat")
    
    if not os.path.exists(raw_path):
        print(f"Skipping Subject {sbj}: Raw file not found at {raw_path}")
        return
        
    mat = sio.loadmat(raw_path)
    runs = mat['data'][0] 
    
    # Storage for the 4 classes
    class_data = {1: [], 2: [], 3: [], 4: []}

    for run_idx, run in enumerate(runs):
        # Access the structured data inside each run [0,0]
        structure = run[0,0]
        eeg = structure['X']      # Full EEG (Samples x 25)
        trials = structure['trial'].flatten() # Start indices
        labels = structure['y'].flatten()     # Class labels (1,2,3,4)
        
        for i in range(len(trials)):
            # MI usually starts at 2s (500 samples) and ends at 6s (1500 samples)
            # We take a 1000-sample window
            start_idx = int(trials[i] + 500)
            end_idx = int(start_idx + 1000)
            
            if end_idx <= eeg.shape[0]:
                # Slice first 22 channels and transpose to (Channels, Time)
                # This ensures the [22, 1000] shape for each trial
                trial_segment = eeg[start_idx:end_idx, :22].T 
                
                label = int(labels[i])
                if label in class_data:
                    class_data[label].append(trial_segment)

    # Save the 4 separate class files for this subject
    for cls_id in range(1, 5):
        if len(class_data[cls_id]) > 0:
            final_arr = np.stack(class_data[cls_id], axis=2) # (22, 1000, Trials)
            save_path = os.path.join(PROCESSED_DIR, f"A{sbj:02d}TClass{cls_id}.mat")
            sio.savemat(save_path, {f"Class{cls_id}": final_arr})
            print(f"Subject {sbj} | Class {cls_id} | Trials: {final_arr.shape[2]}")

if __name__ == "__main__":
    print("Starting Reprocessing...")
    for s in range(1, 10):
        extract_subject_data(s)
    print("\nReprocessing Complete. Check your 'data/processed' folder.")