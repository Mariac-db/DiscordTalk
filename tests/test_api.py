from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

# test prediction with value of 0 
def test_null_prediction():

    response = client.post("/v1/prediction", json = {
                                            "opening_gross": 0,
                                            "screens": 0,
                                            "production_budget": 0,
                                            "title_year": 0,
                                            "aspect_ratio": 0,
                                            "duration": 0,
                                            "cast_total_facebook_likes": 0,
                                            "budget": 0,
                                            "imdb_score": 0
                                            } )
    assert response.status_code == 200
    assert response.json()["worldwide_gross"] == 0

    


# predictions with values != 0 
def test_random_prediction(): 

    response = client.post("/v1/prediction", json = 
                                    {"opening_gross": 27520040.0, 
                                    "screens": 3401.0, 
                                    "production_budget": 130000000,
                                    "title_year": 2013.0, 
                                    "aspect_ratio": 2.35, 
                                    "duration": 100.0, 
                                    "cast_total_facebook_likes": 14168, 
                                    "budget": 130000000.0, 
                                    "imdb_score": 4.9})
    
    assert response.status_code == 200
    assert response.json()["worldwide_gross"] != 0
    


