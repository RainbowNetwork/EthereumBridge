from mongoengine import Document, StringField, ReferenceField

from db.collections.eth_swap import ETHSwap


class Signatures(Document):
    tx_id = ReferenceField(ETHSwap, required=True)
    signed_tx = StringField(required=True)
    signer = StringField(required=True)
