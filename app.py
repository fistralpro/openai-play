import os
import logging
import openai
import json
from io import BytesIO

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
IMAGES_DIR = os.path.join( "images")
GENERATED_DIR = os.path.join( "generated")

@app.get("/")
def index():
    app.logger.info(os.getenv("OPENAI_API_KEY"))
    if (os.getenv("OPENAI_API_KEY")==""):
        app.logger.info("key not set")
        return render_template("setup_key.html")
    text_result = request.args.get("text_result")
    image_result = request.args.get("image_result")
    if image_result is None:
        image = os.path.join(IMAGES_DIR, "blank.png")
    else:
        image = os.path.join(GENERATED_DIR, image_result)
    return render_template("index.html", text_result = text_result, image_result = image)

@app.post("/response/text")
def response_text():
    text_input = request.form["text_input"]
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text_input,
        temperature=0.6,
        max_tokens=2048
    )
    app.logger.info("----OPENAI Response---")
    app.logger.info(response.choices[0].text)

    return redirect(url_for("index", text_result=response.choices[0].text))

@app.post("/response/image")
def response_image():
    image="not_blank.png"
    image_input = request.form["image_input"]
    response = openai.Image.create(
      prompt=image_input,
      n=1,
      size="1024x1024"
      #response_format="b64_json",
    )
    image_url = response['data'][0]['url']
    return redirect(image_url)
    #return redirect(url_for("index", image_result=image))
