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

# Lecture: Course Introduction

This week we will kick-off the course. 

`````{admonition} Learning objectives week 1
:class: important
- Understand the concept of Big Data and how it can be used in sustainability sciences
- Know how this course is structured 
- Understand the basics of machine learning 
- Gain a basic understanding of Python and Jupyter Notebooks
`````

## Big data

`````{admonition} Definition of Big Data
:class: tip
Big data is a collection of massive and complex data sets and data volume that include the huge quantities of data, data management capabilities, social media analytics and real-time data. 
`````

## Python
Python is a programming language which allows us to give instructions to the computer. These instructions can be as simple as "add together these two numbers" or as complex as "give me the average CO2 concentration for 2020". For the former we will be able to complete the task using only a single instruction but for the latter, we may have to write a larger program containing hundreds or thousands of instructions.

This course is going to start from the beginning, showing you to talk to the computer to perform simple tasks and as you become more confident and follow the later courses, you will find that you are able to write much more complex programmes. Within this course, we assume no prior knowledge of Python. Experience with programming concepts or another programming language will help, but is not required to understand the material.

Python is a well-established language, with the current version (version 3) released in 2008 and it is installed by default on nearly all modern Linux systems. Python is also available for OS X and Windows.

```{seealso} 
You can find much more info about Python [here](https://docs.python.org/3/faq/general.html#what-is-python)
```

## What is machine learning?
Machine learning is a subfield of artificial intelligence, which is broadly defined as the capability of a machine to imitate intelligent human behavior. Artificial intelligence systems are used to perform complex tasks in a way that is similar to how humans solve problems.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7gbGavTLUUE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Machine learning starts with data — numbers, photos, or text, like bank transactions, pictures of people or even bakery items, repair records, time series data from sensors, or sales reports. The data is gathered and prepared to be used as training data, or the information the machine learning model will be trained on. The more data, the better the program.

“The function of a machine learning system can be *descriptive*, meaning that the system uses the data to explain what happened; *predictive*, meaning the system uses the data to predict what will happen; or *prescriptive*, meaning the system will use the data to make suggestions about what action to take,” the researchers wrote.  

There are three subcategories of machine learning:

**Supervised machine learning** models are trained with labeled data sets, which allow the models to learn and grow more accurate over time. For example, an algorithm would be trained with pictures of dogs and other things, all labeled by humans, and the machine would learn ways to identify pictures of dogs on its own. Supervised machine learning is the most common type used today.

In **unsupervised machine learning**, a program looks for patterns in unlabeled data. Unsupervised machine learning can find patterns or trends that people aren’t explicitly looking for. For example, an unsupervised machine learning program could look through online sales data and identify different types of clients making purchases.

**Reinforcement machine learning** trains machines through trial and error to take the best action by establishing a reward system. Reinforcement learning can train models to play games or train autonomous vehicles to drive by telling the machine when it made the right decisions, which helps it learn over time what actions it should take.

<img src="../_static/images/machine-learning-infographic_2.jpg" class="bg-primary mb-1">

