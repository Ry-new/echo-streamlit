import streamlit as st
import pandas as pd


df_2022 = pd.read_csv("2022echo.csv", parse_dates=["Cosmos受付日時"])


# df_2022["Date"] = pd.to_datetime(df_2022.iloc[:, 9])
df_2022["Month"] = df_2022["Cosmos受付日時"].dt.strftime("%Y%m")

# left_column, right_column = st.columns(2)
nyuugai_pivot = pd.pivot_table(df_2022, index="入外区分", columns="Month", values="患者コード", aggfunc="count")
# left_column = st.dataframe(df_nyuugai)
# right_column = st.bar_chart(df_nyuugai)
st.dataframe(nyuugai_pivot)



#検査室分類
for i in range(len(df_2022)):
    if "分院" in df_2022.iloc[i, df_2022.columns.get_loc("号機")]:
        df_2022.iloc[i, df_2022.columns.get_loc("号機")] = "分院エコー室"
    elif "技師室裏" == df_2022.iloc[i, df_2022.columns.get_loc("号機")]:
        df_2022.iloc[i, df_2022.columns.get_loc("号機")] = "技師室裏"
    else:
        df_2022.iloc[i, df_2022.columns.get_loc("号機")] = "本院エコー室"

st.write(df_2022["号機"].unique())

df_room = df_2022.groupby(["Month", "入外区分", "号機"])["患者コード"].count()
st.dataframe(df_room, width=600)
