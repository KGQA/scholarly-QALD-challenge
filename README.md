# Scholarly QALD Challenge
Website for the scholarly QALD Challenge @ ISWC 2023

## Tasks

### Task 1: SciQA --- Question Answering of Scholarly Knowledge

This new task introduced this year will use a scholarly data source ORKG (https://orkg.org) as a target repository for answering comparative questions. KGQA benchmarks and systems were so far mainly geared towards encyclopedic knowledge graphs such as DBpedia and Wikidata.
In this task, we will leverage a novel QA benchmark for scholarly knowledge -- *SciQA* (https://zenodo.org/record/7727922). 
The benchmark leverages the Open Research Knowledge Graph (ORKG) which includes over 100,000 resources describing complex research contributions.
Following a bottom-up methodology, we manually developed a set of 100 questions that can be answered using this knowledge graph. 
The questions cover a wide range of research fields and question types and are translated into SPARQL queries over the knowledge graph. 
The SciQA benchmark represents an extremely challenging task for next-generation QA systems.
The 100 hand-crafted questions are significantly more complex to answer than typical common-sense questions. An example question is:

*What is the average energy generation for each energy source considered in 5-year intervals in Greenhouse Gas Reduction Scenarios for Germany?*

The corresponding SPARQL query includes seven triple patterns, uses eight query components, and is shaped as a tree

In addition to the 100 hand-crafted questions, we will provide a set of more than 2,000 questions generated from 10 question/query templates to ensure a good balance between question complexity and wider coverage.


### Task 2: DBLP-QUAD --- Knowledge Graph Question Answering over DBLP

For this task, participants will use the DBLP-QUAD dataset (https://doi.org/10.5281/zenodo.7554379), see also https://huggingface.co/datasets/awalesushil/DBLP-QuAD, which consists of 10,000 question-SPARQL pairs, and is answerable over the DBLP Knowledge Graph (https://blog.dblp.org/2022/03/02/dblp-in-rdf/) and (https://zenodo.org/record/7638511). DBLP is a well-known repository for computer science bibliography and has recently released an RDF dump. This allows users to query it as a knowledge graph.
The first subtask is to fetch the right answer from the DBLP KG given the question. The second subtask is entity linking (EL) on the same dataset. Participants are free to decide if they want to take part in either one, or both of the subtasks.
The DBLP-QuAD dataset was created using the OVERNIGHT approach, where logical forms are first generated from a KG. Then canonical questions are generated from these logical forms. 


For both tasks, we aim to evaluate the participants' approaches using the Hugging Face Evaluate library (https://huggingface.co/docs/evaluate/index). That is, participants can either upload their models to Hugging Face or send us their models so we can compare them neutrally using the Python-based Evaluate library. The participating systems will be evaluated based on the standard metrics precision, recall, and f-measure.



