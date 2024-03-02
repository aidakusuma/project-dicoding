import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bike_df = pd.read_csv('C:/Users/A.I/Documents/Bangkit Academy 2024 H1/Dicoding/project/dashboard/bike_data.csv')
print("\nData bike")
print(bike_df.head())

st.title('Dashboard peminjam sepeda terdaftar registered')
col1, col2 = st.columns(2)
with col1:
    total_registered = bike_df.registered_x.sum()
    st.metric("registered", value=total_registered)
with col2:
    total_days = len(bike_df['dteday_x'])
    st.metric("hari", value=total_days)
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    bike_df['dteday_x'],
    bike_df['registered_x'],
    marker='o',
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.set_xlabel("Tanggal", fontsize=15)
ax.set_ylabel("Registered", fontsize=15)
st.pyplot(fig)

st.title('\nDashboard peminjam sepeda terdaftar casual')
col3, col4 = st.columns(2)
with col3:
    total_casual = bike_df.casual_x.sum()
    st.metric("casual", value=total_casual)
with col4:
    total_day = len(bike_df['dteday_x'])
    st.metric("hari", value=total_day)
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    bike_df['dteday_x'],
    bike_df['casual_x'],
    marker='o',
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.set_xlabel("Tanggal", fontsize=15)
ax.set_ylabel("Casual", fontsize=15)
st.pyplot(fig)

st.title('Dashboard total peminjam sepeda')
casual_data_day = bike_df['casual_x']
registered_data_day = bike_df['registered_x']
mean_casual_day = casual_data_day.mean()
mean_registered_day = registered_data_day.mean()

casual_data_hour = bike_df['casual_y']
registered_data_hour = bike_df['registered_y']
mean_casual_hour = casual_data_hour.mean()
mean_registered_hour = registered_data_hour.mean()

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].bar(['Casual', 'Registered'], [mean_casual_day, mean_registered_day], color=['blue', 'orange'])
axes[0].set_xlabel('Tipe Anggota')
axes[0].set_ylabel('Rata-rata Peminjaman')
axes[0].set_title('per hari')
axes[1].bar(['Casual', 'Registered'], [mean_casual_hour, mean_registered_hour], color=['green', 'red'])
axes[1].set_xlabel('Tipe Anggota')
axes[1].set_ylabel('Rata-rata Peminjaman')
axes[1].set_title('per jam')
plt.suptitle('Perbandingan Rata-rata Peminjaman antara Casual dan Registered (per hari dan per jam)', fontsize=16)
st.pyplot(fig)

total_registered_workingday = bike_df.loc[bike_df['workingday_x'] == 1, 'registered_x'].sum()
total_registered_non_workingday = bike_df.loc[bike_df['workingday_x'] == 0, 'registered_x'].sum()
labels = ['Hari Kerja', 'Bukan Hari Kerja']
sizes = [total_registered_workingday, total_registered_non_workingday]
colors = ['coral', 'skyblue']
explode = (0.1, 0)  
st.title('Proporsi Peminjaman pada Hari Kerja dan Bukan Hari Kerja tipe registered')
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal') 
st.pyplot(fig)

total_casual_workingday = bike_df.loc[bike_df['workingday_x'] == 1, 'casual_x'].sum()
total_casual_non_workingday = bike_df.loc[bike_df['workingday_x'] == 0, 'casual_x'].sum()
labels = ['Hari Kerja', 'Bukan Hari Kerja']
sizes = [total_casual_workingday, total_casual_non_workingday]
colors = ['red', 'blue']
explode = (0.1, 0)  
st.title('Proporsi Peminjaman pada Hari Kerja dan Bukan Hari Kerja tipe casual')
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal') 
st.pyplot(fig)

st.title('Perbedaan Kontribusi Peminjaman Sepeda antara Dua Tipe Anggota')
fig = plt.figure(figsize=(8, 6))
sns.boxplot(data=[registered_data_day, casual_data_day], notch=True)
plt.xticks([0, 1], ['Registered_x', 'Casual_x'])
plt.title('Perbedaan Kontribusi Peminjaman Sepeda antara Dua Tipe Anggota')
plt.xlabel('Tipe Anggota')
plt.ylabel('Jumlah Peminjaman')
plt.show()
st.pyplot(fig)