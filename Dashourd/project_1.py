import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


def load_data(file_path):
    data= pd.read_csv(file_path)

    data.drop_duplicates(inplace=True)
    return data

st.title("Data Visualization Dashboard Developer")
tab1,tab3, tab4,tab5, tab6,tab7, tab8,tab9, tab10= st.tabs(["1","3",'4','5','6','7','8','9','10'])

# Image Inference Section
with tab1:
     # Choose the time interval (daily, weekly, monthly, yearly)
    interval = st.radio("Select Time Interval", ["Daily", "Weekly", "Monthly", "Yearly"])

    # Group data based on the selected time interval
    if interval == "Daily":
        data_daily = pd.read_csv('E:/streamlit/New folder/Daily_registration_subscription_counts.csv')
        st.dataframe(data_daily)

    # Create a Streamlit web app
    

        # Group data by date and calculate the number of registered and subscribed users
        daily_counts = data_daily.groupby('d_date').agg({'registered_users': 'sum', 'subscribed_users': 'sum'}).reset_index()

        # Line chart to visualize daily counts
        fig_daily = px.line(daily_counts, x='d_date', y=['registered_users', 'subscribed_users'], title='Daily User Registration and Subscription')
        fig_daily.update_layout(xaxis_title='Date', yaxis_title='Number of Users')

        # Display the daily plot in the Streamlit app
        st.plotly_chart(fig_daily)

    elif interval == "Weekly":
        data_weekly = load_data('E:/streamlit/New folder/Week_registration_subscription_counts.csv')



            # Display weekly counts as a table
        st.header("Weekly User Registration and Subscription Counts")
        st.dataframe(data_weekly)

            # Line chart to visualize weekly counts
        fig_weekly = px.line(data_weekly, x='week', y=['registered_users', 'subscribed_users'], title='Weekly User Registration and Subscription')
        fig_weekly.update_layout(xaxis_title='Week', yaxis_title='Number of Users')

            # Display the weekly plot in the Streamlit app
        st.plotly_chart(fig_weekly)

    elif interval == "Monthly":
        data_monthly = load_data('E:/streamlit/New folder/M_registration_subscription_counts.csv')



            # Display monthly counts as a table
        st.header("Monthly User Registration and Subscription Counts")
        st.dataframe(data_monthly)

            # Line chart to visualize monthly counts
        fig_monthly = px.line(data_monthly, x='month', y=['registered_users', 'subscribed_users'], title='Monthly User Registration and Subscription')
        fig_monthly.update_layout(xaxis_title='Month', yaxis_title='Number of Users')

            # Display the monthly plot in the Streamlit app
        st.plotly_chart(fig_monthly)

    elif interval == "Yearly":
        data_yearly = load_data('E:/streamlit/New folder/year_registration_subscription_counts.csv')


            # Display yearly counts as a table
        st.header("Yearly User Registration and Subscription Counts")
        st.dataframe(data_yearly)

            # Line chart to visualize yearly counts
        fig_yearly = px.line(data_yearly, x='year', y=['registered_users', 'subscribed_users'], title='Yearly User Registration and Subscription')
        fig_yearly.update_layout(xaxis_title='Year', yaxis_title='Number of Users')

            # Display the yearly plot in the Streamlit app
        st.plotly_chart(fig_yearly)
        import os
        path=os.getcwd()
        print(path)
    
    ###############################################################################################
with tab3:
    df = load_data('E:/streamlit/New folder/10k AI initiative.csv')
    df=df[['user_id','completed_courses_count',	'last_completion_date',	'last_completed_course_degree',	'level']]
    df_sorted = df.sort_values(by='completed_courses_count', ascending=False)

        # Filter for users who have completed courses
    completed_users = df_sorted[df_sorted['completed_courses_count'] > 0].reset_index(drop=True)

        # Display the Streamlit app
    st.title("Users Dashboard")
    st.dataframe(completed_users)

        # Additional Information
    st.subheader("Additional Information:")
    st.write(f"Total Users: {len(df)}")
    st.write(f"Total Completed Courses: {completed_users['completed_courses_count'].sum()}")


