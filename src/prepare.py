from dvc import api
import pandas as pd
from io import StringIO
import sys
import logging
from pandas.core.tools import numeric
 
logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)
logging.info('Fetching data...')


movie_data_path = api.read('dataset/movies.csv', remote='dataset-track')
finantial_data_path = api.read('dataset/finantials.csv', remote='dataset-track')
opening_data_path = api.read('dataset/opening_gross.csv', remote='dataset-track')

#descarga data de tal path 
fin_data = pd.read_csv(StringIO(finantial_data_path))
movie_data = pd.read_csv(StringIO(movie_data_path))
opening_data = pd.read_csv(StringIO(opening_data_path))

numeric_columns_mask = (movie_data.dtypes == float) | (movie_data.dtypes == int)
numeric_columns = [column for column in numeric_columns_mask.index if numeric_columns_mask[column]]
movie_data = movie_data[numeric_columns+['movie_title']]

fin_data = fin_data[['movie_title', 'production_budget', 'worldwide_gross']]
fin_movie_data = pd.merge(fin_data, movie_data, on='movie_title', how='left')
full_movie_data = pd.merge(opening_data, fin_movie_data, on='movie_title', how='left')
full_movie_data = full_movie_data.drop(['gross','movie_title'], axis=1)
full_movie_data.to_csv('dataset/full_data.csv',index=False) 

logger.info('Data Fetched and prepared...')