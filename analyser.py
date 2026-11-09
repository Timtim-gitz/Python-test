import pandas as pd

print("\n🚀 Connecting to live database to stream Human Development Index data...")

# Open database stream using the public source link
# Use the direct CSV endpoint for HDI data
# https://ourworldindata.org/grapher/human-development-index.csv?country=~OWID_WRL
# We keep this URL because it points to the raw dataset rather than the homepage.
data_url = "https://ourworldindata.org/grapher/human-development-index.csv?country=~OWID_WRL"

try:
    # 1. Read the spreadsheet directly from the web link using Python
    df = pd.read_csv(data_url, storage_options={'User-Agent': 'Data fetch/1.0'})
    print("✅ Success! Live data stream opened safely.")

    # 2. Clean up the naming of the main development index column
    df = df.rename(columns={'Human Development Index': 'HDI'})

    # 3. Filter the rows to look strictly at data for the year 2022
    df_2023 = df[df['Year'] == 2023].dropna(subset=['HDI'])

    # 4. Filter out regions (like 'Africa' or 'World') to keep only individual nations
    # This keeps rows where the Code is exactly 3 characters long (like ZAF, USA, KEN)
    df_countries = df_2023[df_2023['Code'].str.len() == 3]

    # 5. Calculate Summary Analysis Statistics
    top_nation = df_countries.sort_values(by='HDI', ascending=False).iloc[0]
    lowest_nation = df_countries.sort_values(by='HDI', ascending=True).iloc[0]
    global_average = df_countries['HDI'].mean()

    # 6. Print the final text summary report
    print("\n==================================================")
    print(" HUMAN DEVELOPMENT REPORT ENGINE ")
    print("==================================================")
    print(f"Global Average HDI Development Benchmark: {global_average:.3f}")
    print(f"Highest Index Nation: {top_nation['Entity']} ({top_nation['HDI']:.3f})")
    print(f"Lowest Index Nation: {lowest_nation['Entity']} ({lowest_nation['HDI']:.3f})")
    print("==================================================")

except Exception as error_msg:
    print(f"\n❌ Network or processing error occurred: {error_msg}")
    print("Please double check your internet connection and try running again.")