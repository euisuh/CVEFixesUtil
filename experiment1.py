from tqdm import tqdm
from vllm import LLM, SamplingParams
from prompt import *
import os
import pandas as pd

os.environ["CUDA_VISIBLE_DEVICES"]="5"
df = pd.read_csv('vulC7.csv')

model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
llm = LLM(model=model_name)
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

before_acc = []
after_acc = []

for i in tqdm(range(df.shape[0])):
    prompts = [
        prompt1(df.func_before.iloc[i]),
        prompt1(df.func_after.iloc[i]),
    ]
    
    outputs = llm.generate(prompts, sampling_params)

    before_acc.append(outputs[0].outputs[0].text)
    after_acc.append(outputs[1].outputs[0].text)

    if (i + 1) % 100 == 0 or i == df.shape[0] - 1:
        output_df = pd.DataFrame({'before': before_acc, 'after': after_acc})
        output_df.to_csv(f'{model_name}_output_{i + 1}.csv', index=False)
        before_acc = []
        after_acc = []

