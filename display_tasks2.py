import pandas as pd


def print_TDL(tdl, sort_by=None):
    # dataframe for sorting
    df = pd.DataFrame(tdl)

    if sort_by == 'priority':
        df = df.sort_values(by='priority')
    elif sort_by == 'date':
        df = df.sort_values(by='date')
    print(df)
