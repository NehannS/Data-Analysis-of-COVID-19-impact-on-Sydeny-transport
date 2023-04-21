# Group 63 COMP2200 Group Project - Analysing the Impact Of COVID-19 On Public Transport In The Sydney Metropolitan Area
This repository contains all the data and analysis files for the group project for the unit COMP2200.

The goal of the analysis is to explore and understand what factors have lead to the significant changes seen in public transport usage throughout Sydney. 

With this new found information we create machine learning models to help understand when things will return to normal. 

### Group Members 

* Thomas Hall
* Sam Huynh
* S S Herath Mudiyanselage Nehan  Irushika Senevirathna
* Kavindu Nilhan Rankothge

### Summary
Sydney's metropolitan transport system has seen a significant decrease in usage since March 2020. The reason for such an occurance can be summed down to the introduction of the novel coronavirus, otherwise known as COVID-19, which has spread rampantly around the world. We closely analyse factors such as social distancing measures, socio economic status of areas and rate of reported cases and how that impacts the transport system. We finish the analysis by developing prediction models to help understand when things may go back to normal.


## Our Files
The notebooks titled Transport_Covid_notebook_Tom.ipynb, etc. are where we conducted our individual work to avoid overlap.

Final_Notebook_Visual_Analysis.ipynb is the combination of our work and where the visual and statistical analysis is provided.

Final_Notebook_Predictive_Analysis.ipynb includes the predicitive analysis part of our project. We use two notebooks to stop the overlapping of our datadframes.

Opal_Postcode_info.txt contains information regarding the area codes that we focus on in our analysis. 

The Scripts file contains all the scripts that Sam Huynh wrote which were used to scrape the appropriate information from the websites detailed in the proposal file. 

covid_nsw_data.csv is a dataset containing all the reports of covid cases throughout NSW. This file is updated regularly using covid_puller.py

opal_patronage_data.csv is a dataset contianing information regarding the tap on and tap off data for each metroplitan area throughout Sydney. This file is updated regularly using opal_patronage_scraper.py

seifa_overview_data.csv is a dataset conaining all the relatvent information for each regions SEC score. This file is updated regularly using sefia_puller.py

Group63-COMP2200.pdf is a pdf form of presentation slides used in our group presentation 