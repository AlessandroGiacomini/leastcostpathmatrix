# Project: Find the least cost path on a Matrix
# Alessandro Giacomini
-----------------------------------

## Description
-----------------------------------

### Live [here](http://leastcostpathmatrix.appspot.com/)

A robot which can move down and right is traversing some terrain that can be represented as a hex grid. Find the least cost path from top left to bottom right through such a grid. Return the path for the robot to follow.

I decided to insert two bottons:
- "Play with a new Matrix button" which works with a random matrix 6x6
- "Play Sample Matrix button"  which works with the following Sample input matrix

### Sample input

[['46B', 'E59', 'EA', 'C1F', '45E', '63'], 
['899', 'FFF', '926', '7AD', 'C4E', 'FFF'], ['E2E', '323', '6D2', '976', '83F', 'C96'], ['9E9', 'A8B', '9C1', '461', 'F74', 'D05'], ['EDD', 'E94', '5F4', 'D1D', 'D03', 'DE3'], ['89', '925', 'CF9', 'CA0', 'F18', '4D2']]
 
### Sample output

Minimun cost from left/top to right/down: 24146

Least cost path: r,r,d,d,r,d,d,r,r,d

## How to Run Project
------------------

* Install the [Google App Engine SDK for Python](https://cloud.google.com/appengine/downloads)
* Sign up for a GAE account ([instructions](https://sites.google.com/site/gdevelopercodelabs/app-engine/creating-your-app-engine-account))
* Clone the repo with ```git clone https://github.com/AlessandroGiacomini/leastcostpathmatrix.git```

run the application through the GAE Launcher GUI
- File -> Add Existing Application
- Add project
- Click Browse