import praw
import xlwt
from xlutils.copy import copy
from xlrd import open_workbook

print('module test')

#Records all posts and links into and excel sheet (.XLS FORMAT ONLY)
rb = open_workbook("/Users/SYTang/Desktop/Programming/PRAW/dataisbeautifulmeta.xls",formatting_info=True) #change according to
r_sheet = rb.sheet_by_index(0) #READ-ONLY COPY (values are not modified)
wb = copy(rb)  # creates a writeable copy
w_sheet = wb.get_sheet(0)  #Creates a sheet within writable copy

rowx = 1 #STARTING ROW
col_indexnumber = 0
col_title = 1
col_url = 2
col_karma = 3
col_date = 4

number = 0

#Create a script application in reddit preferences. Change whenever making a new script/account
reddit = praw.Reddit(client_id='foi1cv65T5v13w',
                     client_secret='oa2Nn50n0irmIAwloOtq6K08_zM',
                     user_agent='Reddit_Post_Crawler')

print(reddit.read_only)  #Should Output False if above data is entered correctly

subreddit = reddit.subreddit('dataisbeautiful')


#Gets first n posts according to date or popularity
for submission in subreddit.new(limit=1000): #n most recent posts

    w_sheet.write(rowx,col_title, submission.title)
    w_sheet.write(rowx,col_url, submission.url)
    w_sheet.write(rowx,col_karma, submission.score)
    w_sheet.write(rowx,col_date, submission.created_utc)
    rowx += 1



wb.save("/Users/SYTang/Desktop/Programming/PRAW/dataisbeautifulmeta.xls") #change accordingly
