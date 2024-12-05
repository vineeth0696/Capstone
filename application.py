from flask import Flask, render_template, redirect, url_for, request
import datetime
import socket

application = Flask(__name__)
application.secret_key = "abc"  
dict={}
#This is the change
def get_host_address():
    hostName = socket.gethostname()
    return socket.gethostbyname(hostName)
# This line has been added in new braanch
def file_to_list(filename):
	file = open(filename,'r')
	list =  file.readlines()
	for elem in list:
		elem.rstrip()
	file.close()
	return list

def search_sort(btype1):
	file = "doc_details"
	file1 = file + ".txt"
	fp = open(file1 , 'r')
	l = fp.readlines()
	fp.close()


	l.sort()
	return l

@application.route("/")
def home():
	return render_template("home.html")
	
@application.route("/upload", methods=['GET', 'POST'])
def upload():
	message=None
	doc_details = open('doc_details.txt','a')
	doc_details_list = file_to_list("doc_details.txt")
	dateofupload = datetime.datetime.now()
	flag=1
	if request.method == 'POST':
		btype = request.form['btype']
		category = request.form['category']
		sex = request.form['sex']
		name = request.form['name']
		age = request.form['age']
		weight = request.form['weight']
		height = request.form['height']     
		mobile = request.form['mobile']
		address = request.form['address']		
		
		print ("Category "+category)
		print ("btype "+btype)
		print ("Doc Type"+sex)
		for line in doc_details_list:
			if btype in line and sex in line and name in line and weight in line and height in line:
				flag=0
				message = "The "+age+" is already uploaded. Please check! "+height
				break
		
		if btype != "Select btype" and sex != "Select Document type" and btype != "none" and sex != "none" and name != "" and age != "" and weight != "" and height != "" and mobile!= "" and flag == 1:
			filename1 = "doc_details.txt"
			doc_details1 = open(filename1,'a')
			doc_details1.write(btype+"::::"+sex+"::::"+name+"::::"+age+"::::"+weight+"::::"+height+"::::"+mobile+"::::"+str(dateofupload)+"::::"+address+"\n")
			document = sex
			file_name = category+"_doc_details.txt"
			document = open(file_name,'a')
			document.write(btype+"::::"+sex+"::::"+name+"::::"+age+"::::"+weight+"::::"+height+"::::"+mobile+"::::"+str(dateofupload)+"::::"+address+"\n")
			message = 'Document uploaded successfully!'
			document.close()
			print (document)
	
		elif btype == "Select btype" or sex == "Select Document type" or btype == "none" or sex == "none" or btype == "" or sex == "" or name == "" or age == "" or weight == "" or height == "" or mobile== "":
			message = 'Some values are empty. Please check!'
		doc_details1.close()
		print (doc_details1)
	
	return render_template("upload.html", message=message)

@application.route("/donor_list", methods=['GET','POST'])
def donor_list():
	doc_details_list = file_to_list("Donor_doc_details.txt")
	return render_template("donor_list.html", doc_details_list=doc_details_list)
	
@application.route("/receiver_list", methods=['GET','POST'])
def receiver_list():
	doc_details_list = file_to_list("Receiver_doc_details.txt")
	return render_template("receiver_list.html", doc_details_list=doc_details_list)
    
if __name__ == '__main__':
	application.run(host=get_host_address(),port="5006",debug="True")
