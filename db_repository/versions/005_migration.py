from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
question = Table('question', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('question', String(length=200)),
    Column('viedo_url', String(length=300)),
    Column('answer_one', String(length=200)),
    Column('answer_two', String(length=200)),
    Column('answer_three', String(length=200)),
    Column('answer_four', String(length=200)),
    Column('timestamp', DateTime),
    Column('test_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['question'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['question'].drop()
