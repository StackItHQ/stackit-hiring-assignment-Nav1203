
# StackIt Hiring Assignment

### Welcome to StackIt's hiring assignment! 🚀

**If you didn't get here through github classroom, are you sure you're supposed to be here? 🤨**


We are glad to have you here, but before you read what you're going to beat your head over for the next few hours (maybe days?), let's get a few things straight:
- We really appreciate honesty. Don't copy anyone else's assignment, it'll only sabotage your chances :P
- You're free to use any stack, and library of your choice. Use whatever you can get your hands on, on the internet!
- We love out of the box solutions. We prefer to call it *Jugaad* 
- This might be just the first round, but carries the most importance of all. Give your best, and we hope you have a fun time solving this problem.

## ✨ **Problem Statement: Crafting a CSV Importer for Google Sheets** ✨

**Context**:
Data analysts around the world 🌍, handle massive amounts of data to derive meaningful insights for their organization 📊. Among the tools they use, Google Sheets 📈 stands out due to its ease of use, accessibility, and collaborative features. However, many analysts have identified a recurring pain point: the cumbersome process of importing CSV files into Google Sheets repeatedly.

A typical week of an analyst in an e-commerce company 🛒 involves receiving multiple CSV files 📁 containing sales, inventory, customer feedback, and more. The data from these files needs to be meticulously analyzed and presented in the company’s weekly meetings. However, instead of diving directly into analysis, most analysts need to spend an inordinate amount of time just importing and structuring these CSV files into Google Sheets ⏳. This repetitive, time-consuming task reduces the efficiency of these professionals and delays the extraction of crucial insights 😫.

**Today, you are going to make their lives better.**

**Problem Statement**:
Make a CSV Importer for Google Sheets that lets users drag and drop CSV files onto the Google Sheet. The moment they drop the CSV file, allow them to select which columns to import 🗂️.

You get brownie points 🍪 if you can make it even easier by allowing them to filter the data as well before importing it into Google Sheets 🔍.

**Other pointers**:
- Import to Sheet – After validation and mapping, devise a method to populate the data into a chosen Google Sheet, either appending to existing data or creating a new sheet 📥📋.
- Optimize for Large Files – Large datasets are common in analytics. Your solution should effectively handle large CSV files (~15MB CSV file) without causing performance issues or prolonged waiting times 📈📦.

## Submission ⏰
The timeline for this submission is: **9AM, 30th Sept, 2023 - 12PM, 2nd Oct, 2023**

Some things you might want to take care of:
- Make use of git and commit your steps!
- Use good coding practices.
- Write beautiful and readable code. Well-written code is nothing less than a work of art.
- Use semantic variable naming.
- Your code should be organized well in files and folders which is easy to figure out.
- If there is something happening in your code that is not very intuitive, add some comments.
- Add to this README at the bottom explaining your approach (brownie points 😋)

Make sure you finish the assignment a little earlier than this so you have time to make any final changes.

Once you're done, make sure you **record a video** showing your project working. The video should **NOT** be longer than 120 seconds. While you record the video, tell us about your biggest blocker, and how you overcame it! Don't be shy, talk us through, we'd love that.

We have a checklist at the bottom of this README file, which you should update as your progress with your assignment. It will help us evaluate your project.

- [x] My code's working just fine! 🥳
- [x] I have recorded a video showing it working and embedded it in the README ▶️
- [x] I have tested all the normal working cases 😎
- [x] I have even solved some edge cases (brownie points) 💪
- [x] I added my very planned-out approach to the problem at the end of this README 📜

## Got Questions❓
Feel free to check the discussions tab, you might get something of help there. Check out that tab before reaching out to us. Also, did you know, the internet is a great place to explore 😛

## Developer's Section

https://github.com/StackItHQ/stackit-hiring-assignment-Nav1203/assets/99076767/61890ab4-27e6-404c-8904-67f7d336901c

[Youtube Link for High Quality](https://youtu.be/9BnMo900D4U)

Approach Taken
- The User Interface has been built using Streamlit.
- We import the dataset using streamlit components that can take in files using a file uploader object.
- We read the data as a dataframe using the pandas library
- Preview the dataset
- Check for null values and if present, notify the user about the number of null values and give the user 5 options to choose from
  - Fill values using forward fill or backward fill
  - Remove rows containing null values
  - Fill using mean of column
  - Fill using mode of column
  - Fill using median of column
- After the null values are removed, the user is asked to provide the google sheet link of where the data is to be pasted
- The user is also to provide the sheet name along with it.
- In the instructions column a service account mail is mentioned which the user is to copy and paste onto the users column and grant editor permission to it as well.
- After that if necessary the user can filter the dataset by column-wise or row-wise filtering
  - If the user is to column wise filter, he can choose the necessary columns using checkboxes or he can choose the range of indexes for the columns to keep
  - If the user is to row-wise filter, he can apply conditional filters such as less than - greater than, or omit certain values out
- On clicking upload, the uploaded data is written into sheet mentioned using the google sheets api for google cloud.  


Optimised code and well commented is present in the file interface.py

To work with the module, clone the repository in a folder using,

```bash
  git clone https://github.com/StackItHQ/stackit-hiring-assignment-Nav1203.git
```

Create a python virtual environment in the folder using,

```bash
  python -m venv venv
```

Activate the virtual environment and then run,

```bash
  pip install -r requirements.txt
```

In the terminal of the root folder, type,

```bash
  streamlit run interface.py
```

The app should be up and running in at localhost:8501


- [x] My code's working just fine! 🥳
- [x] I have recorded a video showing it working and embedded it in the README ▶️
- [x] I have tested all the normal working cases 😎
- [x] I have even solved some edge cases (brownie points) 💪
- [x] I added my very planned-out approach to the problem at the end of this README 📜

## Images of the App

![image](https://github.com/StackItHQ/stackit-hiring-assignment-Nav1203/assets/99076767/15340e42-9b5b-4d3e-ade9-171b04156199)

![image](https://github.com/StackItHQ/stackit-hiring-assignment-Nav1203/assets/99076767/416956eb-45dc-4cb3-85f0-66b6b60920d1)

![image](https://github.com/StackItHQ/stackit-hiring-assignment-Nav1203/assets/99076767/8679be7b-3fe2-42f8-9d92-59903fbffb46)

![image](https://github.com/StackItHQ/stackit-hiring-assignment-Nav1203/assets/99076767/91265b9b-7aa0-4815-af23-6ddf5728b395)


