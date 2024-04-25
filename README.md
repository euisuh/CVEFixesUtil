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
| CWE-918| Server-Side Request Forgery (SSRF) | 148       | 19            |
| CWE-352|  Cross-Site Request Forgery (CSRF) | 121       | 9             |
| CWE-79 | Cross-Site Scripting         | 73              | 2             |
| CWE-20 | Improper Input Validation    | 66              | 6             |
| CWE-22 | Path Traversal               | 61              | 8             |

### C
| CWE ID | Name                         | Number of Pairs | Rank in MITRE |
|--------|------------------------------|-----------------|---------------|

### C++
| CWE ID | Name                         | Number of Pairs | Rank in MITRE |
|--------|------------------------------|-----------------|---------------|

### Java
| CWE ID | Name                         | Number of Pairs | Rank in MITRE |
|--------|------------------------------|-----------------|---------------|

### Ruby
| CWE ID | Name                         | Number of Pairs | Rank in MITRE |
|--------|------------------------------|-----------------|---------------|

### Go
| CWE ID | Name                         | Number of Pairs | Rank in MITRE |
|--------|------------------------------|-----------------|---------------|

