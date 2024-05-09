def prompt1(code):
    return f'''Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Please answer yes or no whether one of Critical CWEs is in the following input.

### Critical CWEs:
CWE-125, CWE-119, CWE-787, CWE-20, CWE-476, CWE-416, CWE-190

### Input:
{code}

### Response:
'''


def prompt2(cwe_id, cwe_name, cwe_desc, poison_code1, code):
    return f'''Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### {cwe_id} {cwe_name}:
{cwe_desc}

### Code with {cwe_id}:
{poison_code1}

### Instruction:
Please answer yes or no whether {cwe_id} is in the following input.

### Input:
{code}

### Response:
'''


def prompt3(cwe_id, cwe_name, cwe_desc, poison_code1, clean_code1, code):
    return f'''Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### {cwe_id} {cwe_name}:
{cwe_desc}

### Code with {cwe_id}:
{poison_code1}

### Code without {cwe_id}:
{clean_code1}

### Instruction:
Please answer yes or no whether {cwe_id} is in the following input.

### Input:
{code}

### Response:
'''