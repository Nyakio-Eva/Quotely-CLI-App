from helpers import (
    exit_program,
    display_quotes_cli,
    find_quotes_by_author_cli,
    find_quote_by_id_cli,
    find_categories_by_author_cli,
    create_quote_cli,
    update_quote_cli,
    delete_quote_cli,
    display_categories_cli,
    find_category_by_name_cli,
    find_category_by_id_cli,
    find_quotes_by_category_cli,
    create_category_cli,
    update_category_cli,
    delete_category_cli
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            display_quotes_cli()
        elif choice == "2":
            find_quotes_by_author_cli()
        elif choice == "3":
            find_quote_by_id_cli()
        elif choice == "4":
            find_categories_by_author_cli()
        elif choice == "5":
            create_quote_cli()
        elif choice == "6":
            update_quote_cli()
        elif choice == "7":
            delete_quote_cli()
        elif choice == "8":
            display_categories_cli()
        elif choice == "9":
            find_category_by_name_cli()
        elif choice == "10":
            find_category_by_id_cli()
        elif choice == "11":
            find_quotes_by_category_cli()
        elif choice == "12":
            create_category_cli()
        elif choice == "13":
            update_category_cli()
        elif choice == "14":
            delete_category_cli()
        else:
            print("Invalid choice, please enter a valid option")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. View all quotes")
    print("2. Find quotes by author name")
    print("3. Find quote by id ")
    print("4. Find categories by author name")
    print("5. Create quote")
    print("6. Update quote")
    print("7. Delete quote")
    print("8. View all categories")
    print("9. Find category by name")
    print("10. Find category by 1d")
    print("11. Find quotes by category")
    print("12. Create category")
    print("13. Update category")
    print("14. Delete category")


if __name__ == "__main__":
    main()    