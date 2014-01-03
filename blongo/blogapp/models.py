#from django.db import models

# Create your models here.
# models added by micadeyeye
from mongoengine import *
#from blongo.settings import DATE_INPUT_FORMATS
from blongo.settings import DBNAME
from djangotoolbox.fields import EmbeddedModelField
DB_NAME = DBNAME

connect(DBNAME)

class Post(Document):
    title = StringField(max_length=500, required=True)
    authors = StringField(max_length=500, required=True)
    publisher = StringField(max_length=500, required=True)
    papertype = StringField(max_length=500, required=True)
    #additional_info = StringField(max_length=500, required=True)
    #page_num = StringField(max_length=500, required=True)
    #date_published = DateTimeField(required=True)
    #selectedpublication = BooleanField(default=False)
#    section = EmbeddedModelField('Section')

class Profile(Document):
    details = StringField(max_length=10000, required=True)
    
#==============================================================================
# class User(Document):
#         email = EmailField(required=True)
#         password = StringField(max_length=50000, required=True)
#         sections = EmbeddedModelField('Section')
#==============================================================================
        
class Section(Document):
    heading = StringField(max_length=120, required=True)
    content = StringField(max_length=50000, required=True)

