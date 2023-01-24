from flask import Flask, render_template, request
import config
import os
import openai


## Creating the 404 page (optional)
def page_not_found(e):
  return render_template('404.html'), 404

## Initialise FLASK
app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


### Initialise the OPENAI library with the key saved in the CONFIG file
openai.api_key = app.config["OPENAI_API_KEY"]


##---------------------START FUNCTIONs------------
def createImagePrompt(prompt):
  response = openai.Image.create(prompt=prompt, n=2, size="1024x1024")
  return response['data']
##---------------------END FUNCTIONs--------------


##View functions
@app.route('/', methods=["GET", "POST"])
def index():
  if request.method == 'POST':
    images = []
    prompt = request.form['prompt']
    res = createImagePrompt(prompt)

    if len(res) > 0:
      for img in res:
        images.append(img['url'])

  return render_template('index.html', **locals())


#Run Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
