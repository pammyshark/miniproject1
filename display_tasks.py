import pandas as pd


def print_TDL(tdl):
    priority_order = ['high', 'medium', 'low']
    tdl['Priority'] = pd.Categorical(tdl['Priority'], categories=priority_order, ordered=True)
    tdl['Deadline'] = pd.to_datetime(tdl['Deadline'])
    df_sorted = tdl.sort_values(by=['Priority', 'Deadline'])

    print("To-Do List:")

    for index, row in df_sorted.iterrows():
        print(f"{index + 1}. {row['Task']} - {row['Priority']} - {row['Deadline'].strftime('%Y-%m-%d')}")

    return tdl
    # print(df)


def recommend(tdl):
    tdl = print_TDL(tdl)
    print("Good afternoon! Here are some tasks you might want to work on:")
    if len(tdl) == 0:
        print("No high-priority tasks available.")
    elif len(tdl) >= 1:
        print(f"{tdl.iloc[0]['Task']} - {tdl.iloc[0]['Priority']} - {tdl.iloc[0]['Deadline'].strftime('%Y-%m-%d')}")

    if len(tdl) >= 2:
        print(f"{tdl.iloc[1]['Task']} - {tdl.iloc[1]['Priority']} - {tdl.iloc[1]['Deadline'].strftime('%Y-%m-%d')}")
