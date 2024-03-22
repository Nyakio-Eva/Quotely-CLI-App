from models.__init__ import CURSOR, CONN


class Category:
    all = {}

    def __init__(self,name,id=None) -> None:
        self.id =id
        self.name = name
        
    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("name must be a non-empty string")
        
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

    # @classmethod
    # def find_by_id(cls, category_id):
    #     """returns a category object based on its ID"""

    #     sql = "SELECT * FROM categories WHERE id = ?"

    #     CURSOR.execute(sql, (category_id,))
    #     category_data = CURSOR.fetchone()
    #     CONN.commit()
    #     if category_data:
    #         print(category_data)
    #         return cls(*category_data)  ## Create and return category object from query result
            
    #     else:
    #         return None
    






from models.quote import Quote