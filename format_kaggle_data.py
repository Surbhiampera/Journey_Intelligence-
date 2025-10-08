import pandas as pd
import os
from datetime import datetime
import itertools

def repeat_to_length(lst, length):
    """Repeat list elements until desired length is reached"""
    return list(itertools.islice(itertools.cycle(lst), length))

def format_kaggle_datasets(input_folder):
    csv_files = [f for f in os.listdir(input_folder) if f.endswith(".csv")]
    if not csv_files:
        print("No CSV files found in the folder.")
        return

    all_formatted_data = []

    for csv_file in csv_files:
        file_path = os.path.join(input_folder, csv_file)
        print(f"Processing file: {file_path}")

        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            print(f"Error reading {csv_file}: {e}")
            continue

        n = len(df) if len(df) > 0 else 5

        formatted_df = pd.DataFrame(columns=[
            'user_id', 'session_id', 'event_time', 'page_name', 'event_type',
            'event_value', 'device_type', 'location', 'duration_on_page',
            'referrer_page', 'next_page', 'conversion_flag', 'funnel_stage',
            'intent_label', 'recommendation_shown', 'recommendation_clicked',
            'cluster_id', 'score_intent_probability'
        ])

        # ✅ Use df.get() if present, otherwise repeat dummy defaults to match n
        formatted_df['user_id'] = df.get('user_id', repeat_to_length(['U1023', 'U1044', 'U1089', 'U1090', 'U1101'], n))
        formatted_df['session_id'] = df.get('session_id', repeat_to_length(['S5502', 'S5503', 'S5504', 'S5505', 'S5506'], n))
        formatted_df['event_time'] = df.get('event_time', pd.date_range('2025-10-07 15:00', periods=n, freq='min').astype(str))
        formatted_df['page_name'] = df.get('page_name', repeat_to_length(['Home_Page', 'Loan_Offers_Page', 'Loan_Apply_Page', 'Payment_Page', 'Success_Page'], n))
        formatted_df['event_type'] = df.get('event_type', repeat_to_length(['view', 'click', 'submit'], n))
        formatted_df['event_value'] = df.get('event_value', repeat_to_length(['View Loan Details', 'Apply Now', 'Submit Application', 'Payment', 'Confirmation'], n))
        formatted_df['device_type'] = df.get('device_type', repeat_to_length(['mobile', 'desktop', 'tablet'], n))
        formatted_df['location'] = df.get('location', repeat_to_length(['Mumbai, IN', 'Delhi, IN', 'Chennai, IN', 'Pune, IN', 'Bangalore, IN'], n))
        formatted_df['duration_on_page'] = df.get('duration_on_page', repeat_to_length([24.5, 12.0, 35.2, 15.8, 28.9], n))
        formatted_df['referrer_page'] = df.get('referrer_page', repeat_to_length(['Home_Page', 'Loan_Offers_Page', 'Loan_Apply_Page'], n))
        formatted_df['next_page'] = df.get('next_page', repeat_to_length(['Loan_Apply_Page', 'Payment_Page', 'Success_Page', 'Logout_Page'], n))
        formatted_df['conversion_flag'] = df.get('conversion_flag', repeat_to_length([0, 1], n))
        formatted_df['funnel_stage'] = df.get('funnel_stage', repeat_to_length(['Offer_View', 'Apply_Loan', 'Payment', 'Success'], n))
        formatted_df['intent_label'] = df.get('intent_label', repeat_to_length(['Apply_Loan', 'Purchase', 'Query_Info', 'Upgrade', 'Renewal'], n))
        formatted_df['recommendation_shown'] = df.get('recommendation_shown', repeat_to_length(['Personal Loan Banner', 'Credit Card Offer', 'Insurance Plan'], n))
        formatted_df['recommendation_clicked'] = df.get('recommendation_clicked', repeat_to_length([0, 1], n))
        formatted_df['cluster_id'] = df.get('cluster_id', repeat_to_length(['C1', 'C2', 'C3', 'C4', 'C5'], n))
        formatted_df['score_intent_probability'] = df.get('score_intent_probability', repeat_to_length([0.87, 0.75, 0.65, 0.92, 0.81], n))

        all_formatted_data.append(formatted_df)

    combined_df = pd.concat(all_formatted_data, ignore_index=True)
    output_file = os.path.join(os.path.dirname(input_folder), "formatted_user_journey_data.csv")
    combined_df.to_csv(output_file, index=False)
    print(f"\n Formatted dataset saved successfully at:\n{output_file}")

if __name__ == "__main__":
    input_folder = "/home/ampara/Downloads/kaggle_dataset_formatter/User_ journey"
    input_folder = input_folder.strip()

    if os.path.isdir(input_folder):
        format_kaggle_datasets(input_folder)
    else:
        print(f"Folder not found. Please check the path:\n{input_folder}")
