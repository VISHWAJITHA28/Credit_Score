
import json
import pandas as pd
from src.preprocessing import extract_features
from src.scoring_model import score_wallets
import argparse

def load_data(json_path):
    with open(json_path) as f:
        data = json.load(f)
    return pd.DataFrame(data)

def main(input_path, output_path):
    df = load_data(input_path)
    features = extract_features(df)
    scored_df = score_wallets(features)
    scored_df.to_csv(output_path, index=False)
    print(f"✅ Saved wallet scores to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Path to user_transactions.json')
    parser.add_argument('--output', required=True, help='Output path for wallet_scores.csv')
    args = parser.parse_args()
    main(args.input, args.output)
