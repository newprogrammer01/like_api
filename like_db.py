import json
#Create Like counting class
from tinydb import TinyDB, Query
from tinydb.table import Document

class LikeDB:
    def __init__(self, db_path):
        #Initialize the database
        self.db_path = db_path
        self.db = TinyDB(db_path, indent=4)
        self.users = self.db.table('users')
        self.images = self.db.table('images')


    def save(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.db, f, indent=4)
    
    def all_likes(self):
        """Counts all users likes
        returns
            all users likes
        """
        pass
        
    def all_dislikes(self):
        """Counts all users dislikes
        returns
            all users dislikes
        """
        pass
        
        
    #Add a like to the database
    def add_like(self, user_id:str,image_id)->dict:
        '''
        Add a like to the database
        args:
            user_id: The user id of the user who liked the post
            image_id: The image id of the image that was liked
        returns:
            The number of likes and dislikes for the post
        '''
        # Get the user document
        # If the user document does not exist, create it
        if self.users.contains(doc_id=user_id):
            user_doc = self.users.get(doc_id=user_id)
            user_doc[image_id] = {'like': True, 'dislike': False}
        else:
            user_doc = {image_id: {'like': True, 'dislike': False}}
        # Create user document
     
        user_doc = Document(user_doc, doc_id=user_id)
        self.users.insert(user_doc)
        

  
    #Add a dislike to the database
    def add_dislike(self, user_id:str)->dict:
        '''
        Add a dislike to the database
        args:
            user_id: The user id of the user who disliked the post
        returns:
            The number of likes and dislikes for the post
        '''
        pass


db = LikeDB('like_db.json')

# db.add_like('user1', 'img1')
db.add_like('3', 'img2')