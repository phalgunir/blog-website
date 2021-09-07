from flask import Flask, render_template
import requests
from blog import Blog

app = Flask(__name__)
# fetch blogs from a json bin on https://www.npoint.io
json_bin_endpoint = 'https://api.npoint.io/ed99320662742443cc5b'
my_blogs = requests.get(json_bin_endpoint).json()
# create Blog objects for each blog in the json
blog_objects = [Blog(blog_id=blog['id'], title=blog['title'], subtitle=blog['subtitle'], body=blog['body']) for blog in my_blogs]


@app.route('/')
def home():
    # display all blogs
    return render_template("index.html", all_blogs=blog_objects)


@app.route('/post/<int:blog_id>')
def read_blog(blog_id):
    # fetch the Blog object for the requested blog id and pass it to blog.html to display that blog
    requested_blog_object = None
    for blog_object in blog_objects:
        if blog_object.id == blog_id:
            requested_blog_object = blog_object
    return render_template("blog.html", display_blog=requested_blog_object)


if __name__ == "__main__":
    app.run(debug=True)
