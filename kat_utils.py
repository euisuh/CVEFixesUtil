import requests
import pandas as pd
import os
import re

def classify_report(text):
    prompt = f'{text}: As a final decision, does the text state that the code contains a security vulnerability? (Answer DIRECTLY "yes" or "no" or "n/a" ONLY in case the text does not provide a definite answer)'
    resp = inferModel(prompt)

    # Handle both possible output types
    if isinstance(resp, list):
        response_text = resp[0] if resp else ""
    else:
        response_text = resp.strip() if resp else ""
        
    if not response_text:
        return -1
    
    # Process the response
    response_words = response_text.lower().split()
    cleaned_response = [re.sub(r'\W+', '', word) for word in response_words]
  

    if 'yes' in cleaned_response and 'no' in cleaned_response:
        return -1
    elif 'yes' in cleaned_response:
        return 1
    elif 'no' in cleaned_response:
        return 0
    else:
        return -1


def get_prediction(text):
    original_text = text  # Save the original text
    text = text.lower().split()
    text = [re.sub(r'\W+', '', word) for word in text]
    
    if text[0] == "yes":
        return 1
    elif text[0] == "no":
        return 0
    elif 'yes' in text and 'no' in text:
        return classify_report(original_text)
    elif 'yes' in text:
        return 1
    elif 'no' in text:
        return 0
    else:
        return classify_report(original_text)
    
def extractPred(df):
    pred_before = []
    pred_after = []
    
    for i in range(df.shape[0]):
        pred_before.append(get_prediction(str(df['res_before'].iloc[i])))
        pred_after.append(get_prediction(str(df['res_after'].iloc[i])))
    
    df['pred_before'] = pred_before
    df['pred_after'] = pred_after



#Same exact inferModel, but temperature default set to 0.0
def inferModel(prompt='This is a cake recipe:\n\n', port=5000, temperature=0.0, max_tokens=200):
    url = f'http://10.4.64.43:{port}/v1/completions'
    headers = {'Content-Type': 'application/json'}
    
    data = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": 0.9,
        "seed": 10
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        try:
            return response.json()['choices'][0]['text']
        except:
            return 'FAILED TO PARSE RESPONSE'
    else:
        return response.text
    


def main():
    directory_path = 'C:/Users/user/Downloads/output28/'
    all_files = os.listdir(directory_path)
    csv_files = [f for f in all_files if f.endswith('.csv')]

    for csv_file in csv_files:
        file_path = os.path.join(directory_path, csv_file)
        print(f"Processing file: {file_path}")  
        
        df = pd.read_csv(file_path)
        
        #data processing function
        extractPred(df)
        
        output_file_path = os.path.join(directory_path, f"p_{csv_file}")
        df.to_csv(output_file_path, index=False)
        print(f"Processed and saved: {output_file_path}")
    
if __name__ == "__main__":
    main()
    