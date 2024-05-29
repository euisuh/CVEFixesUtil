import pandas as pd
import argparse

from utils import *
import os
from tqdm import tqdm
import re


def extract_response_prompt(text):
    return f"""### Instruction:
As a final decision, does the text state that the code contains a security vulnerability?

### Text:
{text}

### Response (Yes | No | N/A):
"""


# os.environ["CUDA_VISIBLE_DEVICES"] = "3"

parser = argparse.ArgumentParser(description="Process command line arguments.")

parser.add_argument(
    "--cuda-visible-devices",
    dest="cuda_visible_devices",
    type=int,
    help="Index of the CUDA visible device",
)
parser.add_argument("--prompt", dest="prompt", type=str, help="prompt")

args = parser.parse_args()

os.environ["CUDA_VISIBLE_DEVICES"] = str(args.cuda_visible_devices)

csv_files = [
    file
    for file in os.listdir("kat_res/")
    if file.endswith(".csv") and "new" not in file
]
csv_files.sort()

invalid_res_before = []
invalid_res_after = []

for csv_file in csv_files:
    df = pd.read_csv(f"kat_res/{csv_file}")

    filtered_res_before = df.loc[df["pred_before"] == -1, "res_before"]
    invalid_res_before.extend(filtered_res_before.tolist())

    filtered_res_after = df.loc[df["pred_after"] == -1, "res_after"]
    invalid_res_after.extend(filtered_res_after.tolist())

div_idx = len(invalid_res_before)
prompts = invalid_res_before + invalid_res_after
prompts = [extract_response_prompt(i) for i in prompts]

responses = inferModelVllm("meta-llama_Meta-Llama-3-8B-Instruct/", prompts)
res_before = responses[:div_idx]
res_after = responses[div_idx:]

df = pd.DataFrame(
    {"res_before": pd.Series(res_before), "res_after": pd.Series(res_after)}
)
df.to_csv("responses.csv", index=False)

# df = pd.read_csv('responses.csv')
# res_before = df['res_before'].dropna().tolist()
# res_after = df['res_after'].dropna().tolist()

pos_bef = 0
pos_aft = 0

tqdm_pos_bef = tqdm(total=len(res_before), desc="Processing res_before")
tqdm_pos_aft = tqdm(total=len(res_after), desc="Processing res_after")

for csv_file in csv_files:
    df = pd.read_csv(f"kat_res/{csv_file}")
    df["res_before_1"] = ""
    df["res_after_1"] = ""

    for index, row in df.iterrows():
        if row["pred_before"] == -1:
            df.at[index, "res_before_1"] = res_before[pos_bef]
            pos_bef += 1
            tqdm_pos_bef.update(1)

        if row["pred_after"] == -1:
            df.at[index, "res_after_1"] = res_after[pos_aft]
            pos_aft += 1
            tqdm_pos_aft.update(1)

    df.to_csv(f"kat_res/{csv_file}", index=False)
