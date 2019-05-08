# Final Project (Threads)

![ScreenShot]

Threads is a single page dynamic Restful application that uses MERN stack which allows users to post, edit view and delete. The idea behind threads came about when i was working in the retail fashion world. Everyone who works in this sector is entitled to some form of discount. Threads is a platform that lets you access others in the same sector so discounts can be shared.

## Getting started


-install dependencies `yarn install`
-Start the server using `yarn start:server`
-Start the client using `yarn start:client`

## Brief

* ** Build a full stack application** by making your own backend and your own front-end
* **Use a Python Flask API** to serve your data from a Postgres database
* **Consume your API with a seperate front-end** built with React
* **Be a complete product** which most likely means multiple relationships and CRUD functionality for a couple of models.
* ** implement thoughtful user stories/wireframes** that are significant enough to help you know which features are core MVP and which you can cut out
* **Have a visually impressive design** to kick your portfolio up a notch and have something to wow future clients.
* **Be deployed online ** so its publicly accessible

## Technologies used

* **JavaScript (ES6)**
* **HTML 5**
* **React.js**
* **React Materialize**
* **Python**
* **JWT**
* **Bcrypt**
* **Git**
* **Github**
* **Heroku**
* **SCSS**
* **Chai**
* **Mocha**
* **Insomnia**

-
## Features

- Material Design.
- Commenting on posts in realtime.
- Ability to create an account securely.
- Post edit and delete your own posts.
-View your current posts on your profile page
-Share via social media


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## Development

Since this was going to be the first project i'd so on my own, I knew that time-management would be important. My back end features three many to many relationship tables and so writing out the model schema's was the first thing I planned out.

![ScreenShot](https://raw.github.com/{username}/{repository}/{branch}/{path} - show screenshot of back end code


For the register and log in page. I had to ensure that the user is fully authenticated and that the username and email have not been  used prior. From auth.py:
```
@api.route('/login', methods=['POST'])
def login():
data = request.get_json()
user = User.query.filter_by(email=data.get('email')).first()

if not user or not user.validate_password(data.get('password', '')):
return jsonify({'message': 'Unauthorized'}), 401

return jsonify({
'message': 'Welcome back {}!'.format(user.username),
'token': user.generate_token()
})

```

This piece of code, along with my secureRoute page, provides the user with a temporary token using Bycrpt. The methodology is as follows:

1) When a user registers we will hash their password with BCrypt before storing it in the database
2) When a user logs in we will validate the password they supply against the hashed password in the database.
3) If the password is valid, we will send a JSON web token.
4) The JWT can then be used to access certain routes that would otherwise be unavailable.

below is the secure route:

```def login_required(func):
@wraps(func)
def wrapper(*args, **kwargs):
if 'Authorization' not in request.headers:
return jsonify({'message': 'Unauthorized'}), 401

token = request.headers.get('Authorization').replace('Bearer ', '')

try:
payload = jwt.decode(token, secret)
except jwt.ExpiredSignatureError:
return jsonify({'message': 'Token Expired'})
except jwt.InvalidTokenError:
return jsonify({'message': 'invalid token'})

user = User.query.get(payload.get('sub'))

if not user:

return jsonify({'message': 'Unauthorized'}), 401

g.current_user = user

return func(*args, **kwargs)

return wrapper
```

## Wins and Blockers

The biggest blocker was underestimating the complexity of the joining table Schema's. To begin with, the plan was  to have a user, postItem, category and designer Schema with  many to many relationships as a user's post can have many designers and a designer category may have many users posts.

I overcame this by providing join tables that would form relationships between tables, similar to embedding them. the code below shows the relationship between my category  tables

```
designers_item_posts = db.Table('designers_ItemPosts',
db.Column('designer_id', db.Integer, db.ForeignKey('designers.id'),
primary_key=True),
db.Column('itemPost_id', db.Integer, db.ForeignKey('posts.id'),
primary_key=True)
)

categories_ItemPosts = db.Table('categories_ItemPosts',
db.Column('itemPost_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)

class ItemPost(db.Model, BaseModel):

__tablename__ = 'posts'

title = db.Column(db.String(2000), nullable=False)
description = db.Column(db.String(400), nullable=False)
size = db.Column(db.String(1000), nullable=False)
creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
image1 = db.Column(db.String(3000))
image2 = db.Column(db.String(3000))
image3 = db.Column(db.String(3000))
creator = db.relationship('User', backref='created_posts')
categories = db.relationship('Category', secondary=categories_ItemPosts, backref='categories')
designers = db.relationship('Designer', secondary=designers_item_posts, backref='designers')
liked_by = db.relationship('User', secondary=likes, backref='likes')
```

Personally, the biggest win was setting up the MERN stack and allowing basic functionality to the application. Initially i thought of several ways to pull in external api's like Twilio and Mapbox to either confirm a discount swap or view its location. However as time went on, and bug fixing started to become time consuming, i decided it was best to utilize remaining time on styling.

The theme and logo of Threads,  I designed myself using Photoshop and Illustrator. I felt it would be best practice to design something that would be purely my own that would mirror the passion that I have for design.

## Bugs

Below is a list of some of the known bugs within the app:

* Star liked ratings  are currently not functioning. I used react-star-ratings to implement the feature but didnt leave myself enough time to get it working.
* The login and register modals to not re-appear once clicking outside the box, closes it. A fix around this would  be to change the attributes of the  modal as so to make it static.

## Future Content

Along with any known bugs that need fixing, there are numerous other elements I will introduce in the future:

* Instant peer to peer messaging (as to allow privacy between users without disclosing discounts if they wish not to)
* Implement the liking feature and fix it up to my back end.
* Automatically expire old posts that fail to get much attention
* I toyed around with file stack while I was developing Threads, yet didnt fully get it working. I will implement this feature so users can upload local images.


