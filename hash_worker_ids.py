
import pandas as pd
from hashlib import md5

if __name__ == '__main__':
    filename = 'Experiment 2/run3_accepted_votes_long.csv'
    df = pd.read_csv(filename)
    df['id2'] = 'run3' + df['workerid'].astype(str)
    df['hash'] = df['id2'].apply(hash)
    df['workerid_hash'] = 'w_' + df['hash'].astype(str)
    df.to_csv(f'{filename}_hash.csv', index=False)
