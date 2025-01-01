from flask import Flask, render_template, request, redirect, url_for, flash, session
import random

app = Flask(__name__)

# Set a secret key for session management (required for flash messages)
app.secret_key = 'OONGA BOONGA'  # You can use a random string here

# Predefined list of phrase pairs
phrase_pairs = [
    ("bipartite logistic system", "empty Turing machines"),
    ("infinite recursion", "bounded solution space"),
    ("quantum foam duality", "hyperspace anomaly"),
    ("principle of maximal ambiguity", "fractal dimension paradox"),
    ("topological manifold", "non-trivial solution"),
]

@app.route("/")
def home():
    # Generate a random proof
    pair = random.choice(phrase_pairs)
    return render_template("index.html", phrase1=pair[0], phrase2=pair[1])

@app.route("/developer", methods=["GET", "POST"])
def developer_mode():
    if request.method == "POST":
        # Handle adding new phrase pairs
        phrase1 = request.form.get("phrase1", "").strip()
        phrase2 = request.form.get("phrase2", "").strip()

        if phrase1 and phrase2:
            phrase_pairs.append((phrase1, phrase2))
            flash("Phrase pair added successfully!", "success")
        else:
            flash("Both phrases must be non-empty.", "danger")

        return redirect(url_for("developer_mode"))

    return render_template("developer_mode.html", phrases=phrase_pairs)

@app.route("/delete_pair/<int:index>")
def delete_pair(index):
    # Remove the phrase pair at the given index
    if 0 <= index < len(phrase_pairs):
        phrase_pairs.pop(index)
        flash("Phrase pair deleted successfully!", "success")
    else:
        flash("Invalid index.", "danger")
    return redirect(url_for("developer_mode"))

@app.route("/edit_pair/<int:index>", methods=["GET", "POST"])
def edit_pair(index):
    if request.method == "POST":
        # Edit the phrase pair at the given index
        phrase1 = request.form.get("phrase1", "").strip()
        phrase2 = request.form.get("phrase2", "").strip()

        if phrase1 and phrase2:
            phrase_pairs[index] = (phrase1, phrase2)
            flash("Phrase pair edited successfully!", "success")
            return redirect(url_for("developer_mode"))
        else:
            flash("Both phrases must be non-empty.", "danger")

    if 0 <= index < len(phrase_pairs):
        return render_template("edit_pair.html", pair=phrase_pairs[index], index=index)
    else:
        flash("Invalid index.", "danger")
        return redirect(url_for("developer_mode"))

if __name__ == "__main__":
    app.run(debug=True)
