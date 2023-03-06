//Dara Sai Vineeth Kumar
//Roll no: 15EC35012
//MIES assigment 1 - Clustering


In this python script I implemented an algorithm for clustering.



First I imported the required libraries such as

  1.pandas for importing the dataset.

  2.random for assigning the initial centroids to random points.
  3.matplotlib for plotting the results and Visualization of results

.


I defined a total of 3 functions such as:

  1. dist: calculates the Euclidean distance between two points.

      function input contains two arguments each is a list of 2 numbers representing a point.
      function returns the Euclidean distance between the two given points.
  2. avgpt: calculates the centroid of given set of points.

      function input is a list of lists representing a list of points.

      function outputs a list of 2 numbers representing the centroid of given points.
  3. cendist: calculates the total sum of distances from a point to given set of points

      function input is a point and list of points
.
      function output is total sum of distances from point to all the other given points


.


After this is the main function.

let errlist be a list containing error corresponding to each k.



• We run the loop k times one for each k.

• If k is one then it means that we are considering only one centroid so we directly find the Centroid of all the points.

• Then we find the error for k=1 by mean of all the distances from this centroid to each data point. This error is stored in a list errlist.

• for k other than 1 we proceed with the following algo:

• We first randomly initialize k centroids.

   • For each data point we find its distance from each centroid and store this point in a list corresponding to the closest centroid.

   • After storing all the data points to corresponding Centroid lists, we find the mean of all the points belonging to each centroid list.

   • We call this mean list as newcen which means new centroids.

   • We check if this newcen is equal to cen, if both are same this mean that our centroids converged and we exit the loop.

   • If both are not same then we continue and find the new centroids until we reach convergence.

   • Once we reach convergence we find the error which is average distance from centroids to data points. we store this error in the errlist.

• After finding errors corresponding to each k we plot them using matplotlib lib to find the elbow point.





Obsevation:

• From the given dataset we find that the elbow point is at k=3. so optimum number of clusters is 3. we can also understand this from visualizing the given data set.

• We observe from the dataset plot that there are 3 seperable clusters means optimal k=3.





Result:

• So for this python script we gave two inputs. one is the dataset and the other is number of clusters for which we have to find the error.

• The output of the script is the plot error vs k from which we find the optimum number of clusters that describes the give dataset.

• The script also outputs a plot of the data points at elbow k=3 to understand more about the clusters. 



