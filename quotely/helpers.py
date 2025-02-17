from models.quote import Quote
from models.category import Category


def exit_program():
    print("See you again!")
    exit()


#Quote helper methods    
def display_quotes_cli():
    quotes = Quote.get_all_quotes()
    for quote in quotes:
        print(quote)


def find_quotes_by_author_cli():
    author_names = Quote.get_all_author_names()

    print("Available authors:", end=" ") #no new line
    
    #display author names as alist
    print(list(author_names))

    author_name = input("Enter the author's name to view quotes: ")

    quotes = Quote.get_quotes_by_author(author_name)  
    print(quotes) if quotes else print(f'Quotes by {author_name} not found!')  

def find_quote_by_id_cli():
    quote_ids = Quote.get_all_quotes_ids()

    print("Available Quote IDs: ")

    #print the ids as a list of strings separated by commas
    print(f"[{', '.join(map(str, quote_ids))}]")

    quote_id = input("Enter the quote's id: ") 

    quote = Quote.find_by_id(quote_id)
    print(quote) if quote else print(f'Quote {quote_id} not found!')


def find_categories_by_author_cli():
    author_names = Quote.get_all_author_names()

    print("Available authors:", end=" ") #no new line
    
    #display author names as alist
    print(list(author_names))

    author_name = input("Enter author's name to view categories: ")
    categories = Quote.get_categories_for_author(author_name)
    print(categories) if categories else print(
        f'No category found for {author_name}')


def create_quote_cli():
    while True:
        quote_text = input("Enter the quote text: ")
        if quote_text.strip():  #check if input in not empty after stripping
            break
        else:
            print("Quote text cannot be empty. Please try again.")

    while True:
        author = input("Enter author's name: ")
        if author.strip():
            break
        else:
            print("Author's name cannot be empty. Please try again.")

    #display available categories
    print("Available categories: ")
    display_categories_cli()

    while True:
        category_id = input("Enter the category ID or '12' to create a new category: ")
        if category_id.strip() and category_id.isdigit():
            break
        else:
            print("Invalid category ID. Please enter a valid category ID or '12' to create a new category. ")    
             
    if category_id == '12':
        create_category_cli()
        category_id = input("Enter the newly created category ID: ")
    
    try:
        quote = Quote.create(quote_text, author, category_id)
        print(f'Quote added successfully: {quote}')
    except Exception as e:
        print("Error adding quote: ", e)


def update_quote_cli():
    quote_id = input("Enter the quote's id: ")
    if Quote.find_by_id(quote_id):
        try:
            while True:
                quote_text = input("Enter the new quote text: ")
                if quote_text.strip():
                    break
                else:
                    print("Error: New quote text cannot be empty.")

            while True:
                author = input("Enter new author name: ")
                if author.strip():
                    break
                else:
                    print("Error: New author name cannot be empty.")

            while True:
                category_id = input("Enter quote's category id: ")
                if category_id.strip() and category_id.isdigit():
                    break
                else:
                    print("Error: category ID cannot be empty. Please enter a valid id")

            updated_quote = Quote.update_quote(quote_id, quote_text, author, category_id)
            if updated_quote:
                print(f'Quote updated successfully: {updated_quote}')
            else:
                print(f'Quote with ID {quote_id} not found, so no changes were made.')

        except Exception as e:
            print("Error updating quote: ", e)
    else:
        print(f'Quote {quote_id} not found!')


def delete_quote_cli():
    quote_id = input("Enter the quote's id: ")
    if Quote.find_by_id(quote_id):
        confirm_delete = input(f"Are you sure you want to delete quote {quote_id} (yes/no): ")
        if confirm_delete.lower() == 'yes':
            Quote.delete_quote(quote_id)
            print(f'Quote {quote_id} deleted successfully!')
        else:
            print("Deletion canceled!")
    else:
        print(f'Quote with ID {quote_id} not found!')


#Category helper methods
def display_categories_cli():
    categories = Category.get_all_categories()
    for category in categories:
        print(category)


def find_category_by_name_cli():
    category_name = input("Enter the category name: ")
    category = Category.find_by_name(category_name)
    print(category) if category else print(
        f'Category {category_name} not found!')
    

def find_category_by_id_cli():
    category_id = input("Enter the category's id: ")
    category = Category.find_by_id(category_id)
    print(category) if category else print(
        f'Category {category_id} not found!')
    

def find_quotes_by_category_cli():
    category_ids = input("Enter category ids for quotes you want to view: ")
    quotes = Category.get_quotes_for_categories(category_ids)

    if quotes:
        print("Quotes:")
        for quote in quotes:
            print(quote)
    else:
        print(f'Category ids {category_ids} not found!')        


def create_category_cli():
    while True:
        name = input("Enter the category name: ")
        if name.strip():
            try:
                category = Category.create(name)
                print(f'Category created successfully: {category}')
                break

            except Exception as e:
                print("Error creating category: ", e)
        else:
            print("Error: category name cannot be empty.")


def update_category_cli():
    print("Available category IDs: ")
    display_categories_cli()

    while True:
        category_id = input("Enter the category's ID to edit: ")
        if category_id.strip():  
            if Category.find_by_id(category_id):
                break
            else:
                print(f'Category with ID {category_id} not found.')
        else:
            print("Error: Category ID cannot be empty.")

    while True:
        new_name = input("Enter the category's new name: ")
        if new_name.strip():  
            try:
                updated_category = Category.update_category(category_id, new_name)
                if updated_category:
                    print(f'Category updated successfully: {updated_category}')
                else:
                    print("No category was updated.")
                break  # Exit the loop if category update is successful
            except Exception as e:
                print("Error updating category: ", e)
        else:
            print("Error: New category name cannot be empty.")

def delete_category_cli():
    print("Available category IDs: ")
    display_categories_cli()

    category_id = input("Enter the category's ID to delete: ")
    category = Category.find_by_id(category_id)
    if category:
        confirm_delete = input(
            f"Are you sure you want to delete category '{category}'? (yes/no): ")
        if confirm_delete.lower() == 'yes':
            Category.delete(category_id)

            print(f"Category '{category}' deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print(f'Category with ID {category_id} not found!')            
