from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"start": "1970-01-01"}


@app.get("/method")
def get_method():
    return {"method": "GET"}


@app.post("/method", status_code=201)
def post_method():
    return {"method": "POST"}


@app.put("/method")
def put_method():
    return {"method": "PUT"}


@app.options("/method")
def options_method():
    return {"method": "OPTIONS"}


@app.delete("/method")
def delete_method():
    return {"method": "DELETE"}


class HerokuApp:
    app_url = "https://z1-d-jak-deployment-gardanw.herokuapp.com/"  # Fill your heroku app url here
