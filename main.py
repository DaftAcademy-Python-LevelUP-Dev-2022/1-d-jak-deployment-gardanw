from fastapi import FastAPI, status, HTTPException, Request
import datetime

from pydantic import BaseModel

app = FastAPI()
events_list = []


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


class GiveEventDataRq(BaseModel):
    date: str
    event: str


class GiveEventDataResp(BaseModel):
    id: int
    date: str
    event: str
    date_added: str


@app.put("/events", response_model=GiveEventDataResp)
def put_events(request: GiveEventDataRq):
    rq = request.dict()
    id = len(events_list)
    date = rq.get("date", None)
    try:
        datetime.date.fromisoformat(date)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
    event = rq.get("event", None)
    date_added = datetime.date.today()
    response = GiveEventDataResp(id=id, date=date, event=event, date_added=str(date_added))
    events_list.append(response)
    return response


class HerokuApp:
    app_url = "https://z1-d-jak-deployment-gardanw.herokuapp.com/"  # Fill your heroku app url here
