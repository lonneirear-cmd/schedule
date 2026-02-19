import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.title("📅 My Schedule Manager")

FILE_NAME = "schedule.csv"

# 파일이 없으면 생성
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Time", "Title", "Description", "Priority"])
    df.to_csv(FILE_NAME, index=False)

df = pd.read_csv(FILE_NAME)

# 📌 사이드바 메뉴
menu = st.sidebar.selectbox("Menu", ["Add Schedule", "View Schedule", "Delete Schedule"])

# ------------------------
# 1️⃣ 일정 추가
# ------------------------
if menu == "Add Schedule":
    st.subheader("➕ Add New Schedule")

    date = st.date_input("Date")
    time = st.time_input("Time")
    title = st.text_input("Title")
    description = st.text_area("Description")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])

    if st.button("Save"):
        new_data = pd.DataFrame({
            "Date": [date],
            "Time": [time],
            "Title": [title],
            "Description": [description],
            "Priority": [priority]
        })
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(FILE_NAME, index=False)
        st.success("Schedule saved!")

# ------------------------
# 2️⃣ 일정 보기
# ------------------------
elif menu == "View Schedule":
    st.subheader("📖 View Schedule")

    view_option = st.radio("View by", ["All", "Select Date"])

    if view_option == "All":
        st.dataframe(df)

    else:
        selected_date = st.date_input("Select Date")
        filtered = df[df["Date"] == str(selected_date)]
        st.dataframe(filtered)

# ------------------------
# 3️⃣ 일정 삭제
# ------------------------
elif menu == "Delete Schedule":
    st.subheader("🗑 Delete Schedule")

    if not df.empty:
        delete_index = st.selectbox("Select schedule to delete", df.index)
        if st.button("Delete"):
            df = df.drop(delete_index)
            df.to_csv(FILE_NAME, index=False)
            st.success("Deleted successfully!")
    else:
        st.info("No schedules available.")
