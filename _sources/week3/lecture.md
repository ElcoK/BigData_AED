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

# Lecture: Introduction to Artificial Neural Networks

This week we will focus on the basic concepts of machine learning and how we can develop a simply machine learning model.

`````{admonition} Learning objectives week 3
:class: important
- Understand the concept of Artificial neural networks.
- Understand and know how you can apply an artificial neural network model in Python. 
- Know how to validate and interpret your results.
`````

## Artificial neural networks
Neural networks are a commonly used, specific class of machine learning algorithms. Artificial neural networks are modeled on the human brain, in which thousands or millions of processing nodes are interconnected and organized into layers.

In an artificial neural network, cells, or nodes, are connected, with each cell processing inputs and producing an output that is sent to other neurons. Labeled data moves through the nodes, or cells, with each cell performing a different function. In a neural network trained to identify whether a picture contains a cat or not, the different nodes would assess the information and arrive at an output that indicates whether a picture features a cat.


## Model validation