# EMSC4033 project plan template

## Scikit learn Random Forests tutorial

## Executive summary

Random forests are a decision tree based classifier, and regression algorithm. Random forests fits the gap between logisitc regression which has high bias and low variance and normal decision trees which have low bias and high variance. In this project I plan to develop a a tutorial package which 1) calls scikit learn packages and describes what each package does 2) provide a workflow notebook calling on functions to output classifications and predictions 3) example notebook which brings in shapefile data with attributes (ie tree presence/absence, location, eleveation, Topographic wetness and geology) and works through data conversion and formatting for random forest classification.


## Goals

- Develop an easy workflow and tutorial modules that describe how random forest and sk learn can be used to classify and predict in multidimensional datasets
- Implement functionality to take shapefile data and feed into random forests to test for spatial attribute importance.  


## Background and Innovation  

In spatial modelling and environmental analysis it is very important to find relationships between predictor and response variables. However, the field of data modelling and machine learning algorithms is very extensive, with each algorithm operating differently from the next. There is such a vast range of algorithms that it often becomes difficult to know what to adopt, and how to adopt it! Learning the nature of data and the outcomes you are trying to achieve is not often intuitive and so easy workflows and packages mean you can find examples like yours and work through them easily. For many user the adoption of machine learning is very daunting, and it is often difficult to even get these algorithms to work. Although attempts are being made in geospatial programs such as ArcGIS to incorporate machine learning, these often are very clunky, and limited in what they can do. The switch from these programs to python furthers the complications of users in analysing their environemental data. 

One of the most used classifiers today is the random forests, which is offered in the scikit learn package. Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time. For classification tasks, the output of the random forest is the class selected by most trees. For regression tasks, the mean or average prediction of the individual trees is returned. This algorithm can greatly increases model performance over tyipcal logisitc regression, which some geospatial programs offer. 

The scikit learn package has many modules within it, and also requires seperate modules to load data in, tranform data and visualise data. To help users with this package, particularily those using spatial data a series of tutorial modeuls and example workflows will greatly improve ease of use. 


_Give more details on the scientific problem that you are working on and how this project will advance the discipline or help with your own research.
(Where applicable, describe how people have been achieving this goal up to now, talk about existing packages, their limitations, whether you can generalise something to help other people use your code)._

## Resources & Timeline

_What do you have at your disposal already that will help the project along. Did you convince somebody else to help you ? Are there already some packages you can build upon. What makes it possible to do this project in the time available. Do you intend to continue this project in the future ?_


  - I’ll be using data of National Forest and Sparse Woodland from landsat satellite, with GA DEM, TWI and CSIRO TPI and GEOLOGY raster data spatially joined to points
  - I’ll detail how to use scikit learn package and the functions in the random forest module. I will package some of these into notebooks and examples.
  - I’ll describe a example workflow using the mentioned data and feed it through the described workflow to estimate classification of tree presence and predict tree presence given predictor variables.
  - This project will be achievable in the timeframe as the workflow is already documented, I just need to be able to explain and document it for a spatial analyst to understand.


## Testing, validation, documentation

**Note:** You need to think about how you will know your code is correct and achieves the goals that are set out above (specific tests that can be implemented automatically using, for example, the `assert` statement in python.)  It can be really helpful if those tests are also part of the documentation so that when you tell people how to do something with the code, the example you give is specifically targetted by some test code.

_Provide some specific tests with values that you can imagine `assert`ing_
