from application import app, db
from application.models import Players, Team
from application.forms import TeamForm, PlayersForm
from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    all_teams = Team.query.all()
    all_players = Players.query.all()
    output=""
    return render_template("home.html", title="Home", all_teams = all_teams, all_players = all_players)


@app.route('/add_team', methods=["GET", "POST"])
def add_team():
    form = TeamForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_team = Team(name = form.name.data, league = form.league.data)
            db.session.add(new_team)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("add.html", title="Create a team", form=form)


@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    form= TeamForm()
    team= Team.query.filter_by(id=id).first()







   

