def prompt0(code):
    return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Please answer yes or no indicating whether the input contains any vulnerabilities.

### Input:
{code}

### Response (Yes | No):
"""


def prompt1(code):
    return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Please answer yes or no whether one of Critical CWEs is in the following input.

### Critical CWEs:
CWE-125, CWE-119, CWE-787, CWE-20, CWE-476, CWE-416, CWE-190

### Input:
{code}

### Response (Yes | No):
"""


def prompt2(cwe_id, cwe_name, cwe_desc, code):
    return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
CWE-{cwe_id} {cwe_name}: {cwe_desc}

Please answer yes or no whether CWE-{cwe_id} is in the following input.

### Input:
{code}

### Response (Yes | No):
"""


def prompt21(cwe_id, code):
    return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Please answer yes or no whether CWE-{cwe_id} is in the following input.

### Input:
{code}

### Response (Yes | No):
"""


def prompt3(cwe_id, code):
    return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Vulnerability type: CWE-{cwe_id}

### Input:
{code}

### Instruction:
#### Define the vulnerability:

#### Provide examples:

#### Examine the code:

#### Confirm if the input has vulnerability (Yes | No):

"""
