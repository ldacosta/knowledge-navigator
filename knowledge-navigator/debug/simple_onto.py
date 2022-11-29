# import
import pandas as pd
from jaal import Jaal
from jaal.datasets import load_got
# load the data
edge_df, node_df = load_got()

data = {
    # Bob knows Alice
    'row_1': ['Bob', 'knows'],
    'row_2': ['knows', 'Alice'],
    # Bob has green car
    'row_3': ['Bob', 'has'],
    'row_4': ['has', 'green'],
    'row_5': ['green', 'car'],
    # Luis has blue car
    'row_6': ['Luis', 'has'],
    'row_7': ['has', 'blue'],
    'row_8': ['blue', 'car'],
}
df = pd.DataFrame.from_dict(data, orient='index', columns=['from', 'to'])

# init Jaal and run server
Jaal(df).plot(directed=True)
