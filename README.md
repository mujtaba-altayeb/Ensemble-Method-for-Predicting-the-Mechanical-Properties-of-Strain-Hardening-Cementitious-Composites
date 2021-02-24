# Ensemble-Method-for-Predicting-the-Mechanical-Properties-of-Strain-Hardening-Cementitious-Composites
A project that aims to build a model for predicting the behavior of Strain hardening cementitious composites also known as Engineered Cementitious Composites

> This project contains the SHCC data files and Codes for the FDNN Algorithm from the paper "An Ensemble Method for Predicting the Mechanical Properties of Strain Hardening Cementitious Composites" in CONSTRUCTION AND BUILDING MATERIALS journal.

The files in this project show our current progress on this work. The team is currently working to simplify the algorithm so that researchers are able to use it for any other applications.

# Data Description
To develop the model, data were collected from a comprehensive literature review of articles.
The dataset consists of several parameters related to the mix design and mechanical properties of SHCC. The mix design
parameters included in the database are the amount of cement, water, fine aggregate, fly ash, silica fume, cenosphere, blast
furnace slag, superplasticiser, coarse aggregate, accelerating admixtures, phase change materials, fibre weight, all represented
in percentage weight. The parameters related to fibre properties in the dataset are fibre type, volume (% volume), diameter
(Micro-meter), length (mm), tensile strength (MPa), and elastic modulus (GPa). The dataset also included rubber, light weight
aggregate, viscosity agent hydroxypropyl methylcellulose, Air entraining admixture, oiling agent, graphene oxide, and
defoamer represented in binary forms, i.e. 1 (was used in mix design) or 0 (was not used). Other experimental conditions are
included, they are water curing time (days), air curing time (days), high frequency & velocity casting (1 or 0), and temperature
(⸰C). Finally, the mechanical properties recorded in the dataset are the tensile stress at the first crack (MPa), tensile strain at
the first crack (%), peak tensile stress (MPa), peak tensile strain (%), flexural strength at the first crack (MPa), flexural strain
at the first crack (%), peak flexural Strength (MPa), peak flexural strain (%), and Compressive strength (MPa). In total, the
resulting data set contains 38 parameters, divided into 29 features and nine targets.

# Notation
For simplicity, the following abbreviations are used in the names of the FDNNs models inputs
* Compressive strength (cs)
* first crack tensile stress (ux1)
* peak tensile stress (ux2)
* first crack tensile strain (us1)
* peak tensile strain (us2)
* first crack flexural Strength (fx1)
* peak flexural strength (fx2)
* first crack flexural strain (fs1)
* peak flexural strain (fs2).

If you intend to use part or all of the SHCC dataset or the FDNN algorithm or model in this project, the authors Kindly request that you cite their work:

{Mohamedelmujtaba Altayeb, Wang Xin, Taha Hussein Musa}
**An Ensemble Method for Predicting the Mechanical Properties of Strain Hardening Cementitious Composites**
in CONSTRUCTION AND BUILDING MATERIALS journal.

For any questions or Inquires Please Contact me at:
mohamed.elmujtaba.o@outlook.com 
