# Amazon_Vine_Analysis :camping::compass:🏞️:fire:
*Analysis with Pyspark and AWS on Outdoor Products* 
## Project Overview 

For this project we are using Amazon's reviews for a catagory of outdoor products.  The purpose of the analysis is to determine if there is any bias torward favorable reviews from Vine members.  Amazon Vine program is a service that allows manufacturers to have reviews posted on Amazon for their pre-release items, for an additional fee.       

#### Software: 
-  **Google Colab**  Vine_Review_Analysis.ipynb
-  **PGAdmin**  Vine_Review_Analysis.ipynb
-  **AWS** Amazon_Reviews_ETL.ipynb
  -  S3 Buckets
  -  RDS Databases and Connections

#### Languages: 
-  **PySpark**  

## Results

In this analysis we analyze reviews taht have more than 
20 total votes and the percentage of the helpful votes is 
equal or greater than 50.   
***We can ask and answer the following questions:*** 

Question # 1- **How many Vine reviews were there?**  

There were
-   107 Vine reviews and 
-  39,869 non-Vine reviews

<p align="center">
  <img width="300" height="75" src="https://github.com/mjrotter4445/Amazon_Vine_Analysis/blob/main/Challenge%20work/Graphics/fig%201%20total%20vine%20and%20non.jpg">
</p>
<p align="center">
Figure 1-Total Vine and non-Vine reviews by Count
</p>

**In summary(counts),**
-   107 Vine reviews and 
-  39,869 non-Vine reviews


Question #2a - **How many Vine reviews were 5-stars? (counts)**

Question #2b - **How many non-Vine reviews were 5-stars? (counts)**

**In summary (counts),**
-   56 total 5-star Vine reviews (counts) and 
-  21,005 total 5-star non-Vine reviews (counts)

<p align="center">
  <img width="300" height="75" src="https://github.com/mjrotter4445/Amazon_Vine_Analysis/blob/main/Challenge%20work/Graphics/fig%202%205st%20count%20vine%20and%20non.jpg">
</p>
<p align="center">
Figure 2- 5-star Vine and non-Vine reviews by Count
</p>

Question #3a - **How many Vine reviews were 5-stars? (%)**

Question #3b - **How many non-Vine reviews were 5-stars? (%)**

**In summary (counts),**
-   52.34% were Vine reviews were 5-star and 
-   52.69% were non-Vine reviews (%)

<p align="center">
  <img width="300" height="75" src="https://github.com/mjrotter4445/Amazon_Vine_Analysis/blob/main/Challenge%20work/Graphics/fig%203%20perc%20of%205star%20vine%20and%20non.jpg">
</p>
<p align="center">
Figure 3- 5-star Vine and non-Vine review breakdown by Percentages
</p>

## Summary

The purpose of this analysis is to analyze and determine if there is any bias 
toward favorable reviews from Vine members in the dataset.  Our analysis reveals 
that more than 20 total votes and the percentage of helpful votes is equal or great 
than 50.  This selection was made in order to pick reviews that are more likely to 
be helpful.   

**Positivity bias for reviews in the Vine Program**
In the analysis, we analyze 5-star review within conditions mentioned above.  
Calculations show that there is **no positivity bias for reveiws in the vine 
program.**  The results show that 5-star views from Vine members is 52.34% and the 
5-star reviews from non-Vine members was 52.69%.  The Non-vine reviews has a 
slightly higher percentage of the 5-star reviews, but not significant.  

**Additional analysis that could be performed**
We could expand this analysis by calculating percentage for all stars reviews.  
Based on the results in Figure 4 below, there is a larger difference in percentage for 1-star
reviews than for 5-star reviews.    Vine reviews have only 0.93% of 1-star reviews, while non-vine 
reviews have 13.35% 1-star reivews within conditions mentioned above.  similarly, there 
is a 1.87% 2-stars Vine reviews and 6.05% 2-star non-vine reviews.  

<p align="center">
  <img width="800" height=200" src="https://github.com/mjrotter4445/Amazon_Vine_Analysis/blob/main/Challenge%20work/Graphics/fig%204%20bothV%20and%20nonV.jpg">
</p>
<p align="center">
Figure 4- Summary of star reviews - 2 charts side by side Vine and non-Vine
</p>

Another idea for analyis could be to do a deeper dive to find out when and if reviews impact
sales as the product life cycle progresses.  On the Amazon Vine homepage, a description 
encourages "their most trusted reviews" on amazon to post opinions abuot the new and pre-release items
to aid in product launch and marketing.   It would be interesting to know if these reviews had a direct
impace or correlation as the sales are tracked over time.   


