import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import calendar
sns.set(style='dark')

days_df = pd.read_csv("day_data.csv")
hours_df = pd.read_csv("hour_data.csv")

def get_total_count_by_hour_df(hour_df):
    hour_count_df =  hour_df.groupby(by="hours").agg({"count_cr": ["sum"]})
    return hour_count_df

def count_by_day_df(hour_df):
    day_df_count_2011 = hour_df.query(str('dteday >= "2011-01-01" and dteday < "2012-12-31"'))
    return day_df_count_2011

def total_casual_df(hour_df):
    cas_df =  hour_df.groupby(by="dteday").agg({
        "casual": ["sum"]
    })
    cas_df = cas_df.reset_index()
    cas_df.rename(columns={
        "casual": "casual_sum"
    }, inplace=True)
    return cas_df

def total_registered_df(hour_df):
    reg_df =  hour_df.groupby(by="dteday").agg({
        "registered": "sum"
    })
    reg_df = reg_df.reset_index()
    reg_df.rename(columns={
        "registered": "register_sum"
    }, inplace=True)
    return reg_df
    
# Function to calculate correlation between two columns
def calculate_correlation(hours_df, col1, col2):
    correlation_value1 = hours_df[[col1, col2]].corr().iloc[0, 1]
    correlation_value2 = hours_df[[col1, col2]].corr().iloc[1, 1]
    corr_df = pd.DataFrame({
        "": [col1,col2],
        col2 : [correlation_value1,correlation_value2],
        col1 : [correlation_value2,correlation_value1]
    })
    return corr_df

# Display correlation heatmap using Seaborn
def plot_correlation_heatmap(df, cols):
    corr_matrix = df[cols].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='rocket', center=0)
    plt.title('Correlation Heatmap')
    st.pyplot(plt)
    
def avg_workingday(df):
    avg_usage = df.groupby('workingday').agg({'casual': 'mean', 'registered': 'mean'}).reset_index()
    return avg_usage

def plot_monthly_bike_counts(df):
    # df['month'] = pd.Categorical(df['month'], categories=
    # ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    # ordered=True)
    monthly_counts = df.groupby(by=["month", "yr"]).agg({"count_cr": "sum"}).reset_index()
    
    monthly_counts['month'] = monthly_counts['month'].apply(lambda x: calendar.month_name[x])

    # Ensure that the months are ordered from January to December
    month_order = list(calendar.month_name)[1:]  # Exclude the empty string at index 0
    monthly_counts['month'] = pd.Categorical(monthly_counts['month'], categories=month_order, ordered=True)

    # Create line plot
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=monthly_counts, x="month", y="count_cr", hue="yr", palette="viridis", marker="o")

    # Set plot labels and title
    plt.title("Total Sepeda Berdasarkan Bulan dan Tahun")
    plt.xlabel("Bulan")
    plt.ylabel("Total Sepeda")
    plt.legend(title="Tahun", loc="upper right")
    
    # Improve plot layout
    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot(plt)
    
days_df = pd.read_csv("day_data.csv")
hours_df = pd.read_csv("hour_data.csv")

datetime_columns = ["dteday"]
days_df.sort_values(by="dteday", inplace=True)
days_df.reset_index(inplace=True)   

hours_df.sort_values(by="dteday", inplace=True)
hours_df.reset_index(inplace=True)

for column in datetime_columns:
    days_df[column] = pd.to_datetime(days_df[column])
    hours_df[column] = pd.to_datetime(hours_df[column])

min_date_days = days_df["dteday"].min()
max_date_days = days_df["dteday"].max()

min_date_hour = hours_df["dteday"].min()
max_date_hour = hours_df["dteday"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://cdni.iconscout.com/illustration/premium/thumb/people-using-bike-rental-service-app-illustration-download-in-svg-png-gif-file-formats--application-rent-pack-vehicle-illustrations-4825721.png?f=webp")
    
        # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date_hour,
        max_value=max_date_hour,
        value=[min_date_days, max_date_days])

main_df_days = days_df[(days_df["dteday"] >= str(start_date)) & 
                        (days_df["dteday"] <= str(end_date))]

main_df_hour = hours_df[(hours_df["dteday"] >= str(start_date)) & 
                        (hours_df["dteday"] <= str(end_date))]

hour_count_df = get_total_count_by_hour_df(main_df_hour)
day_df_count_2011 = count_by_day_df(main_df_hour)
reg_df = total_registered_df(main_df_days)
cas_df = total_casual_df(main_df_days)
avg_usage = avg_workingday(main_df_hour) 

st.header('🚲 Bike Rental Dashboard ')
st.subheader('Daily Sharing')
col1, col2, col3 = st.columns(3)

with col1:
    total_orders = main_df_hour['count_cr'].sum()
    st.metric("Total Sharing Bike", value=total_orders)

with col2:
    total_sum = reg_df.register_sum.sum()
    st.metric("Total Registered", value=total_sum)

with col3:
    total_sum = cas_df.casual_sum.sum()
    st.metric("Total Casual", value=total_sum)
    


# Add correlation DataFrame to Streamlit dashboard
st.subheader("Pertanyaan 1: Apa faktor utama yang memengaruhi jumlah penggunaan sepeda ?")

plot_correlation_heatmap(main_df_hour, ['count_cr', 'humidity','temp','wind_speed','hours'])
st.markdown("<h3 style='text-align: center; color: White;'>Correlation</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<p style='text-align: center; color:White;'>Humidity</p>", unsafe_allow_html=True)
    hum_corr = calculate_correlation(main_df_hour, 'count_cr', 'humidity')
    st.write(hum_corr)
with col2:
    st.markdown("<p style='text-align: center; color:green;'>Temp</p>", unsafe_allow_html=True)
    temp_corr = calculate_correlation(main_df_hour, 'count_cr', 'temp')
    st.write(temp_corr)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<p style='text-align: center; color:White;'>Windspeed</p>", unsafe_allow_html=True)
    hum_corr = calculate_correlation(main_df_hour, 'count_cr', 'wind_speed')
    st.write(hum_corr)
with col2:
    st.markdown("<p style='text-align: center; color:White;'>Hours</p>", unsafe_allow_html=True)
    temp_corr = calculate_correlation(main_df_hour, 'count_cr', 'hours')
    st.write(temp_corr)

st.subheader("Pertanyaan 2 : Pelanggan casual lebih sering bersepeda di hari kerja atau libur ? juga sebaliknya")

fig, ax = plt.subplots(figsize=(16, 8)) 
sns.barplot(
    x='workingday',
    y='registered',
    data=avg_usage,
    label='Registered',
    color='tab:blue',
    ax=ax
)

sns.barplot(
    x='workingday',
    y='casual',
    data=avg_usage,
    label='Casual',
    color='tab:orange',
    ax=ax
)

for index, row in avg_usage.iterrows():
    ax.text(index, row['registered'], str(row['registered']), ha='center', va='bottom', fontsize=12)
    ax.text(index, row['casual'], str(row['casual']), ha='center', va='bottom', fontsize=12)

ax.set_xlabel("hari Libur")
ax.set_ylabel("Hari Kerja")
plt.xticks([0, 1], ['Hari Libur', 'Hari Kerja'])
ax.tick_params(axis='x', labelsize=20, rotation=0)
ax.tick_params(axis='y', labelsize=15)
ax.legend()
st.pyplot(fig)


st.subheader("Pertanyaan 3 : di bulan dan tahun berapakah penyewaan sepeda itu sedang tinggi dan di bulan apakah penyewaan sepeda itu sedang turun")
plot_monthly_bike_counts(main_df_hour)