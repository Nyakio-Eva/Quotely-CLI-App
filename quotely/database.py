from models.__init__ import CONN,CURSOR
from models.quote import Quote
from models.category import Category


def seed_data():
    Quote.drop_table()
    Category.drop_table()
    Quote.create_table()
    Category.create_table()

    #create seed data
    humor = Category.create("humor")
    programming = Category.create("programming")
    motivational = Category.create("motivational")
    whiskey = Category.create("whiskey")
    life = Category.create("life")
    happiness = Category.create("happiness")

    Quote.create("So Stephen Hawking walks into a bar... just kidding.", "Storypick", humor.id)
    Quote.create("Why do programmers prefer dark mode? Cause light attracts bugs.", "ShivamLH", programming.id)
    Quote.create("Don't wish for it, work for it.", "Rachael Robbins", motivational.id )
    Quote.create("I like my whiskey like I like my opinions, straight up and strong","Abby Leigh", whiskey.id)
    Quote.create("life is soup and I'm a fork", "unknown", life.id)
    Quote.create("Smile with your eyes, smise", "Marie", happiness.id)    

seed_data()
print("it's been seeded")    