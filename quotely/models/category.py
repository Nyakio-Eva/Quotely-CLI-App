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
        """create a new instance of category  and save it to the database if it doesnot exist"""
        existing_category = cls.find_existing_category(name)
        if existing_category:
            print(f"Category '{name}' already exists.")
            return existing_category
        
        #if the category with the name doesnot exist
        category = cls(name)
        category.save()
       
        return category
    
    @classmethod
    def find_existing_category(cls, name):
        """check if a category with the given name already exists."""
        sql = "SELECT * FROM categories WHERE name =? "
        CURSOR.execute(sql, (name,))
        existing_category_data = CURSOR.fetchone()
        CONN.commit() 

        if existing_category_data:
            return cls(*existing_category_data)
        else:
            return None
        
    
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

    @classmethod
    def update_category(cls, category_id, new_name):
        """Update an existing category by ID with a new name"""
        sql = "UPDATE categories SET name = ? WHERE id = ?"
        CURSOR.execute(sql, (new_name, category_id))
        CONN.commit()

        # Check if any rows were affected by the update
        if CURSOR.rowcount > 0:
            # Update the local dictionary if category exists in it
            if category_id in cls.all:
                cls.all[category_id].name = new_name
            return cls.find_by_id(category_id)  # Return the updated category
        else:
            return None  # No category was updated
        
    @classmethod
    def delete(cls, category_id):
        """Delete a category from the database and the local dictionary based on its ID"""
        category = cls.find_by_id(category_id)
        
        if category:
            # Delete from database
            sql = "DELETE FROM categories WHERE id = ?"
            CURSOR.execute(sql, (category_id,))
            CONN.commit()

            # Delete from local dictionary
            del cls.all[category_id]
            print(f"Category '{category.name}' deleted successfully.")
        else:
            print(f"Category with ID {category_id} not found.")


        
from models.quote import Quote