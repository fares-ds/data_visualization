import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data_1.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = [item[0] for item in language_counter.most_common(15)]
popularity = [item[1] for item in language_counter.most_common(15)]

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("Most Popular Languages")
# plt.ylabel("Programmig Languages")
plt.xlabel("Number of People Who use")

plt.tight_layout()
plt.savefig('matplotlib_p_2_bar_charts_and_analyzing_data_from_csv.png')
plt.show()
