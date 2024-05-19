from tqdm import tqdm
from utils import *
from prompts_kat import *
import pandas as pd

import json

json_file_path = 'C:/Users/user/Documents/GitHub/original/CVEFixesUtil/cwe25.json'

with open(json_file_path, 'r') as file:
    cwe25 = json.load(file)
    cwe_map = {item['id']: {'name': item['name'], 'description': item['description']} for item in cwe25}

df = pd.read_csv('vulC7_test.csv')


#S4
for i in tqdm(range(df.shape[0])):
    res_before = inferSystemModel(promptS4(df.code_before.iloc[i], cwe_map.get(df['exp_cwe_id'].iloc[i][4:])['name']), f"You are a code security expert who analyzes the given code for the security vulnerability known as {cwe_map.get(df['exp_cwe_id'].iloc[i][4:])['name']}.")
    res_after = inferSystemModel(promptS4(df.code_after.iloc[i], cwe_map.get(df['exp_cwe_id'].iloc[i][4:])['name']), f"You are a code security expert who analyzes the given code for the security vulnerability known as {cwe_map.get(df['exp_cwe_id'].iloc[i][4:])['name']}.")
    
    df.at[i, 'res_before'] = res_before
    df.at[i, 'res_after'] = res_after
    
df.to_csv('res_kat/res_S4_llama3.csv', index=False)  