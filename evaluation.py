import pandas as pd
from utils import *
import os
from tqdm import tqdm
import re

os.environ["CUDA_VISIBLE_DEVICES"] = "5"

def classify_report(text):
    prompt = f'''
### System:
You are an AI assistant specialized in code security analysis. Your task is to evaluate security reports for potential code vulnerabilities. Given a security report detailing a specific vulnerability, you need to determine if the vulnerability exists in the provided code.

### Security Report:
{text}

### Response (Yes | No):
'''
    
    res = inferModel(prompt)

    res = res[0].lower().split()
    res = [re.sub(r'\W+', '', word) for word in res]
    if 'yes' in res and 'no' in res:
        return -1
    elif 'yes' in res:
        return 1
    elif 'no' in res:
        return 0
    else:
        return -1

def get_prediction(text):
    text = text.lower().split()
    text = [re.sub(r'\W+', '', word) for word in text]

    if 'yes' in text and 'no' in text:
        return classify_report(" ".join(text))
    elif 'yes' in text:
        return 1
    elif 'no' in text:
        return 0
    else:
        return classify_report(" ".join(text))

csv_files = [f for f in os.listdir('kat_res/') if f.endswith('.csv')]
csv_files = sorted(csv_files)

for f in csv_files:
    df = pd.read_csv(f'kat_res/{f}')

    pred_before = []
    pred_after = []
    
    for i in tqdm(range(df.shape[0])):
        res_before = df.res_before.iloc[i]
        res_after = df.res_after.iloc[i]

        pred_before.append(get_prediction(res_before))
        pred_after.append(get_prediction(res_after))

    df['pred_before'] = pred_before
    df['pred_after'] = pred_after 

    df.to_csv(f'kat_res/new_{f}', index=False)
    print(f'Successfully completed {f}')