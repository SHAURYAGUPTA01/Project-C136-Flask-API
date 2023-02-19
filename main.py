from flask import Flask,jsonify,request
import data

obj = Flask(__name__)

@obj.route("/")
def add_data():
    return jsonify({"data": data,"message" : "success"}),200

@obj.route("/star")
def star():
    name = request.args.get("name")
    sdata = next(item for item in data if item["name"] == name )

    return jsonify({"data": sdata,"message" : "success"}),200

if __name__ == "__main__":
    obj.run(debug = True)
