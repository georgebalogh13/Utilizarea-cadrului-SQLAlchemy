from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String 

engine = create_engine('sqlite:///example.db', echo = True)

meta = MetaData() 
books = Table( 'books', meta, Column('id', Integer, primary_key = True), Column('title', String), Column('year', Integer), ) 

meta.create_all(engine)

def insert_book(title, year):
    query = books.insert().values(title= title, year= year)
    conn = engine.connect()
    result=conn.execute(query)    

def showBooks():
    query = books.select()
    conn = engine.connect()
    result = conn.execute(query)

    for book in result:
        print("Book with id: " + str(book.id) + " has title: " +  book.title + ", appeared in " + str(book.year))

print("")
print("")
print("")
print("Inserting books...please wait")
print("")
print("")
print("")

insert_book("test title", 1999)
insert_book("test title 1", 2006)
insert_book("test title 2 ", 2022)

print("")
print("")
print("")
print("**************  Retrieving all books from db...  ***************")
print("")
print("")
print("")
showBooks()