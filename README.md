Repository for Skin in the Game with TD Monitoring

Directories are named by the sequence mentioned in the paper: 

"1 - Data Mining": This directory is related to data mining and aggregation. Sanitised data mined from version 1.01 and version 2.00 of The Technical Debt Dataset (https://github.com/clowee/The-Technical-Debt-Dataset) can be found in a CSV file. The mining query can be found in an SQL file.

"2 - monitoringConditions": This directory represents example Behaviaural Cloning scripts utilised to capture users' feedback, train the model and test between users' feedback and the model. These scripts are derived from https://github.com/navuboy/gail_gym.

"3 - Replicator Dynamics": This directory stores replicator dynamics scripts of corresponding projects. These are utilised in example case studies. Three examples of strategies selected in the scripts are based on their optimal values in different weighting sets.

"4 - Jaccard Analysis": This directory is related to materials utilised for Jaccard Analysis of corresponding projects (i.e. Apache Accumulo and Apache Cocoon). The prefix "commit_analysis" represents Commit Analysis of corresponding projects. This is a pre-requisite for Jaccard Analysis, which utilised scripts are represented with the prefix "jaccard_analysis_". The rest of the directory is the output from those analyses.

"5 - Statistical Analysis": This directory stores scripts and samples from Jaccard Analysis, Cost Analysis and TDS score. These are categorised into sub-directories with the name of corresponding projects. Statistical tests (Shapiro-Wilk/U-Mann Whitney) scripts utilised to produce evaluation results are also uploaded here.

The following files apply to several areas/sections of the paper:

Files with the suffix "_Analysis" in the root repository are mined dataset, defined threshold, and analyses (Cost, TDS score) of their samples and complied statistical test results. These files are categorised with corresponding project names.

"Cross Project Analysis" store analysis used in the Evaluation and cross-project analysis of Apache Accumulo and Apache Cocoon, including their statistical test summary.

"Weighting Rationale" shows weightings conditions utilised in the paper, reformatted as spreadsheet formulas.
