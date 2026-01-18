from fastapi import FastAPI, Request #noqa
#from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

#Some dummy post 

posts: list[dict] = [
    { "id": 1, "title": "First Post", "date_posted": "2024-06-01","author": "Author One", "content": "This is the content of the first post."},
    { "id": 2, "title": "Second Post", "date_posted": "2024-06-02", "author": "Author Two", "content": "This is the content of the second post."},
    { "id": 3, "title": "Third Post", "date_posted": "2024-06-03", "author": "Author Three", "content": "This is the content of the third post."},
    { "id": 4, "title": "Fourth Post", "date_posted": "2024-06-04", "author": "Author Four", "content": "This is the content of the fourth post."},
    { "id": 5, "title": "Fifth Post", "date_posted": "2024-06-05", "author": "Author Five", "content": "This is the content of the fifth post."},
    { "id": 6, "title": "Sixth Post", "date_posted": "2024-06-06", "author": "Author Six", "content": "This is the content of the sixth post."}
]

# @app.get("/", response_class=HTMLResponse, include_in_schema=False)
# @app.get("/posts/", response_class=HTMLResponse)
# async def read_root():
#     return f"<h1>{posts[0]['title']}</h1><p>{posts[0]['content']}</p>"
@app.get("/", include_in_schema=False)

async def home(request: Request):
    title="Home Page"
    context={
        "request": request,
        "posts": posts,
        "title": title
    }
    return templates.TemplateResponse(request,"blog/home.html",context)



@app.get("/api/posts/")
async def get_posts():
    return posts