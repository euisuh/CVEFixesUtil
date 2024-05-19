############################
# Standard Prompts
############################

# Standard Prompt 1 (ZS) (TO)
def promptS1(code, cwe_name):
    return f'''
Code:
{code}

Question:
Does this code contain instances of the security vulnerability known as {cwe_name}?

Answer:
'''
# Standard Prompt 2 (ZS) (RO)
# sys = "You are a helpful assistant."
def promptS2(code, cwe_name):
    return f'''
Code:
{code}

Question:
Does this code contain instances of the security vulnerability known as {cwe_name}?

Answer:
'''

# Standard Prompt 3 (ZS) (RO)
# sys = "You are a code security expert."
def promptS3(code, cwe_name):
    return f'''
Code:
{code}

Question:
Does this code contain instances of the security vulnerability known as {cwe_name}?

Answer:
'''

# Standard Prompt 4 (ZS) (RO)
# sys = "You are a code security expert who analyzes the given code for the security vulnerability known as {}.".format(cwe_name)
# no question here, but cwe_name is being passed into the sys prompt
def promptS4(code):
    return f'''
Code:
{code}

Analysis:
'''
# Standard Prompt 5 (FS) (TO)

# They provide "vuln_reason" and "patch_reason" as examples in addition to "vuln_code"
# code_before_reason - reason for the code_before being vulnerable
# code_after_reason - reason for the code_after being benign
#the vuln and patched code reasoning they provide here are taken from the CWE website.
def promptS5(code, cwe_name, code_before, code_after, code_before_reason, code_after_reason):
    return f'''
Examples:
Example 1:
Code:
{code_before}

Question:
Does this code contain instances of the security vulnerability known as {cwe_name}

Answer:
{code_before_reason}

Example2:
Code:
{code_after}

Question:
Does this code contain instances of the security vulnerability known as {cwe_name}

Answer:
{code_after_reason}

Code:
{code}

Question:
Does this code contain instances of the security vulnerability known as {cwe_name}

Answer:
'''


# Standard Prompt 6 (FS) (RO)
#sys = "You are a code security expert who analyzes the given code for the security vulnerability known as {}.".format(cwe_name)
def promptS6(code, cwe_name, code_before, code_after, code_before_reason, code_after_reason):
    return f'''
Examples:
Example 1:
Code:
{code_before}

Analysis:
{code_before_reason}

Example2:
Code:
{code_after}

Analysis:
{code_after_reason}

Code:
{code}

Analysis:
'''


############################
# Step-by-Step Prompts
############################

# Step-by-Step (R1) Prompt 1 (ZS) (TO)
def promptR1(code, cwe_name):
    return f'''

Code:
{code}

Question:
Does this code contain instances of the security vulnerability known as {cwe_name}?

Answer: 
Let's think step by step.
'''

# Step-by-Step (R2) Prompt 2 (ZS) (RO)
#sys = "You are a code security expert who analyzes the given code for the security vulnerability known as {} following these four steps:\n1. First you describe the overview of the code\n2. Then based on the overview you identify the sub-components in code that could lead to {}\n3. After that you do a detailed analysis of the identified sub-components for the existence of the {}\n4. Based on the detailed analysis you decide and answer whether the {} is present in the given code or not".format(cwe_name, cwe_name, cwe_name + " vulnerability", cwe_name + " vulnerability")
def promptR2(code, cwe_name):
    return f'''
Code:
{code}

Analysis:
'''

###################################################################3
#not done yet (unsure how to do)
# Step-by-Step (R3) Prompt 3 (ZS) (TO)
def promptR3(code, cwe_name):
    return f'''

Code:
{code}

Analysis:
'''
#####################################################################
# Step-by-Step (R4) Prompt 4 (FS) (RO)
#sys = "You are a code security expert who analyzes the given code for the security vulnerability known as {}.".format(cwe_name)
#here the reasoning they provide for the vuln and patched codes are the ones written by experts, not CWE like the previous example in the standard prompt S6.
# code_before_reasonExp, code_after_reasonExp are the expert reasoning
def promptR4(code, cwe_name, code_before, code_after, code_before_reasonExp, code_after_reasonExp):
    return f'''
Examples:
Example 1:
Code:
{code_before}

Analysis:
{code_before_reasonExp}

Example2:
Code:
{code_after}

Analysis:
{code_after_reasonExp}

Code:
{code}

Analysis:
'''

