from models.__init__ import CURSOR, CONN


class Category:
    all = {}

    def __init__(self,name,id=None) -> None:
        self.id =id
        self.name = name

    def __repr__(self) -> str:
        return f"<Category: {self.name}, {self.id} >"    
    

    # @property
    # def name(self):
    #     return self.name 

    # @name.setter
    # def name(self, name):
    #     if isinstance(name, str):
    #         cleaned_name = name.strip()   #remove trailing whitespaces
    #         if cleaned_name and  len(cleaned_name) >= 2 and len(cleaned_name) <= 15:
    #             self.name = cleaned_name
    #         else:
    #             raise ValueError("name must be between 2 and 15 characters")
                
    #     else:
    #         raise ValueError("name must be a non-empty string")
        
    @classmethod
    def create_table(cls):
        """create table that persists attributes of Category instances in the database"""
        sql = """
            CREATE TABLE IF NOT EXISTS categories(
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """drop table that persists category instances """
        sql = """
            DROP TABLE IF EXISTS categories;
        """ 
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name ) :
        """create a new instance of category  and save it to the database"""
        category = cls(name)
        category.save()
       
        return category
    
    def save(self):
        """insert a new row with attribute values of the category instance using primary key id,
        update local dictonary"""
        sql = """
            INSERT INTO categories(name)
            VALUES(?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid  #provides primary key value of the newly inserted row
        type(self).all[self.id] = self  #store instance to local class-level dictionary

    @classmethod
    def find_by_id(cls, category_id):
        """returns a category object based on its ID"""

        sql = "SELECT * FROM categories WHERE id = ?"

        CURSOR.execute(sql, (category_id,))
        category_data = CURSOR.fetchone()
        CONN.commit()
        if category_data:
           #print("Found category:", category_data)
           return cls(*category_data)  # Create and return category object from query result
        else:
           return None

    
    @classmethod
    def find_by_name(cls, category_name):
        """Returns a category object based on its name"""
        sql = "SELECT * FROM categories WHERE name = ?"
        CURSOR.execute(sql, (category_name,))
        category_data = CURSOR.fetchone()
        CONN.commit()
        if category_data:
            
            return cls(*category_data)
        else:
            return None

    @classmethod
    def get_all_categories(cls):
        """retrieve all categories from the database""" 
        sql = "SELECT * FROM categories"
        CURSOR.execute(sql)
        all_categories_data = CURSOR.fetchall()
        
        all_categories = []
        for category_data in all_categories_data:
            category_instance = cls(*category_data)
            all_categories.append(category_instance)
           
        return all_categories
        
    def get_quotes_for_categories(cls, category_ids):
        """retrieve quotes belonging to categories specified by their ids"""

        #generate placeholders for the IN clause based on the number of category IDs
        placeholders = ','.join(['?' for _ in range(len(category_ids))])

        #query with dynamic placeholders
        sql = f"SELECT * FROM quotes WHERE category_id IN ({placeholders})"
        #print("sql query:", sql)

        try:
            CURSOR.execute(sql, category_ids)
            quotes_data = CURSOR.fetchall()
            #print("quotes data:", quotes_data)
            
            quotes = []
            for quote_data in quotes_data:
                quote_instance = Quote(*quote_data)
                quotes.append(quote_instance)
                #print("found quote:", quote_instance)

            return quotes 
        except Exception as e:
            print("Error fetching quotes:", e)  


        
from models.quote import Quote