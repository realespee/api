from flask import Flask, request, jsonify

app = Flask(__name__)

all_redflags = []

@app.route('/api/v1/redflags', methods=['POST'])
def create_red_flag():
    red_flag = request.json
    all_redflags.append(red_flag)
    return jsonify({"status" : 201, "data" : [{"id" : red_flag['id'], "message" : "Created red-flag record”"}]}), 201

@app.route('/api/v1/redflags', methods=['GET'])
def get_red_flag():
    return jsonify({"status" : 200, "data" : all_redflags})


if __name__ == "__main__":
    app.run(debug=True)