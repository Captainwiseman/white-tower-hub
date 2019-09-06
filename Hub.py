from flask import Flask, render_template

whiteTowerHubBrain = Flask(__name__)

@whiteTowerHubBrain.route("/")
def main():
    print("White~Tower~Hub is Online and Functional")
    return render_template('index.html')

if __name__ == "__main__":
    whiteTowerHubBrain.run(debug=True, host="0.0.0.0", port=80)