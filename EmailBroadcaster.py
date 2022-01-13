import streamlit as st
import pandas as pd
import os 
# The servers PORT that will be used
from server_setup import PORT

# Getting the email servers information
dir_path = os.path.dirname(os.path.realpath(__file__))
df = pd.read_excel(dir_path+'/emailServers.xlsx')

# Email that is going to be used 
values = df['Email'].tolist()
# The mail server
options = df['Server'].tolist()

st.sidebar.header("Details")

dic = dict(zip(options, values))

side = st.sidebar.selectbox('Choose a sender email', options, format_func=lambda x: dic[x])

import io
file_buffer = st.file_uploader("Upload Files")
# text_io = io.TextIOWrapper(file_buffer)
st.set_option('deprecation.showfileUploaderEncoding', False)
if file_buffer != None:
    df_emails = pd.read_excel(file_buffer)
    if (st.checkbox("Show contents"))==True:
        st.write(df_emails)

    #------------------------------------------------------------#
    #                       EMAIL SELECTION                      #
    #------------------------------------------------------------#
    st.write("______________________________________________________________________")
    column_name = st.selectbox("Choose the EMAIL column",(df_emails.columns).tolist())
    EMAILS = df_emails[column_name].unique()
    
    #------------------------------------------------------------#
    #                       NAME SELECTION                       #
    #------------------------------------------------------------#
    st.write("______________________________________________________________________")
    column_name_ref = st.selectbox("Choose the NAME column",(df_emails.columns).tolist())
    NAME = df_emails[column_name_ref].unique()

    st.write("______________________________________________________________________")
    #------------------------------------------------------------#
    #                       SELECT ALL                           #
    #------------------------------------------------------------#
    sel_all = st.checkbox("Select All Emails?")
    
    st.write("OR")

    if sel_all:
        data = EMAILS
    else:
        EMAILS_SELECTED = st.multiselect('Select Individual Emails', EMAILS)
        # Mask to filter dataframe
        mask_emails = df_emails[column_name].isin(EMAILS_SELECTED)
        data = df_emails[mask_emails]

        st.write("______________________________________________________________________")
    
    # Subject line of the email
    subject = st.text_input("Subject*")

    # Text area containing html used in
    arr_news_html = st.text_area(f"Enter the the message (in HTML):")

    if st.button("Send Email"):
        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        import os
        import io

        #can update
        sender_email = str(values[0])
        st.write(sender_email)

        password = (df['Password'].tolist()[0])
        
        text = arr_news_html
        
        for i in range(len(data)):
            recepientName = NAME[i]
            receiver_email = str(df_emails[column_name][i])
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = sender_email
            message["To"] = receiver_email

            # The HTML that will be the body and conlusion of the email
            html = """
            <html>
                <body>
                    <p>Hi {} </p>
                    {}
                </body>
            </html>
            """.format(recepientName,text)

            part2 = MIMEText(html, "html")

            message.attach(part2)

            #----------------------------------------------#
            #            ATTATCHING FILES                  #
            #----------------------------------------------#      
        
            # Create secure connection with server and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(str(side), PORT, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )