from bs4 import BeautifulSoup
import requests, datetime
import pandas as pd
import tweez


metadata = []
    
for i in tweez.urls:
    urlPDF = i.replace('/abs/', '/pdf/') + '.pdf'
    result = requests.get(i)
    URLchecker = result.status_code
    if URLchecker != 200:
        print('Please enter correct URL')
        exit()
    src = result.content
    soup = BeautifulSoup(src, "html.parser")

    # Getting the submitted date of the article
    # TODO: the submission dates are actually mutiple lines where resubmitted dates also appear. Check that 
    submittedDate = soup.find(class_='dateline').find_all(text=True, recursive=False)[0].strip()[14:].rstrip(']')
    format = '%d %b %Y'
    submittedDate_format = datetime.datetime.strptime(submittedDate, format)
    pub_date = str(submittedDate_format.date())
    # Getting the title of the article
    title = soup.find(class_='title mathjax').find_all(text=True, recursive=False)[0]
    # Getting the Author list
    authorList = soup.find(class_='authors').find_all(text=True, recursive=True)[1:]
    #cleaning the Author List
    authors = []
    finalAuthorList = []
    for i in authorList:
        i = str(i)
        if i != ', ':
            authors.append(i)
    for i in authors:
        aSplit = i.split(' ')
        fname = aSplit[0]
        lname = aSplit[1] 
        authorNameSplit = lname + ', ' + fname
        finalAuthorList.append(authorNameSplit)
    # Getting the Abstract
    abstract = soup.find(class_='abstract mathjax').find_all(text=True, recursive=False)[1].strip()
    metadata.append({'title':title, 'pub_date': pub_date, 'authors': finalAuthorList, 'abstract': abstract, 'FTURL': urlPDF})
# # Data Sciencing
metadata_df = pd.DataFrame(metadata)
metadata_df.to_csv('arxiv_metadata.csv')