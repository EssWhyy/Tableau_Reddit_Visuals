# Tableau_Reddit_Visuals
##A couple of data visualisation projects I did using Tableau.

**Project 1: Analysing Karma Distribution of r/dataisbeautiful.**

I used PRAW (documentation here) to get all posts made in r/dataisbeautiful, a data visualisation subreddit, along with their titles, upload dates and karma counts, from there I sorted them into various categories of ascending karma, and illustrated as a heat map of sorts  in Tableau.

**Project 2: Analysing Subscriber Count of Various Global Subreddits.** 

This did not involve using PRAW but instead, common python data scraping modules. All subreddits have the same format url reddit.com/r/(subreddit_name). As such, it is possible to access multiple subreddits consecutively using python’s urllib module. I formatted a list of country names into an excel sheet and used Python to access each url, then used beautifulsoup, another python module, to get the number of subreddit subscribers of the subreddit, I copied the data to an excel sheet, sorted them into categories based on their size as in the first project and illustrated it in a world map graph in Tableau.


*To find out more about Tableau:  https://help.tableau.com/current/guides/get-started-tutorial/en-us/get-started-tutorial-home.htm*

