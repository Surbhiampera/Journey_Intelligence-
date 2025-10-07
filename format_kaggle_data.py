import pandas as pd
import os
from datetime import datetime

def format_kaggle_datasets(input_folder):
    # Find all CSV files in the folder
    csv_files = [f for f in os.listdir(input_folder) if f.endswith(".csv")]
    if not csv_files:
        print("No CSV files found in the folder.")
        return

    all_formatted_data = []

    # Process each CSV file
    for csv_file in csv_files:
        file_path = os.path.join(input_folder, csv_file)
        print(f"Processing file: {file_path}")

        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            print(f"Error reading {csv_file}: {e}")
            continue

        # Create formatted DataFrame structure
        formatted_df = pd.DataFrame(columns=[
            'user_id', 'session_id', 'timestamp', 'page_visited', 'action_type',
            'step_in_funnel', 'dropoff_flag', 'device_type', 'location',
            'time_spent_on_page', 'conversion'
        ])

        n = len(df) if len(df) > 0 else 3  # handle empty file
        formatted_df['user_id'] = df.get('user_id', ['U101', 'U102', 'U103'] * (n // 3 + 1))[:n]
        formatted_df['session_id'] = df.get('session_id', ['S001', 'S002', 'S003'] * (n // 3 + 1))[:n]
        formatted_df['timestamp'] = df.get('timestamp', pd.date_range('2025-10-06 10:00', periods=n, freq='min'))
        formatted_df['page_visited'] = df.get('page_visited', ['homepage', 'login_page', 'loan_application'] * (n // 3 + 1))[:n]
        formatted_df['action_type'] = df.get('action_type', ['page_view', 'click_login', 'form_submit'] * (n // 3 + 1))[:n]
        formatted_df['step_in_funnel'] = df.get('step_in_funnel', list(range(1, n + 1)))
        formatted_df['dropoff_flag'] = df.get('dropoff_flag', [0] * n)
        formatted_df['device_type'] = df.get('device_type', ['mobile', 'desktop'] * (n // 2 + 1))[:n]
        formatted_df['location'] = df.get('location', ['Delhi', 'Mumbai'] * (n // 2 + 1))[:n]
        formatted_df['time_spent_on_page'] = df.get('time_spent_on_page', [45, 10, 120, 30] * (n // 4 + 1))[:n]
        formatted_df['conversion'] = df.get('conversion', [0, 0, 0, 1] * (n // 4 + 1))[:n]

        all_formatted_data.append(formatted_df)

    # Combine all formatted data
    combined_df = pd.concat(all_formatted_data, ignore_index=True)

    # Save output file
    output_file = os.path.join(os.path.dirname(input_folder), "formatted_kaggle_data.csv")
    combined_df.to_csv(output_file, index=False)
    print(f"\n Formatted dataset saved successfully at:\n{output_file}")

if __name__ == "__main__":
    input_folder = "/home/ampara/Downloads/kaggle_dataset_formatter/User_ journey"

    if os.path.isdir(input_folder):
        format_kaggle_datasets(input_folder)
    else:
        print("Folder not found. Please check the path.")
