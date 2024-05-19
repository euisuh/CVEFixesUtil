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

#S3
for i in tqdm(range(df.shape[0])):
    res_before = inferSystemModel(promptS3(df.code_before.iloc[i], cwe_map.get(df['exp_cwe_id'].iloc[i][4:])['name']), "You are a code security expert.")
    res_after = inferSystemModel(promptS3(df.code_after.iloc[i], cwe_map.get(df['exp_cwe_id'].iloc[i][4:])['name']), "You are a code security expert.")
    
    df.at[i, 'res_before'] = res_before
    df.at[i, 'res_after'] = res_after
    
df.to_csv('kat_res/res_S3_llama3.csv', index=False)   