# Step-by-Step (R5) Prompt 5 (FS) (RO)
# sys = "You are a code security expert who analyzes the given code for the security vulnerability known as {} following these four steps:\n1. First you describe the overview of the code\n2. Then based on the overview you identify the sub-components in code that could lead to {}\n3. After that you do a detailed analysis of the identified sub-components for the existence of the {}\n4. Based on the detailed analysis you decide and answer whether the {} is present in the given code or not".format(cwe_name, cwe_name, cwe_name + " vulnerability", cwe_name + " vulnerability")
# code_before_reasonExp, code_after_reasonExp are the expert reasoning
def promptR5(code, cwe_name, code_before, code_after, code_before_reasonExp, code_after_reasonExp):
    return f'''
Examples:
Example 1:
Code:
{code_before}

Analysis:
{code_before_reasonExp}

Example2:
Code:
{code_after}

Analysis:
{code_after_reasonExp}

Code:
{code}

Analysis:
'''

# Step-by-Step Prompt 6 (FS) (TO)
# sys = "Guidelines to analyze the given code for the security vulnerability known as {}:\n1. First describe the overview of the code\n2. Then based on the overview identify the sub-components in code that could lead to {}\n3. After that do a detailed analysis of the identified sub-components for the existence of the {}\n4. Based on the detailed analysis decide and answer whether the {} is present in the given code or not".format(cwe_name, cwe_name, cwe_name + " vulnerability", cwe_name + " vulnerability")
# code_before_reasonExp, code_after_reasonExp are the expert reasoning
def promptR6(code, cwe_name, code_before, code_after, code_before_reasonExp, code_after_reasonExp):
    return f'''
Code:
{code_before}

Analysis:
{code_before_reasonExp}

Example2:
Code:
{code_after}

Analysis:
{code_after_reasonExp}

Code:
{code}

Analysis:
'''



############################
# Definition Prompts
############################

# Definition Prompt 1 (ZS) (TO)
# Here they provide a definition of the CWE 
# cwe_defin is the definition of the CWE
def promptD1(code, cwe_name, cwe_defin):
    return f'''
{cwe_defin}

Code:
{code}

Question:
Does this code contain instances of the security vulnerability known as {cwe_name}?

Answer:
'''

# Definition Prompt 2 (ZS) (RO)
#  sys = "You are a code security expert who analyzes the given code for the security vulnerability known as {}.\n\n{}".format(cwe_name, self.defs[cwe])
# The definition of the CWE goes in the system prompt
def promptD2(code, cwe_name, cwe_defin):
    return f'''
Code:
{code}

Analysis:
'''

# Definition Prompt 3 (FS) (RO)
# sys = "You are a code security expert who analyzes the given code for the security vulnerability known as {}.\n\n{}".format(cwe_name, self.defs[cwe])
# The definition of the CWE goes in the system prompt
def promptD3(code, cwe_name, cwe_defin, code_before, code_after, code_before_reason, code_after_reason):
    return f'''
Code:
{code_before}

Analysis:
{code_before_reason}

Example2:
Code:
{code_after}

Analysis:
{code_after_reason}

Code:
{code}

Analysis:
'''

# Definition Prompt 4 (FS) (RO)
# sys = "You are a code security expert who analyzes the given code for the security vulnerability known as {}.\n\n{}".format(cwe_name, self.defs[cwe])
# The definition of the CWE goes in the system prompt
# Here the reasoning
def promptD4(code, cwe_name, cwe_defin, code_before, code_after, code_before_reasonExp, code_after_reasonExp):
    return f'''
Code:
{code_before}

Analysis:
{code_before_reasonExp}

Example2:
Code:
{code_after}

Analysis:
{code_after_reasonExp}

Code:
{code}

Analysis:
'''

# Definition Prompt 5 (FS) (TO)
# sys = "Analyze the given code for the security vulnerability known as {}.\n\n{}".format(cwe_name, self.defs[cwe])
# Definition of the CWE passed in the system prompt
def promptD5(code, cwe_name, cwe_defin, code_before, code_after, code_before_reasonExp, code_after_reasonExp):
    return f'''
Code:
{code_before}

Analysis:
{code_before_reasonExp}

Example2:
Code:
{code_after}

Analysis:
{code_after_reasonExp}

Code:
{code}

Analysis:
'''
