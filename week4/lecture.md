---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Lecture: Big Data in the public domain

This week we will focus on the large amount of data available in the public domain that we can utilize within our research in sustainability sciences.

`````{admonition} Learning objectives week 4
:class: important
- Understand what type of data is available.
- Understand how licensing works.
- Know how to access OpenStreetMap and perform basic spatial analysis on this data.
- Know how to combine different open-access spatial datasets to perform a natural hazards risk assessment. 
`````

## Overview of data sources
There are many places on online where we can find large amounts of public data to be used within our discipline. Below we highlight a few of the most used data sources.

- [**Google Earth Engine Data Catalogue**](https://developers.google.com/earth-engine/datasets).Earth Engine's public data archive includes more than forty years of historical imagery and scientific datasets, updated and expanded daily. 
- [**Copernicus Climate Data Store**](https://cds.climate.copernicus.eu/#!/home). CDS datasets include observations, historical climate data records, estimates of Essential Climate Variables (ECVs) derived from Earth observations, global and regional climate reanalyses of past observations, seasonal forecasts and climate projections. Access to data is open, free and unrestricted.
- [**Our World in Data**](https://ourworldindata.org/). Our World in Data (OWID) is a scientific online publication that focuses on large global problems such as poverty, disease, hunger, climate change, war, existential risks, and inequality.
- [**Worldpop**](https://www.worldpop.org/). Open access spatial demographic datasets built using transparent approaches.
- [**CMIP6**](https://www.wcrp-climate.org/about-wcrp/wcrp-overview). Coupled Model Intercomparison Project Phase 6. The objective of CMIP is to better understand past, present and future climate changes arising from natural, unforced variability or in response to changes in radiative forcing in a multi-model context. This understanding includes assessments of model performance during the historical period and quantifications of the causes of the spread in future projections. An important goal of CMIP is to make the multi-model output publicly available in a standardized format.
- [**OpenStreetMap**](https://www.openstreetmap.org/). A  free, editable map of the whole world that is being built by volunteers largely from scratch and released with an open-content license.
- [**ThinkHazard**](https://thinkhazard.org/en/). ThinkHazard! provides a general view of the hazards, for a given location. The hazard levels provided are based on published hazard data, provided by a range of private, academic and public organizations.
- [**Eurostat**](https://ec.europa.eu/eurostat). Statistics and data on Europe. Both tabular and spatially explicit.
- [**EM-DAT**](https://www.emdat.be/).EM-DAT contains essential core data on the occurrence and effects of over 22,000 mass disasters in the world from 1900 to the present day. 
- [**IPUMS**](https://www.ipums.org/). IPUMS provides census and survey data from around the world integrated across time and space.
- [**GADM**](https://gadm.org/). GADM provides maps and spatial data for all countries and their sub-divisions. 
- [**Global Flood Database**](https://global-flood-database.cloudtostreet.ai/). The Global Flood Database contains maps of the extent and temporal distribution of 913 flood events occurring between 2000-2018.

## Licensing of data in the public domain
The most common license for public data is the Creative Commons license. Creative Commons licenses give everyone from individual creators to large institutions a standardized way to grant the public permission to use their creative work under copyright law. From the reuser’s perspective, the presence of a Creative Commons license on a copyrighted work answers the question, “What can I do with this work?” 

You can find all the information about the Creative Commons license [here](https://creativecommons.org/about/cclicenses/).

## FAIR - principles
The FAIR principles constitute a set of guidelines for effective data management, formally introduced in a pivotal 2016 paper authored by a collaborative consortium of scientists and organizations, [published in the journal Scientific Data](https://www.nature.com/articles/sdata201618). FAIR stands for  **F**indability, **A**ccessibility, **I**nteroperability, and **R**euse. These principles prioritize ensuring that data is easily discoverable, accessible, interoperable, and reusable. At its core, the FAIR framework seeks to address the challenges posed by the ever-expanding volume and complexity of data, coupled with the accelerating pace at which new data is generated. Especially when dealing with big and publicly accessible data, a clear set of rules and principles are essential to ensure the reproducability of your work.  

The acronym FAIR encapsulates a set of principles that extend beyond mere data organization; they underscore the necessity for machine-actionability. As our dependence on computational systems continues to intensify, the FAIR principles emphasize the importance of enabling these systems to autonomously discover, access, interoperate, and reuse data with minimal human intervention. This distinctive feature ensures that the principles remain relevant in the face of evolving technological landscapes and the increasing reliance on automated processes in data management.

`````{admonition} The FAIR-principles
:class: tip
**To be Findable**:

F1. (meta)data are assigned a globally unique and persistent identifier

F2. data are described with rich metadata (defined by R1 below)

F3. metadata clearly and explicitly include the identifier of the data it describes

F4. (meta)data are registered or indexed in a searchable resource

**To be Accessible**:

A1. (meta)data are retrievable by their identifier using a standardized communications protocol

A1.1 the protocol is open, free, and universally implementable

A1.2 the protocol allows for an authentication and authorization procedure, where necessary

A2. metadata are accessible, even when the data are no longer available

**To be Interoperable**:

I1. (meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation.

I2. (meta)data use vocabularies that follow FAIR principles

I3. (meta)data include qualified references to other (meta)data

**To be Reusable**:

R1. meta(data) are richly described with a plurality of accurate and relevant attributes

R1.1. (meta)data are released with a clear and accessible data usage license

R1.2. (meta)data are associated with detailed provenance

R1.3. (meta)data meet domain-relevant community standards
`````

You can read more about the FAIR-principes [here](https://www.go-fair.org/fair-principles/)