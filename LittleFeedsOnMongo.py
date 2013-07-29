from pymongo.connection import Connection
import logging
import humongolus as orm
import datetime
import humongolus.field as field
import humongolus.widget as widget
from tests.states import states
from DBConfig import*

conn = Connection()
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger("humongolus")

orm.settings(logger=logger, db_connection=conn)

class Newsfeed(orm.Document):
    """docstring for Newsfeed"""
    _db = dbName
    _collection = collectionName
    guid = field.Char(required=True)
    # rss_id = field.AutoIncrement(collection="newsfeeds")
    title = field.Char(required=True)
    descript = field.Char(required=True)
    link = field.Char(required=True)
    piclink = field.Char()
    # date = field.TimeStamp(required=True)
    source = field.Char()
    # category = field.Char(required=True)
    tags = field.Char()
    #Editor Related fields
    #0:Unviewed, 1:edited, 2:dismissed, 3:editLater
    editStatus = field.Integer(required=True, min=0, max=3)
    editorId = field.Integer(required=True)
    editorMemo = field.Char()
    editorDate = field.TimeStamp()
        
# def newNewsfeed(jData):
#     pass

# def commitEdition(jData):
#     pass

