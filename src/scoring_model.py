
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def score_wallets(features_df):
    scoring_features = [
        'deposit_borrow_ratio', 'repay_borrow_ratio', 'liquidation_rate',
        'n_deposits', 'n_borrows', 'n_repays', 'tx_per_day', 'unique_assets'
    ]

    scaler = MinMaxScaler()
    normalized = scaler.fit_transform(features_df[scoring_features])

    weights = np.array([0.25, 0.25, -0.3, 0.1, -0.1, 0.1, 0.2, 0.2])
    scores = np.dot(normalized, weights)
    scores = (scores - scores.min()) / (scores.max() - scores.min()) * 1000

    features_df['credit_score'] = scores.astype(int)
    return features_df[['user', 'credit_score']]
