
# Aave V2 Credit Scoring Engine

## Objective

Build a machine learning-based scoring engine that assigns a credit score (0–1000) to DeFi wallets based on historical transactions with the Aave V2 protocol.

## How It Works

We:
- Parse raw transaction data (deposit, borrow, repay, etc.)
- Engineer features per wallet
- Apply a normalized, weighted scoring formula
- Output credit scores for each wallet

## Run the Script

```bash
python src/main.py --input data/user_transactions.json --output output/wallet_scores.csv
```

## Features Used

- Deposit-to-Borrow Ratio
- Repay-to-Borrow Ratio
- Liquidation Rate
- Number of Deposits / Borrows / Repays
- Asset Diversity
- Transaction Frequency

## Dependencies

- Python ≥ 3.8
- pandas
- numpy
- scikit-learn
- seaborn
