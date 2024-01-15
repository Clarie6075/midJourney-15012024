from flask import Flask, request, render_template
import json, requests,time

# Creates an instance of the Flask class, which is the WSGI application.
app = Flask(__name__)

# Decorates the index function to be called when the root URL ("/") is accessed with either a GET or POST request
@app.route("/",methods = ["GET","POST"])

def index():  # handling requests to the root URL ("/").

    if request.method =="POST":
        q = request.form.get("q")
        print(q)
        body = json.dumps(
            {
            "version":"db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
            "input":{"prompt":q}
            }
        )
        headers = {
        "Authorization":"Token r8_XUGmgvzWW7SbIdjoWtmeSU3e4EKK8uE17C5SH",
        "Content-Type" : "application/json"
        }

        output = requests.post("https://api.replicate.com/v1/predictions",data=body,headers=headers)
        time.sleep(10)
        get_url = output.json()["urls"]["get"]
        get_result = requests.post(get_url,headers=headers).json()["output"]
        return(render_template("index.html",result=get_result[0]))
    else:

        return(render_template("index.html",result = "waiting for image request......"))

if __name__ =="__main__":
        app.run(host="127.0.0.1", port=8080)
