
import pandas as pd

def extract_features(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    features = df.groupby('user').apply(lambda x: pd.Series({
        'n_deposits': (x['type'] == 'deposit').sum(),
        'n_borrows': (x['type'] == 'borrow').sum(),
        'n_repays': (x['type'] == 'repay').sum(),
        'n_liquidations': (x['type'] == 'liquidationcall').sum(),
        'total_deposit': x[x['type'] == 'deposit']['amount'].sum(),
        'total_borrow': x[x['type'] == 'borrow']['amount'].sum(),
        'total_repay': x[x['type'] == 'repay']['amount'].sum(),
        'activity_days': (x['timestamp'].max() - x['timestamp'].min()).days + 1,
        'unique_assets': x['reserve'].nunique(),
        'total_transactions': len(x)
    })).fillna(0)

    features['deposit_borrow_ratio'] = features['total_deposit'] / (features['total_borrow'] + 1e-5)
    features['repay_borrow_ratio'] = features['total_repay'] / (features['total_borrow'] + 1e-5)
    features['liquidation_rate'] = features['n_liquidations'] / (features['n_borrows'] + 1e-5)
    features['tx_per_day'] = features['total_transactions'] / (features['activity_days'] + 1e-5)

    return features.reset_index()
