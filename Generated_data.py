import pandas as pd
import os
import numpy as np
from datetime import datetime, timedelta
import random

def generate_more_data(formatted_file, output_file, target_rows=10000):
    """
    Reads an already formatted dataset and generates more synthetic data
    while keeping the structure and distribution similar.
    """
    if not os.path.isfile(formatted_file):
        print("Formatted file not found.")
        return

    df = pd.read_csv(formatted_file)
    n_current = len(df)
    
    if n_current == 0:
        print("Formatted file is empty.")
        return

    print(f"Current dataset size: {n_current} rows")
    print(f"Generating {target_rows} rows of synthetic data...")

    new_rows = []
    
    for _ in range(target_rows):
        row = {
            'user_id': f"U{random.randint(1000, 9999)}",
            'session_id': f"S{random.randint(10000, 99999)}",
            'timestamp': (datetime.now() - timedelta(minutes=random.randint(0, 10000))).strftime('%Y-%m-%d %H:%M:%S'),
            'page_visited': random.choice(df['page_visited'].unique()),
            'action_type': random.choice(df['action_type'].unique()),
            'step_in_funnel': random.randint(1, df['step_in_funnel'].max()),
            'dropoff_flag': random.choice([0, 1]),
            'device_type': random.choice(df['device_type'].unique()),
            'location': random.choice(df['location'].unique()),
            'time_spent_on_page': random.choice(df['time_spent_on_page'].unique()),
            'conversion': random.choice([0, 1])
        }
        new_rows.append(row)

    synthetic_df = pd.DataFrame(new_rows)

    # Combine original and synthetic data
    combined_df = pd.concat([df, synthetic_df], ignore_index=True)
    
    # Save output
    combined_df.to_csv(output_file, index=False)
    print(f"Synthetic dataset saved at:\n{output_file}")
    print(f"Total rows: {len(combined_df)}")

if __name__ == "__main__":
    formatted_file = "/home/ampara/Downloads/kaggle_dataset_formatter/formatted_kaggle_data.csv"
    output_file = "/home/ampara/Downloads/kaggle_dataset_formatter/formattedSynthetic_data2k.csv"

    # Example: generate 20k more rows
    generate_more_data(formatted_file, output_file, target_rows=2000)
