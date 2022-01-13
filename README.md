# Automated Python Email Broadcaster

![](https://img.shields.io/badge/v3.9-Python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a)

![](https://img.shields.io/badge/Streamlit-Python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a)

This program aims to send a custom greeting to multiple individuals.


## Setup
Make sure that there exists a file emailServers.xlsx. emailServers.xlsx contains the following column headings:

|     Email    |    Password   |    Server       |

The information inserted into the rows below the headings would be in the following format e.g.

|test@test.com |     123456    | mail.server.com |

Multiple servers and emails can be set up by adding more rows.

## Usage 
1. Execute the following command in the terminal:

    run streamlit EmailBroadcaster.py

2. The dropdown menu on the left-hand side allows the user to change the sender email if there are multiple emails. 

3. In the main part of the program: Upload the excel sheet containing the names and emails.

4. Choose the Email column from the dropdown that is imported from the excel sheet.

5. Choose the Name column from the dropdown that is imported from the excel sheet.

6. Choose "Select All Emails?" or Individual emails can be chosen from the excel sheet.

7. Fill in the Subject* field.

8. Fill in the "Enter the message (in HTML)" text field.

9. Press the "Send Email" button.

## Improvements
- Determine if read receipts are available to determine if a person has opened the email.
- Move the server port to the emailServers.xlsx and access it from there.