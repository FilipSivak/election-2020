import urllib.request
import json
import pandas as pd
from pathlib import Path
import datetime
from graph import make_graph

target_filename = Path("election_data_SG_GA.csv")

# Fetch data
cnn_url = "https://politics-elex-results.data.api.cnn.io/results/view/2020-SG-GA.json"
contents = urllib.request.urlopen(cnn_url).read()
record = json.loads(contents.decode("utf8"))

# Assemble dataframe
row = {"time": datetime.datetime.now()}

for candidate in record["candidates"]:
    row[candidate["lastName"]] = candidate["voteNum"]


# Append dataframe
if target_filename.exists():
    df = pd.read_csv(target_filename).append(pd.DataFrame([row]))
else:
    df = pd.DataFrame([row])

# Save dataframe
df.to_csv(target_filename, index = False)

# Save graph
make_graph()
