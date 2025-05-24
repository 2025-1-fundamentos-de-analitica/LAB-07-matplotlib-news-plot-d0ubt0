"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    df = pd.read_csv('files/input/news.csv', index_col= 0)

    colors = {'Television': '#5a5', 'Newspaper': '#7d7', 'Internet': '#f88', 'Radio': '#9d9'}
    z = {'Television': 1, 'Newspaper': 1, 'Internet': 2, 'Radio': 1}
    line_width = {'Television': 2, 'Newspaper': 2, 'Internet': 4, 'Radio': 2}

    for columna in df.columns:
        plt.plot(df[columna], label = columna,  color = colors[columna], zorder = z[columna], linewidth = line_width[columna])

    plt.title('Uso de los medios de comunicacion', fontsize = 16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    #plt.legend(loc= 'upper right')
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        first_year = df.index[0]

        plt.scatter(x = first_year, y = df[col][first_year], color = colors[col], zorder = z[col])

        last_year = df.index[-1]

        plt.scatter(x = last_year, y = df[col][last_year],  color = colors[col], zorder = z[col])
        
        plt.text(first_year - 0.2, df[col][first_year], col + " " + str(df[col][first_year]) + '%', ha= 'right', va = 'center', color = colors[col])
        plt.text(last_year + 0.2, df[col][last_year], str(df[col][last_year]) + '%', ha= 'left', va = 'center', color = colors[col])


    if not os.path.exists('files/plots'):
        os.mkdir('files/plots')

    plt.tight_layout()
    plt.savefig('files/plots/news.png')

pregunta_01()