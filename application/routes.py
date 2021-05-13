from flask.globals import session
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


@app.route("/add_team", methods=["GET", "POST"])
def add_team():
    form = TeamForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_team = Team(name = form.name.data, league = form.league.data)
            db.session.add(new_team)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add.html", title="Create your team", form=form)


@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    form= TeamForm()
    team= Team.query.filter_by(id=id).first()
    if request.method == "POST":
        team.name = form.name.data
        team.league = form.league.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update.html", title="Update your team", form=form)

@app.route("/delete/<int:id>", methods=["GET","POST"])
def delete(id):
    delete_team= session.query.filter_by(id=id).first()
    db.session.delete(delete_team)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/player/<int:id>",methods=["GET", "POST"])
def player(id):
    form= PlayersForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_player = Players(player_name = form.name.data, player_nationality = form.nationality.data, player_position = form.position.data, teamid=id)
            db.session.add(new_player)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add-Player.html", title = "Select Players to Add to Your Team", form=form)
       
    








    








   
