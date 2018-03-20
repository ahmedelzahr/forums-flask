import datetime
class Member():
	"""docstring for ClassName"""
	def __init__(self, name,age):
		self.name = name
		self.age=age
		self.id=0
		self.posts=[]

	def __cmp__(self,other):
		return cmp(len(other.posts),len(self.posts))
		

	def __str__(self):
		return "id: "+str(self.id) +"\nname:" +self.name+"\n"+30*"="

	def __dict__(self):
		return{
			"id":self.id,
			"name":self.name,
			"age":self.age,
			"posts":self.posts,
		}

class Post():
	def __init__(self, title,subject,member_id=0):
		self.title = title
		self.subject=subject
		self.id=0
		self.member_id=member_id
		self.date = datetime.datetime.now()

	def __str__(self):
		return "Title: "+self.title +"\n" +self.subject+"\n"+str(self.date)+"\n"+30*"="

	def __dict__(self):
		return{
			"id":self.id,
			"title":self.title,
			"subject":self.subject,
			"member_id":self.member_id,
		}
		
