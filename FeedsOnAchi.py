from pprint import pprint
from mongoalchemy.session import Session
from mongoalchemy.document import Document, Index
from mongoalchemy.fields import StringField

class Newsfeed(Document):
    guid = StringField(_id=True)
    title = StringField()
    description = StringField()
    rssid = StringField(max_length=10, min_length=0,required=False)
    link = StringField()
    # piclink = StringField(required = False)
    # source = StringField(required = False)
    # tags = ListField(StringField(), required = False)
    # date = DateTimeField(required = False)
    # category = ListField(StringField(), required = False)
    # editStatus = IntField(min_value=0, required = False)
    # editorId = IntField(min_value=0, required = False)
    # editorMemo = StringField(required = False)
    # editDate   = DateTimeField(required = False)
    guid_index = Index().ascending('guid').unique()

    def newNewsfeed(jData):
        pass

    def commitEdition(jData):
        pass

