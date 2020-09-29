import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas

plots = ['new_cases', 'total_cases', 'new_deaths', 'total_deaths']
covid_data = pandas.read_csv("../../resources/owid-covid-data.csv", index_col=2)
countries = covid_data.index.unique()


with PdfPages('covid_data_of_the_world.pdf') as pdf:
    for country in countries:
        if country is np.nan:
            break
        print(country)
        for plot in plots:
            country_data = covid_data.loc[country][['date', plot]]
            country_data.date = pandas.to_datetime(country_data['date'], format='%Y-%m-%d')
            country_data.set_index(['date'], inplace=True)
            country_data.plot()
            plt.title(f"{plot} in {country}")
            pdf.savefig()
            plt.close()





