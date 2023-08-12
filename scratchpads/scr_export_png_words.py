"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""
from mage_ai.data_preparation.variable_manager import get_variable
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = get_variable('damp_flower', 'load_api_nomes', 'output_0')

result = df.groupby('nome')['frequencia'].sum()
wordcloud_data = result.to_dict()
wordcloud = WordCloud(width=800, height=400, background_color='black').generate_from_frequencies(wordcloud_data)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
