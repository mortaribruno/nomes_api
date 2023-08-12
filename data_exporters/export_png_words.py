from wordcloud import WordCloud
import matplotlib.pyplot as plt
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here
    result = data.groupby('nome')['frequencia'].sum()
    wordcloud_data = result.to_dict()
    wordcloud = WordCloud(width=800, height=400, background_color='black').generate_from_frequencies(wordcloud_data)
    wordcloud.to_file('words.png')

