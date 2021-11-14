from flask import request, redirect, render_template





db.drop_all()
db.create_all()



@app.route('/addband')
def addband():
    form = AddBand()
    return render_template("inputform.html",form=form)

@app.route('/editband',methods=['GET','POST'])
def editband():
    if request.method == 'POST':
        Band.name = form.name.data
        Band.genre = form.genre.data
        Band.year_formed = form.year_formed.data
        Band.most_recent_no1 = form.most_recent_no1
        Band.no_of_members = form.no_of_members.data
        Band.next_concert_venue = form.next_concert_venue.data