###############################################################

with tab4:


    # Choose the time interval (daily, weekly, monthly, yearly)
    interval = st.radio("Select Time Interval", ["Currently Learning", "Monthly", "Yearly"])

    if interval == "Currently Learning":
        df = pd.read_csv('E:/streamlit/New folder/user_courses.csv')

        if 'user_id' in df.columns and 'course_id' in df.columns:
            # Group data by user_id and count the number of currently learning courses
            currently_learning_courses = df.groupby('user_id')['course_id'].nunique().reset_index()
            currently_learning_courses.columns = ['user_id', 'currently_learning_courses_count']
            
            # Sort the data in descending order of currently_learning_courses_count
            currently_learning_courses = currently_learning_courses.sort_values(by='currently_learning_courses_count', ascending=False)

            # Display the table
            st.subheader("Currently Learning Courses Count:")
            st.dataframe(currently_learning_courses)

            # Visualize currently learning courses count
            st.subheader("Bar Chart:")
            bar_chart = px.bar(
                currently_learning_courses,
                x='user_id',
                y='currently_learning_courses_count',
                labels={'currently_learning_courses_count': 'Number of Courses'},
                title='Number of Currently Learning Courses per User'
            )
            st.plotly_chart(bar_chart)
        else:
            st.error("Column 'user_id' or 'course_id' not found in the dataset.")
            
    elif interval == "Monthly":
        df = load_data('E:/streamlit/New folder/this_M_ Completed_Courses.csv')

        if 'user_id' in df.columns and 'completed_courses_count' in df.columns:
            # Sort the data in descending order of completed_courses_count
            df = df.sort_values(by='completed_courses_count', ascending=False)

            # Display the table
            st.subheader("Completed Courses Count:")
            st.dataframe(df[['user_id', 'completed_courses_count']])

            # Visualize completed courses count
            st.subheader("Bar Chart:")
            bar_chart = px.bar(
                df,
                x='user_id',
                y='completed_courses_count',
                labels={'completed_courses_count': 'Number of Completed Courses'},
                title='Number of Completed Courses per User this month.'
            )
            st.plotly_chart(bar_chart)
        else:
            st.error("Column 'user_id' or 'completed_courses_count' not found in the dataset.")
            
    elif interval == "Yearly":
        df = load_data('E:/streamlit/New folder/this_y_ Completed_Courses.csv')

        if 'user_id' in df.columns and 'completed_courses_count' in df.columns:
            # Sort the data in descending order of completed_courses_count
            df = df.sort_values(by='completed_courses_count', ascending=False)

            # Display the table
            st.subheader("Completed Courses Count:")
            st.dataframe(df[['user_id', 'completed_courses_count']])

            # Visualize completed courses count
            st.subheader("Bar Chart:")
            bar_chart = px.bar(
                df,
                x='user_id',
                y='completed_courses_count',
                labels={'completed_courses_count': 'Number of Completed Courses'},
                title='Number of Completed Courses per User this year'
            )
            st.plotly_chart(bar_chart)
        else:
            st.error("Column 'user_id' or 'completed_courses_count' not found in the dataset.")


    #################################5%######################################################
with tab5:



    st.header("User Information Dashboard")

        # Load data
    data = load_data('E:/streamlit/New folder/users_com_5.csv')

        # User search input
    user_id_search = st.text_input("Enter User ID:")

        # Check if user_id is provided
    if user_id_search:
            # Filter data for the specified user_id
        user_data = data[data['user_id'] == int(user_id_search)]

            # Check if user_data is empty (no user found)
        if user_data.empty:
            st.warning(f"No user found with User ID: {user_id_search}")
        else:
                # Display user information
            st.header("User Information:")
            user_info_columns = ['subscribed', 'coupon', 'registration_date',
                                    'level', 'gender', 'age', 'study_degree', '10k_AI_initiative']
            user_info_data = user_data[user_info_columns].drop_duplicates().reset_index(drop=True)
            st.table(user_info_data)

                # Display completed courses information
            st.subheader("Completed Courses:")
            courses_columns = ['course_title',
                                'completed_course_degree', 'completed_course_completion_date']
            courses_data = user_data[courses_columns].drop_duplicates().reset_index(drop=True)
            st.table(courses_data)

                # Display capstones information
            st.subheader("Capstones:")
            capstones_columns = ['capstone_chapter_id', 'capstone_lesson_id', 'capstone_degree', 'lock',
                                    'reviewed']
            capstones_data = user_data[capstones_columns].drop_duplicates().reset_index(drop=True)
            st.table(capstones_data)
    else:
        st.warning("Enter a User ID to search.")

    
    #################66666666666666666666666666666666666666
