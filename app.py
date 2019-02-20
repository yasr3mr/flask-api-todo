from flask_api import FlaskAPI
from flask import request
from db.DB import *
#init app
app=FlaskAPI(__name__)
#_______________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________


@app.route('/create/<string:name>/<string:description>',methods=["GET",'POST'])
def create(name,description):
	flag=create_task(name,description)
	if flag:
		return "saved"
	else:
		return 'not saved'
#_______________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________

@app.route('/tasks',methods=['GET'])
def get():
	if request.method == 'GET':
		data=get_all_task()
		return {"data":data}
#_______________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________

@app.route('/tasks/<int:id>',methods=['GET'])
def get_one(id):
	data=get_one_task(id)
	return {'data':data}
#_______________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________

@app.route('/update/<int:id>/<string:name>/<string:description>',methods=["GET",'PUT'])
def update(id,name,description):
	flag=update_task(id,name,description)
	if flag:
		return "Updated"
	else:
		return 'not Updated'
#_______________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________

@app.route('/delete/<id>',methods=['GET', 'DELETE'])
def delete(id):
	flag=delete_task(id)
	if flag:
		return "Deleted"
	else:
		return 'not Deleted'
#_______________________________________________________________________________________________________________
#_________________________________________________________________________________________________

@app.errorhandler(404)
def bar(error):
	return "Not found"

#_______________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________

#run app
if __name__=="__main__":

	app.run(debug=True)