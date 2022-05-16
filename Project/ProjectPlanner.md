# Scikit learn Random Forests tutorial

## Executive summary

### <span style="color:red">The big goal </span>
Machine learning algorithms are mathematical model mapping methods used to learn or uncover underlying patterns embedded in the data. There is such a vast quantity of new algorithms/libraries being created to learn and explore that many novice and new researchers are often scared away from using them. The creation of easy to follow tutorials and ease of access to these is very important to allow everyday researchers the opprotunity to learn and develop their research skills.

The random forest classifier is an extremely powerful decision tree ensemble model that can be used to both classify and perform regression on datasets. The development of a easy to follow tutorial based around this package will increase many researchers access to machine learning algorithms for their studies.

### <span style="color:red"> The Tutorial </span>
The scikit-learn 'Random Forest' tutorial aims to build upon basic knowledge of stastical learning models with a practical demostration of random forests. The tutorial is designed that anybody with basic python experience can follow allong a guiged demonstration, with options to try things out yourself. By doing so the model trys to build all the skills and understandings of the packages core functions that you can use it yourself with any of your own data.

The tutorial consists of 6 notebooks that cover loading the package and data in, data visualisation, data pre-processing, forest building and evaluating model performance. The notebook uses an inbuilt data package to show its cabailities, but the end user will learn how to use this with their own research and data.

### <span style="color:red"> The Next Steps </span>
The end user can take this tutorial and either substitute out the base data for their own, but more importantly will have the required knowledge to actually implement random forests from scratch. 

Future capabilities will be greatkly increased, and the ability to take what has been learnt here to other machine learning algorithms will be greatly increased. 




## Goals

- Demonstrate the scikit-learn random forest fucntionality on a dataset from beggining to end. This will include performing a full classification on some dataset.
- Detail the workflow/ create a framework that users will need to take for implementing random forests
- Decribe what each process in the random forest package is doing so the average user will understand, and know why they need to undertake a certain step.
- Explain data pre-processing for categorical type data 


## Background and Innovation  

In spatial modelling and environmental analysis it is very important to find relationships between predictor and response variables. However, the field of data modelling and machine learning algorithms is very extensive, with each algorithm operating differently from the next. There is such a vast range of algorithms that it often becomes difficult to know what to adopt, and how to adopt it! Learning the nature of data and the outcomes you are trying to achieve is not often intuitive and so easy workflows and packages mean you can find examples like yours and work through them easily. For many user the adoption of machine learning is very daunting, and it is often difficult to even get these algorithms to work. Although attempts are being made in geospatial programs such as ArcGIS to incorporate machine learning, these often are very clunky, and limited in what they can do. The switch from these programs to python furthers the complications of users in analysing their environmental data. 

One of the most used classifiers today is the random forests, which is offered in the scikit learn package. Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time. For classification tasks, the output of the random forest is the class selected by most trees. For regression tasks, the mean or average prediction of the individual trees is returned. This algorithm can greatly increases model performance over tyipcal logisitc regression, which some geospatial programs offer. 

The scikit learn package has many modules within it, and also requires seperate modules to load data in, tranform data and visualise data. To help users with this package, a series of tutorial modules and example workflows will greatly improve ease of use. 


## Resources & Timeline

_What do you have at your disposal already that will help the project along. Did you convince somebody else to help you ? Are there already some packages you can build upon. What makes it possible to do this project in the time available. Do you intend to continue this project in the future ?_


The random forest is a fully developed package from scikit-learn. Although documentation is quite extensive for this package it is very difficult to follow without deeper explanations and examples. To build my tutorial I have used both my experience in learning it, and a combination of online tutorials to build what I think is the easiest to follow tutorial.

I will build my tutorials on a format similar to that of the workbooks we have been looking at in class. This format usually consists of around 4-5 notebooks to expalin some fucntionality of python. Instead I will use 4-5 notebooks to explain the functionality of random forests

### Data
 - I will be incorporating panda dataframes and matplotlib libraries for data control and plotting. 
 - I will be using the IRIS dataset, which is a famous multivariate dataset describing flower characteristics of three iris species. The dataset consists of 50 labelled samples, with 4 float columns.
 - I will also be using a prebuilt NOAA temperature dataset to show users with categorical data how to pre-process it for random forests.
  
### Timeline
- The first step in this will be too learn the random forest package myself, I will implement it on my own data for honours to see how it works differently to what I previously had done. I can make comments on what was difficult to follow, and issues I incurred to include as details in the tutorial I expect this to take 3-4 days.
- To build this workbook I will first look at a variety of other tutorial resources (class notebooks and onlibe tutorials). I expect this to take between 5-6 hours
- To structure the notebooks I will use my implentation of random forests and susbtitute my data for the IRIS dataset, so it works cleanly and is avaliable for all users.
- Writing the code for the random forest will take between 1-2 days.
- Writing the supporting documentation and descriptions for the tutorial will take a further 3-4 days.
- The packaging, creation of tests and uploading to github is expected to take a further day.


## Testing, validation, documentation

**Note:** You need to think about how you will know your code is correct and achieves the goals that are set out above (specific tests that can be implemented automatically using, for example, the `assert` statement in python.)  It can be really helpful if those tests are also part of the documentation so that when you tell people how to do something with the code, the example you give is specifically targetted by some test code.

_Provide some specific tests with values that you can imagine `assert`ing_

- The random forests has prebuilt functions, so rather testing agaisnt these I will aim to test the user has actually loaded the packages in correctly, and is creating getting results which allign with what is expected.

I can test for:
- The random forest package is imported and part of the system variables
- the user has created a panda data frame
- the user has created a random forest ensemble


```python

```
