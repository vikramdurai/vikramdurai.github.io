from flask import Flask
from flask import render_template
from mistune import markdown

app = Flask(__name__)

class Post:
	def __init__(self, title, content):
		self.title = title
		self.content = content


@app.route("/")
def index():
	posts = []
	import os
	for i in os.listdir("posts/"):
		with open("posts/%s.md" % i[:-3], "r+") as f:
			posts.append(Post(title=i[:-3], content=markdown(f.read())))
	return render_template("index.html", posts=posts)


if __name__ == "__main__":
	app.run()