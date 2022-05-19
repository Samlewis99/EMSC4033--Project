# Project Report

## Instructions
Lets run through how to access and use the tutorial workbooks. There are 6 workbooks in total and there is a structured order to follow along. This order goes:
1. Getting started
2. RF_1
3. RF_2
4. RF_3
5. RF_4
6. One Hot encoding (optional)

To access these notebooks we first need to clone the git repository to our local machine. To clone the project you will need to copy the link https://github.com/Samlewis99/EMSC4033--Project.git . If you are unfamiliar with how to clone a repository, it is really simple and there are plenty of fantastic resources on how this can be undertaken. Check out this link here if you need some guidance: https://www.educative.io/edpresso/how-to-clone-a-git-repository-using-the-command-line.

The individual notebook tutorials can be found in the "notebooks folder" of the cloned repository. These notebooks are guided step by step and if you simply want to follow along with them there is nothing for you to change. If you are wanting to import some of your own data you will need to load your data into the same directory where the repositroy has been cloned, or alternatively set a destiantion path when importing this data. If using trying to import a csv you can do this with the code: ```pandas.read_csv(r"path-to-file-name.csv")```


## List of dependencies
1.  Sklearn
 - datasets
 - model_selection.train_test_split
 - ensemble.RandomForestClassifier
 - metrics
 - tree.Plot_tree
2.  Pandas
3. Matplotlib
 - pyplot
4. Seaborn
5. Datetime

## Describe testings
As these functions have not been built by myself I am not creating assert tests for the functions themselves (as we know they already work). Instead the tests I create are for the user to use and check that they are following on correctly with the tutorial, and what they are getting is what is expected.

1. The first test is to see whether the user has installed all the correct dependencies onto their machine. 
2. The second test is to see whether their data has been correctly changed to a pandas dataframe
3. The third test is to see whether they created a random forest classifier model.
4. The fourth test is to see if their model has achieved a similar accuracy to what is expected if the correct parameters have been used. 
5. The fifth test is to see that the user has only float/or numerical values in their dataframe after one hot encoding


## Limitations
The tutorial is limited in the type of data that it looks at. In order for the tutorials to be easily followed along I used a dataset that I know would work out well. However, this is a limitation as it doesnt show how messy 'real world' data might behave in a random forest classifier. 

Real world data often has outliers, large amounts of noise, too many or too little predictor variables and be structured differently than a simple dataframe we might expect from a .csv. Although the tutorial shows how we can work with some of these issues it may not be reflecting the amount of time and effort that goes into cleaning real world data. I know this from my personal expereince of using random forests with my honours data, where the classifictation processing took alot longer than in these notebooks and the results were far less satisfactory. 

Secondly, when working with very large datasets, random forest can be very slow, and often it is not advised to run your classification on the whole dataset. This is known in machine learning as batch learning vs online learning. In batch learning the system is incapable of learning incrementely and must be trained in one batch. On-line learning however splits large datasets up and allows for incremental learning. This was not discussed in this tutorial as it is a much more complex aspect to machine learning, however with large real world datasets it might be a requirement to use On-line learning to get around computing requirements.

## Future research
To expand upon these tutorials in the future I would like to add two more modules in that would address some of the limitations mentioned above. The first would be a module on how we can laod spatial data (such as .shp) and convert this into a random forest compatable dataset. This is really important as spatial data often needs to be analysed for the spatial relationship, so understanding how to take a file like this into python would be important for many researchers. The other module would be explaining the difference between random forestes classifiers and regressors. Although I breifly touched on this there is a larger explanation and another example would be useful for peoples understandings. 
