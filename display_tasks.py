import pandas as pd


def print_TDL(tdl):
    priority_order = ['high', 'medium', 'low']
    tdl['Priority'] = pd.Categorical(tdl['Priority'], categories=priority_order, ordered=True)
    tdl['Deadline'] = pd.to_datetime(tdl['Deadline'])
    df_sorted = tdl.sort_values(by=['Priority', 'Deadline'])

    print(df_sorted)
    # print(df)
