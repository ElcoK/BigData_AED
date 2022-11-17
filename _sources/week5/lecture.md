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

# Lecture: Earth Observation & Google Earth Engine

This week we will focus on what we can do with earth observation data and learn how to use the google earth engine to unleash the potential of earth observation data.

`````{admonition} Learning objectives week 4
:class: important
- Gain a basic understanding of the Google Earth Engine.
- Understand and know how you can use the Google Earth engine in Python. 
`````

## Google Earth Engine
Google Earth Engine is a cloud-based platform for planetary-scale geospatial analysis that brings Google's computational capabilities to bear on a variety of high-impact societal issues including deforestation, drought, disaster, disease, food security, water management, climate monitoring and environmental protection. 

The Google Earth Engine consists of a multi-petabyte analysis-ready data catalog co-located with a high-performance, intrinsically parallel computation service. It is accessed and controlled through an Internet-accessible application programming interface (API) and an associated web-based interactive development environment (IDE) that enables rapid prototyping and visualization of results.

The data catalog houses a large repository of publicly available geospatial datasets, including observations from a variety of satellite and aerial imaging systems in both optical and non-optical wavelengths, environmental variables, weather and climate forecasts and hindcasts, land cover, topographic and socio-economic datasets. All of this data is preprocessed to a ready-to-use but information-preserving form that allows efficient access and removes many barriers associated with data management.

Users can access and analyze data from the public catalog as well as their own private data using a library of operators provided by the Earth Engine API. These operators are implemented in a large parallel processing system that automatically subdivides and distributes computations, providing high-throughput analysis capabilities. Users access the API either through a thin client library or through a web-based interactive development environment built on top of that client library.

