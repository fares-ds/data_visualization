import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data_2.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig_1, ax_1 = plt.subplots()
fig_2, ax_2 = plt.subplots()

ax_1.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')
ax_2.plot(ages, py_salaries, label='Python')
ax_2.plot(ages, js_salaries, label='JavaScript')


ax_1.legend()
ax_1.set_title('Median Salary (USD) by Age')
ax_1.set_xlabel('Ages')
ax_1.set_ylabel('Median Salary (USD)')

ax_2.legend()
ax_2.set_title('Median Salary (USD) by Age')
ax_2.set_xlabel('Ages')
ax_2.set_ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()

fig_1.savefig('matplotlib_p_10_subplots_fig_1.png')
fig_2.savefig('matplotlib_p_10_subplots_fig_2.png')
