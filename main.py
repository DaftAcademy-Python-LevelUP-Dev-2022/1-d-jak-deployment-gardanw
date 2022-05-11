from fastapi import FastAPI, status, HTTPException

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


days = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}


@app.get("/day")
def get_day(name: str = "", number: int = 0):
    if name in days and days[name] == number:
        return status.HTTP_200_OK
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


class HerokuApp:
    app_url = "https://z1-d-jak-deployment-gardanw.herokuapp.com/"  # Fill your heroku app url here
