import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import emoji

df = pd.read_csv('All_Pokemon.csv')

colors = {'Fire':'red', 'Water':'royalblue', 'Grass':'green','Poison':'darkviolet',
          'Steel':'grey','Bug':'palegreen','Normal':'silver','Dark':'k',
          'Electric':'yellow','Ground':'sandybrown','Rock':'saddlebrown',
          'Ice':'aqua','Fairy':'fuchsia','Fighting':'lightsalmon','Psychic':'pink',
          'Ghost':'darkslateblue','Dragon':'mediumslateblue','Flying':'paleturquoise'}

sns.set_style('whitegrid')
fig, ax = plt.subplots(figsize = (10,10))
sns.histplot(data = df,
             x = 'Mean')
ax.set_title('Histograma de la media de las estadísticas base',
             fontsize = 15, fontweight = 'bold')
ax.set_xlabel('Media')
ax.set_ylabel('Cantidad')
ax.set_xlim(20,150)
ax.set_xticks(np.arange(20,151,10))
plt.savefig('histograma_pec2.png')
plt.close()

sns.set_style('whitegrid')
fig, ax = plt.subplots(figsize = (10,10))
sns.swarmplot(data = df.sort_values('Type 1', ascending = False), 
              x = 'Mean',
              y = 'Type 1',
              hue = 'Type 1',
              palette=colors,
              legend=False,
              s = 4)
ax.set_title('Swarmplot de la media de las estadísticas en función del tipo primario',
             fontsize = 15, fontweight = 'bold')
ax.set_xlabel('Media')
ax.set_ylabel('Tipo Primario')
ax.set_xlim(20,150)
ax.set_xticks(np.arange(20,151,10))
plt.savefig('swarmplot_pec2.png')
plt.close()

type_count = pd.DataFrame(df['Type 1'].value_counts()).reset_index()
pokemon_types = list(sorted(df['Type 1'].unique()))

type_symbols = {
    'Grass': '☘️',     
    'Electric': '⚡',
    'Poison':'🐍',
    'Steel':'🛡️',
    'Normal':'⬜',
    'Ground':'⛰️',
    'Ghost':'👻',
    'Psychic':'🔮',
    'Fighting':'🏋️',
    'Dark':'🕶️',
    'Bug':'🐛',
    'Ice':'❄️',
    'Dragon':'🐉',
    'Flying':'🦅',
    'Water':'💧',
    'Fire':'🔥',
    'Rock':'🗿',
    'Fairy':'🧚'
    
}
type_symbols = dict(sorted(type_symbols.items()))



import matplotlib.font_manager  
plt.rcParams['font.family'] = [f.name for f in matplotlib.font_manager.fontManager.ttflist]

# sns.set_style('whitegrid')
fig, ax = plt.subplots(figsize = (10,10))
yticks = []
for i, type_name in enumerate(pokemon_types):
    if type_name in type_symbols:
        count = type_count[type_count['Type 1']==type_name]['count'].iloc[0]
        color = colors[type_name]
        symbol = type_symbols[type_name]
        
        num_symbols = count // 5
        yticks.append(2*i+2)
        for j in range(num_symbols):
            plt.text(1.5*j+1, 2*i+2, symbol, 
                     fontsize=20, ha='center', 
                     va='center', color=color)
            
            
ax.set_yticks(yticks, [key for key in type_symbols])
ax.set_xticks([])
ax.set_ylabel('Tipo Primario')
ax.grid(False)
ax.set_xlim(0,40)
ax.set_ylim(0,38)
ax.set_title('Grafico Isotype de la cantidad de Pokemon por tipo primario')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
plt.savefig('isotypechart_pec2.png')
plt.close()

