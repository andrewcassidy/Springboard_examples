import pandas as pd
data = pd.read_excel("./data/Healthy Minds 2015-2016 Survey Data.xlsx")
race_columns = ["race_white", "race_black", "race_asian", "race_ainaan", "race_mides", "race_pi", "race_haw", "race_other"]
fill_to_zero = dict(zip(race_columns, [0.0]*len(race_columns)))
data.loc[:,race_columns] = data.loc[:,race_columns].fillna(fill_to_zero) # Could just do fillna(0)

age_by_race = data.loc[:,race_columns + ["age"]].dropna() ## Drop anyone who didn't report their age
# Tall meaning tall data aka a biracial person appears twice
tall_age_by_race = pd.melt(age_by_race, id_vars="age")
tall_age_by_race = tall_age_by_race[tall_age_by_race["value"] == 1.0]
del tall_age_by_race["value"]
tall_age_by_race.columns = ["age", "race"]

# What is the average age of each race?
tall_age_by_race.groupby("race").mean()


### Let's make a biracial column
reported_num_of_races = data.loc[:,race_columns].sum(axis=1) # Sum across rows
# 1181 people did not report their race at all
reported_num_of_races.value_counts()

race = pd.Series(index=data.index)
race[reported_num_of_races == 0.0] = "Unknown"
race[reported_num_of_races > 1.0] = "Biracial"
single_race = reported_num_of_races == 1.0
x = data.loc[single_race, race_columns]
def getColumnIndex(row):
    return list(filter(lambda tup: tup[1] == 1.0, enumerate(row)))[0][0]
race[single_race] = x.columns[x.apply(getColumnIndex, axis=1)].tolist()










