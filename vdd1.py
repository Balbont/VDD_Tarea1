import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import math
import plotly.graph_objects as go


#CIUDADES
parametros = ['Costo de vida', 'Arriendo', 'Alimentos', 'Costo de Vida (con arriendo)', 'Restaurantes']
liverpool = [61.78, 22.06, 47.44, 42.14, 73.02]
amsterdam = [70.31, 44.44, 54.06, 57.52, 79.21]
seul = [72.88 ,29.27 ,90.38 ,51.32 ,44.19]
n = len(parametros)
angulos = [i/n * 2 * np.pi for i in range(n)]

liverpool += liverpool[:1]
amsterdam += amsterdam[:1]
seul += seul[:1]
angulos += angulos[:1]

fig, ax = plt.subplots(nrows=1, ncols=1, figsize =(8,8), subplot_kw=dict(polar=True))

plt.xticks(angulos[:-1],parametros, color='grey', size=12)

ax.plot(angulos, liverpool, linewidth=1, linestyle='solid')
ax.fill(angulos, liverpool, 'skyblue', alpha=0.2)

ax.plot(angulos, amsterdam, linewidth=1, linestyle='solid')
ax.fill(angulos, amsterdam, 'orange', alpha=0.2)

ax.plot(angulos, seul, linewidth=1, linestyle='solid')
ax.fill(angulos, seul, 'green', alpha=0.2)

plt.legend(labels=('Liverpool','Amsterdam','Seul'), loc=1)
plt.show()


#ACTORES
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=70,
        thickness=20,
        line=dict(color="black", width=0.8),
        label=["Keanu Reeves 19", "Ewan McGregor 21", "Johnny Depp 20", "Sport", "Drama", "Romace", "Action", "Crime",
               "Sci-Fi", "Family",
               "Documentary", "Music", "Western", "Comedy", "Thriller", "Adventure", "Fantasy", "Biography", "Mystery",
               "Animation",
               "History", "Horror", "War", "Music"]
    ),
    link=dict(
        source=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],

        target=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
                ],
        value=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
               ]
    ))])
fig.show()
