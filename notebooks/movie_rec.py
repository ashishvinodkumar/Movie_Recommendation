from google.cloud import bigquery
client = bigquery.Client()
import pandas as pd
import click


def get_imdb_title_id_from_title(title):
    query = """
        SELECT *
        FROM `cosmic-sensor-287820.movie_recommendation.combined_metadata`
        where title = '"""+title+"""'
        LIMIT 20;
    """        
        
    df = (
        client.query(query)
        .result()
        .to_dataframe()
    )
    
    return df['imdb_title_id'][0]


@click.command()
@click.option('--title')
def main(title):
    imdb_title_id = get_imdb_title_id_from_title(title)
    print('The imdb title id for the movie "'+title+'" is: '+ imdb_title_id)
    

    
if __name__ == "__main__":
    main()
