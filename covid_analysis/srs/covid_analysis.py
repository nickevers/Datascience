import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas

plots = ['new_cases', 'total_cases', 'new_deaths', 'total_deaths']
covid_data = pandas.read_csv("../../resources/owid-covid-data.csv", index_col=2)
countries = covid_data.index.unique()
selected_countries = []

print("Welcome to the Covid-19 analysis of the world.")
print("Select a country using its ISO_Code or name.")
print("U are able to select more countries with a comma(,).")
print("When u leave this empty. All countries will be selected.")
val = input("select ur countries:")
val = val.strip()
if val == '':
    selected_countries = countries
    print('All countries selected.')
else:
    val = val.split(',')
    val = [word.strip() for word in val]
    for country in val:
        if country == '':
            continue
        elif len(country) == 3:
            if country.upper() in covid_data.iso_code.unique():
                selected_countries.append(covid_data.loc[covid_data['iso_code'] == country.upper()].index[0])
            else:
                print(f"{country} is not a valid ISO_Code.")
        else:
            amount = len(selected_countries)
            for cntry in countries:
                if cntry.upper() == country.upper():
                    selected_countries.append(cntry)
            if amount == len(selected_countries):
                print(f"{country} is not a valid country name.")
    print("selected countries:")
    print(selected_countries)


with PdfPages('covid_data_of_the_world.pdf') as pdf:
    for country in selected_countries:
        if country is np.nan:
            break
        for plot in plots:
            country_data = covid_data.loc[country][['date', plot]]
            country_data.date = pandas.to_datetime(country_data['date'], format='%Y-%m-%d')
            country_data.set_index(['date'], inplace=True)
            country_data.plot()
            plt.title(f"{plot} in {country}")
            pdf.savefig()
            plt.close()
print("done")





