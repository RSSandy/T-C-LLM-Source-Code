# Terms of Service (ToS) Clause Risk Scanner 
## Project Overview
This project develops an automated data pipeline that processes Terms of Service (ToS) documents to identify potentially problematic or "shady" clauses and generate user-friendly explanations in simpler language. Legal documents, such as ToS, are often difficult for most users to understand due to their complex, legal language. This tool aims to make these documents more accessible by flagging harmful clauses and clarifying their risks.

The pipeline works as follows:

1. **Document Processing:**  The ToS document is read and tokenized.
2. **Classification:** A fine-tuned LegalBERT model classifies each clause as either "shady" or "not shady."
3. **Key Term Extraction:** The attention weights from LegalBERT are extracted to identify key terms that influence the classification decision.
4. **Explanation Generation:** If a clause is flagged as shady, the clause, its classification, and key terms are passed to a LLaMA model, which generates a concise, user-friendly explanation.

This tool automates the process of reviewing legal documents, making it easier for consumers, legal professionals, and companies to interpret contract terms.

## Contents of the Repository
The repository contains the following components:

*TOS_LLM.ipynb* - Source Code: The source code for the notebook that implements the pipeline described above.

*/Example TOS* - Example ToS Files: A folder containing a set of example ToS documents for testing and demonstration purposes.

*app.py*  - Streamlit App (unfinished): An unfinished app.py file for a Streamlit app that allows users to upload ToS documents and view flagged clauses with their explanations.

*TOS_Backend.ipynb* - API Backend (unfinished): An unfinished backend to streamline the source code into a working API for integration with the Streamlit app.

## Future Goals
The following goals are planned for future development:

- Finish the Streamlit App: Completing the user interface for uploading ToS documents, viewing flagged clauses, and reading explanations.
- Fine-tune LegalBERT: Create a pipeline to process annotated texts and use them to fine-tune the LegalBERT model.
- Implement RAG Mechanism: Develop a Retrieval-Augmented Generation (RAG) mechanism that feeds LegalBERT or the LLaMA model the legal context surrounding specific clauses/terms to improve classification and explanation quality.

## Citation
LegalBERT: [Link Text](https://huggingface.co/nlpaueb/legal-bert-base-uncased) 

LLaMA Model: [Link Text](https://huggingface.co/huihui-ai/Llama-3.2-1B-Instruct-abliterated)

ToS Example Dataset: [Link Text](https://www.sciencedirect.com/science/article/pii/S2352340924001082?ssrnid=4596818&dgcid=SSRN_redirect_SD)
