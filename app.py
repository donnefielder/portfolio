from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/blender-projects")
def blender_projects():
    return render_template("blender_projects.html")

@app.route("/after-effects")
def after_effects():
    return render_template("after_effects_projects.html")   

@app.route("/illustrator")
def illustrator():
    return render_template("illustrator_projects.html")

@app.route("/photoshop")
def photoshop():
    return render_template("photoshop_projects.html")

@app.route("/internship")
def internship():
    return render_template("internship_projects.html")

@app.route("/school")
def school():
    return render_template("school_projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
