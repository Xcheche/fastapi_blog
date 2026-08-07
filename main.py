from fastapi import FastAPI, Request, HTTPException, status #noqa
from fastapi.exceptions import RequestValidationError 
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException  
#from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from exception_handlers import register_exception_handlers
from schemas import PostCreate, PostResponse


app = FastAPI()
# Calling the exception handler rom exception_handlers.py
register_exception_handlers(app) # <-- this activates your handlers


# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Set up Jinja2 templates
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



# Home page (non-API, monolithic style)
@app.get("/", include_in_schema=False)
async def home(request: Request):
    """ Render the home page with posts. """
    title="Home Page"
    # Get by filter based on date created, descending order
    sorted_posts = sorted(posts, key=lambda x: x["date_posted"], reverse=True)
    context={
        "request": request,
        "posts": sorted_posts,
        "title": title
    }
    return templates.TemplateResponse(request,"blog/home.html",context)

# Single post page (non-API, monolithic style)
@app.get("/posts/{post_id}", include_in_schema=False)
async def post_detail(request: Request, post_id: int):
    """ Render a single post detail page. """
    title="Post Detail"
    post = None
    for p in posts:
        if p.get("id") == post_id:
            post = p
            break
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {post_id} not found")
    context={
        "request": request,
        "post": post,
        "title": title
    }
    return templates.TemplateResponse(request,"blog/post_detail.html",context)  


#------------------------------------------------------Api Endpoints-----------------------------------------------------
# Get all posts
@app.get("/api/posts/", response_model=list[PostResponse])
async def get_posts():
    """ Return all posts as JSON. """
     # Get by filter based on date created, descending order
    sorted_posts = sorted(posts, key=lambda x: x["date_posted"], reverse=True)
    return sorted_posts


# Create a new post

@app.post(
    "/api/posts",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_post(post: PostCreate):
    new_id = max(p["id"] for p in posts) + 1 if posts else 1
    new_post = {
        "id": new_id,
        "author": post.author,
        "title": post.title,
        "content": post.content,
        "date_posted": "April 23, 2025",
    }
    posts.append(new_post)
    return new_post



# Get a single post by ID
@app.get("/api/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int):
    """
    Return a single post by ID.
    Raise 404 if not found.
    """
   
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with id {post_id} not found")