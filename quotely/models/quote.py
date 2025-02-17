from .__init__ import CURSOR, CONN

class Quote:
    all ={}

    def __init__(self, quote_text, author, category_id, id=None) -> None:
        self.id = id
        self.quote_text = quote_text
        self.author = author
        self.category_id = category_id

    def __repr__(self) -> str:
        return f"<Quote: {self.quote_text}, {self.author}, Author: {self.category_id}, Category: {self.id}>"
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, str) and len(author):
            self._author = author
        else:
            raise ValueError("author must be a non-empty string")


    @classmethod
    def create_table(cls):
        """create table that persists attributes of Quotes instances in the database"""
        sql = """
            CREATE TABLE IF NOT EXISTS quotes(
            id INTEGER PRIMARY KEY,
            quote_text TEXT,
            author TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """drop table that persists quotes instance """
        sql = """
            DROP TABLE IF EXISTS quotes;
        """ 
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, quote_text, author, category_id ) :
        """create a new instance of quote  and save it to the database"""
        #check if a quote with the same text ,author and category id already exists
        existing_quote = cls.find_existing_quote(quote_text,author,category_id)
        if existing_quote:
            print("Quote already exists.")
            return existing_quote
        
        #if quote doesn't exist, create a new instance nd save it
        quote = cls(quote_text,author,category_id)
        quote.save()
        return quote
    
    @classmethod
    def find_existing_quote(cls,quote_text, author, category_id):
        """check if a quote with the same text, author and category id exists """
        sql = """SELECT * FROM quotes 
            WHERE quote_text =? 
            AND author =? 
            AND category_id = ?
        """
        CURSOR.execute(sql, (quote_text,author,category_id))
        existing_quote_data = CURSOR.fetchone()
        CONN.commit()
        if existing_quote_data:
            return cls(*existing_quote_data)  #return the existing quote object
        else:
            return None
    
    def save(self):
        """insert a new row with attribute values of the quote using primary key id
        update local dictonary"""
        sql = """
            INSERT INTO quotes(quote_text, author, category_id)
            VALUES(?,?,?)
        """
        CURSOR.execute(sql, (self.quote_text,self.author,self.category_id))
        CONN.commit()

        self.id = CURSOR.lastrowid  #provides primary key value of the newly inserted row
        type(self).all[self.id] = self  #store instance to local class-level dictionary

    @classmethod
    def find_by_id(cls, quote_id):
        """returns a quote object based on its ID"""

        sql = "SELECT * FROM quotes WHERE id = ?"

        CURSOR.execute(sql, (quote_id,))
        quote_data = CURSOR.fetchone()
        CONN.commit()
        if quote_data:
            return cls(*quote_data)  # Create and return quote object from query result
        else:
            return None
    
    @classmethod
    def get_all_quotes(cls):
        """retrieve all quotes from the database"""
        
        sql = "SELECT * FROM quotes"
        CURSOR.execute(sql)
        all_quotes_data = CURSOR.fetchall()
        
        all_quotes = []
        for quote_data in all_quotes_data:
            all_quotes.append(cls(*quote_data))
           
        return all_quotes
    
    @classmethod
    def get_all_author_names(cls):
        """Retrieve all unique author names from the"""
        sql = "SELECT DISTINCT author FROM quotes"
        CURSOR.execute(sql)
        author_names_data = CURSOR.fetchall()

        author_names = [author_name[0] for author_name in author_names_data]
        return author_names
    
    @classmethod
    def get_all_quotes_ids(cls):
        """Retrieve all available quote IDS from the database"""
        sql = "SELECT id FROM quotes"
        CURSOR.execute(sql)
        quote_ids = CURSOR.fetchall()
        return [quote_id[0] for quote_id in quote_ids]

    @classmethod    
    def get_quotes_by_author(cls, author_name):
        """retrieve quotes based on an author"""
        sql = "SELECT * FROM quotes WHERE author = ?"
        CURSOR.execute(sql, (author_name,))
        quotes_data = CURSOR.fetchall()

        quotes_by_author = []
        for quote_data in quotes_data:
            quote_instance = cls(*quote_data)
            quotes_by_author.append(quote_instance)
        return quotes_by_author    

    @classmethod
    def get_category_ids_for_author(cls, author_name):
        """Retrieve category ids associated with quotes by a specific author"""
        sql = "SELECT DISTINCT category_id FROM quotes WHERE author = ?"
        CURSOR.execute(sql, (author_name,))
        category_ids = CURSOR.fetchall()
        return[category_id[0] for category_id in category_ids]
    
    @classmethod
    def get_categories_for_author(cls, author_name):
        """Retrieve categories associated with quotes by a specific author"""
        category_ids = cls.get_category_ids_for_author(author_name)
        categories = [Category.find_by_id(category_id) for category_id in category_ids if category_id is not None]
        return categories

    @classmethod
    def update_quote(cls, quote_id, quote_text, author, category_id):
        """Update an existing quote by ID with new details"""
        try:
            #convert category_id to integer if necessary
            category_id = int(category_id)
            # Update in database
            sql = """
                UPDATE quotes 
                SET quote_text = ?, author = ?, category_id = ? 
                WHERE id = ?
            """
        
            CURSOR.execute(sql, (quote_text, author, category_id, quote_id))
            CONN.commit()

            # Check if any rows were affected by the update
            if CURSOR.rowcount > 0:
                print(f"Quote with ID {quote_id} updated successfully.")
                updated_quote = cls.find_by_id(quote_id)  # Return the updated quote
                return updated_quote
            else:
                print(f"Quote with ID {quote_id} not found or no changes were made.")
                return None  # No quote was updated or quote not found
            
        except Exception as e:
            print("Error updating quote:", e) 

        
    @classmethod
    def delete_quote(cls, quote_id):
        """Delete a quote from the database and the local dictionary based on its ID"""
        # Check if the quote ID exists in the database
        quote = cls.find_by_id(quote_id)
        if quote:
            # Delete from database
            sql = "DELETE FROM quotes WHERE id = ?"
            CURSOR.execute(sql, (quote_id,))
            CONN.commit()

            # Delete from local dictionary if present
            if quote_id in cls.all:
                del cls.all[quote_id]

            print(f"Quote with ID {quote_id} deleted successfully.")
        else:
            print(f"Quote with ID {quote_id} not found.")

from models.category import Category
