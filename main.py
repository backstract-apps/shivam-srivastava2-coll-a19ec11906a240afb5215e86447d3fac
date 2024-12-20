from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - shivam-srivastava2-coll-a19ec11906a240afb5215e86447d3fac',debug=False,docs_url='/distracted-colden-ee2f015abedb11ef97320242ac12000538/docs',openapi_url='/distracted-colden-ee2f015abedb11ef97320242ac12000538/openapi.json')

app.include_router(router, prefix='/distracted-colden-ee2f015abedb11ef97320242ac12000538/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()