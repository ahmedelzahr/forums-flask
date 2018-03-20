from app import models, db
from sqlalchemy import desc, func

class BaseStore():
  def __init__(self, data_provider):
        self.data_provider = data_provider

  def get_all(self):
    return self.data_provider.query.all()

  def add(self, item):
      # append member
        db.session.add(item)
        db.session.commit()
        return item

  def get_by_id(self, id):
      return self.data_provider.query.get(id)
    

  def delete(self, id):
     # delete item by id
    result = self.data_provider.query.filter_by(id = id).delete()
    db.session.commit()
    return result

  def update(self, item, fields):
        result = self.data_provider.query.filter_by(id = item.id).update(fields)
        db.session.commit()
        return result

  def entity_exists(self, item):
        result = True

        if self.get_by_id(item.id) is None:
            result = False

        return result
  

#---------------------------------------------------------------------------------------    

class MemberStore(BaseStore):


 
  def __init__(self):
        BaseStore.__init__(self,models.Member)

  #def __contains__(self, id):
    #return self.get_by_id(id)!=None
      
  def get_by_name(self, member_name):
        return self.data_provider.query.filter_by(name = member_name)     


  def update(self, item):
        fields = {"name": item.name, "age": item.age}
        return super().update(entity, fields)

  def get_members_with_posts(self):
        return self.data_provider.query.join(models.Member.posts)

  def get_top_two(self):
        return self.data_provider.query(func.count(models.Member.posts).label('total')).order_by('total DESC')

        

#-----------------------------------------------------------------------------------------------

class PostStore(BaseStore):


  def __init__(self):
        BaseStore.__init__(self,models.Post)
  def update(self, entity):
        fields = {"title": entity.title, "content": entity.content}
        return super().update(entity, fields)   

        




   
