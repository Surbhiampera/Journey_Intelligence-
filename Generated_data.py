import pandas as pd
import os
import numpy as np
from datetime import datetime, timedelta
import random

def repeat_to_length(lst, n):
    """Repeat list elements to match length n."""
    return (lst * (n // len(lst) + 1))[:n]

def generate_more_data(formatted_file, output_file, target_rows=10000):
    """
    Reads an already formatted dataset and generates exactly target_rows
    synthetic data, ignoring the original dataset size.
    """
    if not os.path.isfile(formatted_file):
        print("Formatted file not found.")
        return

    df = pd.read_csv(formatted_file, low_memory=False)
    n_current = len(df)

    if n_current == 0:
        print("Formatted file is empty. Using dummy values only.")

    print(f"Generating {target_rows} rows of synthetic data...")

    new_rows = []
    for _ in range(target_rows):
        row = {
            'user_id': random.choice(df.get('user_id', repeat_to_length(['U1023','U1044','U1089','U1090','U1101'], target_rows))),
            'session_id': random.choice(df.get('session_id', repeat_to_length(['S5502','S5503','S5504','S5505','S5506'], target_rows))),
            'event_time': (datetime.now() - timedelta(minutes=random.randint(0, 10000))).strftime('%Y-%m-%d %H:%M:%S'),
            'page_name': random.choice(df.get('page_name', repeat_to_length(['Home_Page','Loan_Offers_Page','Loan_Apply_Page','Payment_Page','Success_Page'], target_rows))),
            'event_type': random.choice(df.get('event_type', repeat_to_length(['view','click','submit'], target_rows))),
            'event_value': random.choice(df.get('event_value', repeat_to_length(['View Loan Details','Apply Now','Submit Application','Payment','Confirmation'], target_rows))),
            'device_type': random.choice(df.get('device_type', repeat_to_length(['mobile','desktop','tablet'], target_rows))),
            'location': random.choice(df.get('location', repeat_to_length(['Mumbai, IN','Delhi, IN','Chennai, IN','Pune, IN','Bangalore, IN'], target_rows))),
            'duration_on_page': random.choice(df.get('duration_on_page', repeat_to_length([24.5,12.0,35.2,15.8,28.9], target_rows))),
            'referrer_page': random.choice(df.get('referrer_page', repeat_to_length(['Home_Page','Loan_Offers_Page','Loan_Apply_Page'], target_rows))),
            'next_page': random.choice(df.get('next_page', repeat_to_length(['Loan_Apply_Page','Payment_Page','Success_Page','Logout_Page'], target_rows))),
            'conversion_flag': random.choice(df.get('conversion_flag', repeat_to_length([0,1], target_rows))),
            'funnel_stage': random.choice(df.get('funnel_stage', repeat_to_length(['Offer_View','Apply_Loan','Payment','Success'], target_rows))),
            'intent_label': random.choice(df.get('intent_label', repeat_to_length(['Apply_Loan','Purchase','Query_Info','Upgrade','Renewal'], target_rows))),
            'recommendation_shown': random.choice(df.get('recommendation_shown', repeat_to_length(['Personal Loan Banner','Credit Card Offer','Insurance Plan'], target_rows))),
            'recommendation_clicked': random.choice(df.get('recommendation_clicked', repeat_to_length([0,1], target_rows))),
            'cluster_id': random.choice(df.get('cluster_id', repeat_to_length(['C1','C2','C3','C4','C5'], target_rows))),
            'score_intent_probability': random.choice(df.get('score_intent_probability', repeat_to_length([0.87,0.75,0.65,0.92,0.81], target_rows)))
        }
        new_rows.append(row)

    synthetic_df = pd.DataFrame(new_rows)

    # Save output (only synthetic rows, exactly target_rows)
    synthetic_df.to_csv(output_file, index=False)
    print(f"Synthetic dataset saved at:\n{output_file}")
    print(f"Total rows: {len(synthetic_df)}")

if __name__ == "__main__":
    formatted_file = "/home/ampara/Downloads/kaggle_dataset_formatter/formatted_user_journey_data.csv"
    output_file = "/home/ampara/Downloads/kaggle_dataset_formatter/formattedSynthetic_data3k.csv"

    # Generate exactly 300 synthetic rows
    generate_more_data(formatted_file, output_file, target_rows=500)

