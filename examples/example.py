from aifeynman import run_aifeynman
import time
import sys
import numpy as np
import os

def process_file(file_path):
    header = "Test Set Error, Cumulative Log, Complexity, Input Set Error, Symbolic Expression"
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    processed_lines = [header]
    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 6:
            numeric_parts = ' '.join(parts[:5])
            symbolic_expression = ' '.join(parts[5:])
            processed_lines.append(f"{numeric_parts} {symbolic_expression}")
    
    with open(file_path, 'w') as file:
        file.write('\n'.join(processed_lines))

def find_best_expression(file_path):
    best_error = float('inf')
    best_expression = ""

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:
                try:
                    error = float(parts[0])
                    expression = ' '.join(parts[5:])  # Join all parts from index 5 onwards
                    if error < best_error:
                        best_error = error
                        best_expression = expression
                except ValueError:
                    continue

    return best_error, best_expression

def add_noise(data, noise_level):
    noise = np.random.normal(0, noise_level * np.abs(data), data.shape)
    return data + noise

def test_noise_tolerance(pathdir, filename, noise_levels, BF_try_time=60, BF_ops_file_type="7ops.txt", polyfit_deg=3, NN_epochs=500):
    original_data = np.loadtxt(os.path.join(pathdir, filename))
    
    for noise_level in noise_levels:
        if noise_level == 0:
            noisy_data = original_data
            temp_filename = filename
        else:
            noisy_data = add_noise(original_data, noise_level)
            temp_filename = f"{os.path.splitext(filename)[0]}_noisy_{noise_level}{os.path.splitext(filename)[1]}"
            
        np.savetxt(os.path.join(pathdir, temp_filename), noisy_data)
        
        start_time = time.time()
        run_aifeynman(pathdir, temp_filename, BF_try_time, BF_ops_file_type, polyfit_deg, NN_epochs)
        end_time = time.time()
        execution_time = end_time - start_time
        
        result_filename = os.path.join("results", f"solution_{temp_filename}")
        process_file(result_filename)
        
        best_error, best_expression = find_best_expression(result_filename)
        
        # Append the best result to the solution file
        with open(result_filename, 'a') as file:
            file.write(f"\nBest Result: Noise Level: {noise_level} | Equation: {best_expression} with error of {best_error} | Solution time: {execution_time:.2f} seconds")
        
        if noise_level != 0:
            os.remove(os.path.join(pathdir, temp_filename))

# Main execution
if __name__ == "__main__":
    pathdir = "../example_data/"
    filename = "WaterlooEx1.txt"
    piname = "buckinghamWaterlooEx1.txt"
    noise_levels = [0.01] # Add noise levels to test here

    test_noise_tolerance(pathdir, filename, noise_levels)
    test_noise_tolerance(pathdir, piname, noise_levels)

