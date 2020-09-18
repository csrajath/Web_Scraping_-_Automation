This is a twitter bot used to pull Arxiv Pre-Print articles, of last 24 hours, tweeted by Arxiv's support twitter handle. 
Sample Data Pull can be seen in 'arxiv_metadata.csv'
### Requirements
- The requirements for the same can be installed with `pip install requirments.txt`
### Improvements
- Currently the bot outputs a CSV. We can instead choose to pipeline it to a DB.
- It as been tested for Windows Task Scheduler and can be experimented with CronTab
- The code can be optimized by creating functions out of the blocks and reducing time complexity