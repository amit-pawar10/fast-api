from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return "Hello World!"


@app.get('/property')
def property():
    return "This is property page!"


@app.get('/movies')
def movies():
    return {"movie_list":{"movie_1", "movie_2"}}


############### This is static path - Place static paths first
@app.get('/profile/admin')
def admin():
    return {"This is admin page"}

############# Dynamic path 
@app.get('/profile/{username}')
def profile(username: str):
    return {f"This is profile page for {username}"}

########## PATH PARAMETR ---> id here is a path parameter
@app.get('/property/{id}')
def property(id: int):
    return f"This is property page for proprty {id}!"


############ QUERY PARAMETER ---> http://127.0.0.1:8000/products?id=10&price=200
@app.get('/products')
def product(id:int=10, price:int=0):
    return {f"Product with id : {id} and it's price is {price}"}


######## COMBINATION OF QUERY & PATH PARAMETR
@app.get('/profile/{user_id}/comments')
def profile(user_id: int, commentid:int):
    return {f"Profile page for user with user id {user_id} and comment with {commentid}"}