with tab6:




    # Sidebar
    st.header("Capstone Evaluation Dashboard for each admin")
    interval = st.radio("Select Time Interval", ["this day", "this week", "this month", "this year"])

    # Main content
    

    # Load data based on the selected time interval
    if interval == "this day":
        st.write("There is no capstones evaluated for today")

    elif interval == "this week":
        
        st.write("There is no capstones evaluated for this week")
        

    elif interval == "this month":
        data_this_month = load_data('E:/streamlit/New folder/Capstones evaluated this month.csv')
        st.dataframe(data_this_month)

    elif interval == "this year":
        data_this_year = load_data('E:/streamlit/New folder/Capstones evaluated this year.csv')
        st.dataframe(data_this_year)

      



############################################################
with tab7:

    capstones = load_data('E:/streamlit/New folder/capstones.csv')
    eval_history = load_data('E:/streamlit/New folder/capstone_evaluation_history.csv')

    # Merge the two DataFrames on the common columns (course_id and user_id)
    merged_data = pd.merge(capstones, eval_history, on=['course_id', 'user_id'], how='left')

    # Create a Streamlit web app
    st.title("User Capstones and Evaluation History Dashboard")

    # Display the merged data table
    df_7=[['user_id',	'course_id',	'chapter_id',	'lesson_id',	'degree',	'lock',	'last_submission_date',	'reviewed'	,'revision_date'
           ,'eval_history_id',	'admin_id'	

]]
    st.write(merged_data)
#####################################888888888888888888
with tab8:


    coupons_data = load_data('E:/streamlit/New folder/copons.csv')


    st.title("Coupon Usage Dashboard")

    # Display the coupons data table
    #st.write("Coupons Data:")
    #st.write(coupons_data)
  
    df_8 = coupons_data[['coupon_id', 'copon_code', 'users']]

# Sort the DataFrame in ascending order based on the 'users' column
    df_8_sorted = df_8.sort_values(by='users', ascending=False)

  


    # Display the coupon usage counts table
  
    st.write(df_8_sorted)
########################999999999999999999999999999
with tab9:
    users_data = load_data('E:/streamlit/New folder/users (1).csv')


    st.title("User Statistics Dashboard")

    # Group data by age and study degree and calculate the number of users in each group
    user_groups = users_data.groupby(['age', 'study_degree']).size().reset_index(name='user_count').sort_values(by='user_count', ascending=False)

    # Display the user groups table
   
    st.write(user_groups)
################################10000000000000000
with tab10:
    data = load_data('E:/streamlit/New folder/users_employment_pending_submitted.csv')

    # Create a Streamlit web app
    st.header("Users Employment Grant Status and History")

   

    # Group data by user_id to get unique users and count of status values
    users_data = data.groupby('user_id').agg({
        'status': 'count',
        'submitted': 'sum',
        'preparation': 'sum',
        'pending': 'sum',
        'hold': 'sum',
        'inreview': 'sum',
        'shortlisted': 'sum',
        'postponed': 'sum',
        'accepted': 'sum'
    }).reset_index()

    # Display unique users and their employment grant status count
 
    st.write(users_data)

    # Display the count of users in each employment grant status
    st.write("Count of Users in Each Employment Grant Status:")
    status_counts = data['status'].value_counts()
    st.bar_chart(status_counts)



    ##################################################
 




   