import pandas as pd

def main():
    df = pd.read_csv('~/src/covidence/tmp/Result_20.csv')
    print(df.head())
    print(df.info())
    creation_weeks = df.pop('creation_week')
    print(creation_weeks)
    print(df.info())
    df.to_csv('~/src/covidence/tmp/Result_20_modified.csv', index=False)
    return 0

if __name__ == '__main__':
    main()