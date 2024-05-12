import os
import random

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    image_files = [
        filename
        for filename in os.listdir("static/images")
        if filename.split(".")[-1].lower() in ["jpg", "jpeg", "png", "webp"]
    ]

    random_images = random.sample(image_files, 1)
    random_image_urls = [
        url_for("static", filename=f"images/{image}") for image in random_images
    ]
    return render_template("index.html", random_image_urls=random_image_urls)
