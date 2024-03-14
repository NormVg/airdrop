from flask import Flask , jsonify , request,send_file
from tinydb import TinyDB, Query
import uuid , os, random

db = TinyDB('data.json')
app = Flask(__name__)

def fileswitch(name:str):
    if name in os.listdir("temp"):
        a,b = os.path.splitext(name)
        name =  a+str(random.randint(111,999))+b
    return name

@app.route("/list")
def index():
    g = db.all()
    return jsonify(g)

@app.post("/upload")
def upload():
    for i in request.files.getlist("file"):
        filename = fileswitch(i.filename)
        i.save("temp/"+filename)
        scm = {"id":uuid.uuid4().hex,"filename":filename}
        db.insert(scm)
 
    return "ramram"

@app.route("/download")
def download():
    dfile = Query()
    id = request.args.get("fileid")
    a = db.search(dfile.id == id)
    
    
    return send_file('temp/'+str(a[0]['filename']))

app.run("192.168.1.2", port=2345,debug=True)