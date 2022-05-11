from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"start": "1970-01-01"}


class HerokuApp:
    app_url = "https://z1-d-jak-deployment-gardanw.herokuapp.com/"  # Fill your heroku app url here
