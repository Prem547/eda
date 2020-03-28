### Project Overview

 This data set consists of three types of entities:

(a) the specification of an auto in terms of various characteristics

(b) its assigned insurance risk rating

(c) its normalized losses in use as compared to other cars.

The data consists of technical specifications of cars. The dataset is downloaded from UCI Machine Learning Repository

Content: The data concerns city-cycle fuel consumption in miles per gallon, to be predicted in terms of 3 multivalued discrete and 5 continuous attributes

Number of Instances: 398

Number of Attributes: 9 including the class attribute


### Learnings from the project

 I've learned how to visualize and extract the meaning out of the DATA using SEABORN & MATPLOT LIBRARIES.
Eliminating NAN values and replacing them using MEAN, MEDIAN & MODE approach
Counterplot
jointplot
correlation heatmap of the data
finging skewness of the numeric features
Label Encode the categorical features


### Approach taken to solve the problem

 1. Firstly, I've loaded the data and using describe() & info() methods i've learned what features and instances does data contain.
2. later i've plotted Histogram using SEABORN's SNS showing distribution of car prices 
3. plotted Jointplot showing relationship between 'horsepower' and 'price' of the car using SNS.JOINTPLOT()
4. To find the Correlation i've used heatmap for the better understanding
5. Used BOXPLOT Plot as it shows the variability of each 'body-style' with respect to the 'price'.
6. found the values having "?" in columns and replaced them with NAN and
7.Imputed the missing values of the numerical data with mean of the particular column and transformed them
8.tested the skewness of columns and transformed the features with skewness > 1 using square root transformation
9.I've finally Label encoded the features and Combined the 'height' and 'width' to make a new feature 'area' of the frame of the car.



### Challenges faced

 I've not faced any major challanges  but faced a few minor challanges  and i've overcomed 'em by reading documents and understood well & continued.


### Additional pointers

 NA


