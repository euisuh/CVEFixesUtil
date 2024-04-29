# CVEFixesUtil

The CVEFixes Dataset Processor is a Python-based tool designed to analyze and process datasets related to Common Vulnerabilities and Exposures (CVE) fixes. The tool provides functionality to parse, filter, and extract relevant information from CVE fixes datasets, empowering researchers, security analysts, and developers to gain insights into vulnerabilities and their fixes.

## Key Features
1. Dataset Parsing: Effortlessly parse and load CVE fixes datasets into a structured format for further analysis.
2. Data Filtering: Filter and extract specific CVE entries or attributes based on various criteria such as CVE ID, severity, affected software, and more.
3. CVE Analysis: Conduct in-depth analysis on CVE entries, including identifying common patterns, trends, and correlations among vulnerabilities and their fixes.
4. Integration Support: Seamlessly integrate the processed CVE data with existing security tools, vulnerability scanners, and databases for enhanced vulnerability management and mitigation strategies.

## Getting Started

To get started with the CVEFixesUtil, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using the provided requirements.txt file.
3. Download the CVEFixes database file from [Zenodo](https://zenodo.org/records/7029359).
4. Place the downloaded database file in the same directory as the repository.
5. Explore the sample datasets and documentation provided to understand the tool's functionalities and usage.
6. Begin analyzing and processing CVE fixes datasets to gain valuable insights into vulnerabilities and their fixes.

For more information, visit the [CVEfixes GitHub repository](https://github.com/secureIT-project/CVEfixes).

## CWE ID Tables
Below are tables containing CWE ID, name, number of pairs, and rank in the MITRE for each language:

### Python
| CWE ID | Name                         | Number of Pairs | Rank in MITRE |
|--------|------------------------------|-----------------|---------------|
| CWE-918| Server-Side Request Forgery (SSRF) | 146       | 19            |
| CWE-352| Cross-Site Request Forgery (CSRF)  | 121       | 9             |
| CWE-79 | Cross-Site Scripting         | 63              | 2             |
| CWE-20 | Improper Input Validation    | 61              | 6             |
| CWE-22 | Path Traversal               | 51              | 8             |

### C
| CWE ID | Name                         | Number of Pairs | Rank in MITRE |
|--------|------------------------------|-----------------|---------------|
| CWE-125| Out-of-bounds Read           | 583             | 7             |
| CWE-119| Buffer Overflow              | 493             | 17            |
| CWE-787| Out-of-bounds Write          | 303             | 1             |
| CWE-20 | Improper Input Validation    | 288             | 6             |
| CWE-476| NULL Pointer Dereference     | 269             | 12            |
| CWE-416| Use After Free               | 243             | 4             |
| CWE-190|Integer Overflow or Wraparound| 211             | 14            |
| CWE-362| Race Condition               | 177             | 21            |

### C++
| CWE ID | Name                         | Number of Pairs | Rank in MITRE |
|--------|------------------------------|-----------------|---------------|

### Java
| CWE ID | Name                         | Number of Pairs | Rank in MITRE |
|--------|------------------------------|-----------------|---------------|
| CWE-287| Improper Authentication      | 126             | 13            |
| CWE-22 | Path Traversal               | 101             | 8             |
| CWE-862| Missing Authorization        | 62              | 11            |
| CWE-918| Server-Side Request Forgery (SSRF)| 48         | 19            |
| CWE-79 | Cross-site Scripting         | 40              | 2             |

### Ruby
| CWE ID | Name                         | Number of Pairs | Rank in MITRE |
|--------|------------------------------|-----------------|---------------|
| CWE-89 | SQL Injection                | 203             | 3             |
| CWE-79 | Cross-site Scripting         | 65              | 2             |
| CWE-20 | Improper Input Validation    | 54              | 6             |
| CWE-863| Incorrect Authorization      | 30              | 24            |

### Go
| CWE ID | Name                         | Number of Pairs | Rank in MITRE |
|--------|------------------------------|-----------------|---------------|
| CWE-863| Incorrect Authorization      | 36              | 24            |
| CWE-190| Integer Overflow or Wraparound| 19             | 14            |
| CWE-78 | OS Command Injection         | 13              | 5             |
| CWE-918| Server-Side Request Forgery (SSRF)| 12         | 19            |
| CWE-22 | Path Traversal               | 11              | 8             |
| CWE-20 | Improper Input Validation    | 10              | 6             |

## Dataset

The dataset is published and available for download [here](https://huggingface.co/datasets/euisuh15/cveFixes1).