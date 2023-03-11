from flask import Flask, render_template, request
from stories import stories_lib

story = ""

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html', stories = stories_lib)

@app.route('/form/<storytitle>')
def form_page(storytitle):
    global story
    story = [story for story in stories_lib if story.title == storytitle][0]
    return render_template('madlib-form.html', story=story)

@app.route('/<storytitle>')
def story_page(storytitle):
    story_text = story.generate(request.args)
    return render_template('story.html', title = story.title, text = story_text)

