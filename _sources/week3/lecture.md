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

Artificial neural networks (ANNs) are comprised of a node layers, containing an input layer, one or more hidden layers, and an output layer. Each node, or artificial neuron, connects to another and has an associated weight and threshold. If the output of any individual node is above the specified threshold value, that node is activated, sending data to the next layer of the network. Otherwise, no data is passed along to the next layer of the network.




## Model validation