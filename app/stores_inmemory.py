import itertools
class BaseStore():
  def __init__(self,data_provider, last_id):
    self.data_provider=data_provider
    self.last_id=last_id
  def get_all(self):
    return self.data_provider

  def add(self, item):
      # append member
        item.id=self.last_id
        self.data_provider.append(item)
        self.last_id +=1

  def entity_exists(self, item):
      # checks if an entity exists in a store
    return item in self.get_all()

  def get_by_id(self, id):
      # search for item by id
      result=None
      for item in self.get_all():
        if item.id==id:
          result=item
          break
      return result
      

  def delete(self, id):
     # delete item by id
    item=self.get_by_id(id) 
    self.data_provider.remove(item)

  def update(self, item):
     result = item
     all_items = self.get_all()

     for index, current_item in enumerate(all_items):
         if current_item.id == item.id:
             all_items[index] = item
             break

     return result
  

#---------------------------------------------------------------------------------------    

class MemberStore(BaseStore):


  members = []
  last_id=1
  def __init__(self):
        BaseStore.__init__(self,MemberStore.members, MemberStore.last_id)

  #def __contains__(self, id):
    #return self.get_by_id(id)!=None
      
  def get_by_name(self,name):
    for member in self.get_all():
      if member.name==name:
        yield member      


  def get_members_with_posts(self,all_post):
    all_members=self.get_all()
    for member, post in itertools.product(all_members, all_post):
      if member.id==post.member_id:
        member.posts.append(post)
          #self.update(member)  
    return self.get_all() 

  def  get_top_two(self,all_post):
    sorted_members=sorted(self.get_members_with_posts(all_post))
    return sorted_members[:2]

        

#-----------------------------------------------------------------------------------------------

class PostStore(BaseStore):

  posts = []
  last_id=1
  def __init__(self):
        BaseStore.__init__(self,PostStore.posts, PostStore.last_id)
  def get_posts_by_date(self):
    all_posts=self.get_all()
    posts_sorted_byDate=sorted(all_posts, key=lambda post: post.date)
    return posts_sorted_byDate     

        




   
