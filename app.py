from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bookmark.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Bookmark('{self.domain}')"

headers = {
  "x-api-key": "YOUR KEY"
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        domain = request.form["domain"]
        bookmark = Bookmark(domain=domain)
        db.session.add(bookmark)
        db.session.commit()
    
    bookmarks = Bookmark.query.all()
    bookmark_domains = [bookmark.domain for bookmark in bookmarks]

    data = []
    for domain in bookmark_domains:
        url = f"https://api.criminalip.io/v1/domain/reports?query={domain}"
        response = requests.get(url, headers=headers)
        report = response.json()["data"]["reports"][0]
        connected_ip_cnt = report["connected_ip_cnt"]
        countries = report["countries"]
        issues = report["issues"]
        reg_dtime = report["reg_dtime"]
        scan_id = report["scan_id"]
        score = report["score"]
        technologies = report["technologies"]
        title = report["title"]
        url = report["url"]
        data.append({
            "title": title,
            "url": url,
            "score": score,
            "reg_dtime": reg_dtime,
            "scan_id": scan_id,
            "connected_ip_cnt": connected_ip_cnt,
            "technologies": technologies,
            "countries": countries,
            "issues": issues
        })

    return render_template("home.html", data=data)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
