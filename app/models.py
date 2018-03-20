from app import db
class Member(db.Model):
	
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(50))
	age=db.Column(db.Integer)
	posts=db.relationship("Post",backref="members")

	def __str__(self):
		return "id: "+str(self.id) +"\nname:" +self.name+"\n"+30*"="
	
	def __cmp__(self,other):
		return cmp(len(other.posts),len(self.posts))
		

	def as_dict(self):
		return{
			"id":self.id,
			"name":self.name,
			"age":self.age,
			"posts":self.posts,
		}

class Post(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(800))
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"))

    def __str__(self):
        return "Title: {self.title}, Content: {self.content}"

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "member_id": self.member_id,
        }
