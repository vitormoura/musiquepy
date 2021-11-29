from sqlalchemy import create_engine, text, insert, select
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session, registry, relationship

from sqlalchemy.sql.schema import Column, ForeignKey, MetaData, Table
from sqlalchemy.sql.sqltypes import Integer, String

conn: Connection
session: Session

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)


def testing_schema_with_orm():

    mapper_reg = registry()
    Base = mapper_reg.generate_base()
    #Base = declarative_base()

    class User(Base):
        __tablename__ = 'user_account'
        id = Column('id', Integer, primary_key=True)
        name = Column('name', String(30))
        fullname = Column('fullname', String)

        addresses = relationship('Address', back_populates='user')

    class Address(Base):
        __tablename__ = 'address'
        id = Column('id', Integer, primary_key=True)
        user_id = Column('user_id', ForeignKey(
            'user_account.id'), nullable=False)
        email_address = Column('email_address', String, nullable=False)

        user = relationship('User', back_populates='addresses')

    # create database
    mapper_reg.metadata.create_all(engine)

    # inserting (1)
    stmt = insert(User.__table__).values(
        name='spongebob', fullname='Sponge Bob Squarepants')
    compiled = stmt.compile()

    print(stmt)
    print(compiled.params)

    with engine.connect() as conn:
        conn: Connection

        result = conn.execute(stmt)
        conn.commit()

        print(result.inserted_primary_key)

    user_table = User.__table__

    # inserting (2)
    with engine.begin() as conn:
        stmt = insert(user_table, [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"}
        ])     

        conn.execute(stmt)   

    # select (1)
    print('select #1')
    with engine.connect() as conn:
        stmt = select(user_table).where(user_table.c.name == 'spongebob')

        for row in conn.execute(stmt):
            print(row)

    # select (2)
    print('select #2')

    with engine.connect() as conn:
        stmt = select(User)

        for row in conn.execute(stmt):
            print(row)


def testing_bd_metadata():
    metadata = MetaData()
    user_table = Table('user_account', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('name', String(30)),
                       Column('fullname', String),
                       )

    address_table = Table('address', metadata,
                          Column('id', Integer, primary_key=True),
                          Column('user_id', ForeignKey(
                              'user_account.id'), nullable=False),
                          Column('email_address', String, nullable=False)
                          )

    metadata.create_all(engine)


def testing_sql_statements():

    # "commit as you go"
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE some_table (x int, y int)"))

        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
        )

        conn.commit()

    # "begin once"
    with engine.begin() as conn:
        conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"), [
            {"x": 6, "y": 8}, {"x": 9, "y": 10}])

    with engine.connect() as conn:

        for x, y in conn.execute(text('SELECT * FROM some_table')):
            print(f'{x},{y}')

    # statements
    stmt = text(
        'SELECT * FROM some_table WHERE y > :y ORDER BY x, y').bindparams(y=6)

    with Session(engine) as session:
        result = session.execute(stmt)

        for row in result:
            print(f"({row['x']},{row['y']})")


if __name__ == '__main__':
    testing_schema_with_orm()
    # testing_bd_metadata()
