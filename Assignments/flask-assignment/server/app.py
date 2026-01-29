from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
from config import get_db
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

db = get_db()
collection = db["users"]

# ---------------- API ROUTE ----------------
@app.route("/api", methods=["GET"])
def api():
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
        print(data)
    return jsonify(data)
    

# ---------------- FORM ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def form():
    error = None

    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]

            collection.insert_one({
                "name": name,
                "email": email
            })

            return redirect(url_for("success"))

        except Exception as e:
            error = str(e)

    return render_template("form.html", error=error)



# ---------------- SUCCESS ROUTE ----------------
@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/users")
def users():
    users_list = list(collection.find({}, {"_id": 0}))
    return render_template("render.html", users=users_list)


@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.form or request.json
    itemName = data.get('itemName')
    itemDescription = data.get('itemDescription')

    if not itemName or not itemDescription:
        return jsonify({"error": "Missing fields"}), 400

    collection.insert_one({
        "itemName": itemName,
        "itemDescription": itemDescription
    })

    return jsonify({"message": "Item saved"}), 201

if __name__ == "__main__":
    app.run(debug=True)
