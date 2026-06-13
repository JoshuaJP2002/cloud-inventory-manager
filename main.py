import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Connect to Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Create Firestore client
db = firestore.client()


def add_product():
    """
    Add a product to Firestore.
    """

    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    product = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    db.collection("products").add(product)

    print("Product added successfully!")


def view_products():
    """
    Display all products from Firestore.
    """

    products = db.collection("products").stream()

    print("\n----- PRODUCTS -----")

    found = False

    for product in products:
        found = True

        data = product.to_dict()

        print(f"\nID: {product.id}")
        print(f"Name: {data['name']}")
        print(f"Quantity: {data['quantity']}")
        print(f"Price: ${data['price']}")

    if not found:
        print("No products found.")

def update_product():
    """
    Update an existing product.
    """

    product_id = input("Enter product ID: ")

    doc_ref = db.collection("products").document(product_id)

    doc = doc_ref.get()

    if doc.exists:

        print("\nEnter new values")

        new_name = input("New name: ")
        new_quantity = int(input("New quantity: "))
        new_price = float(input("New price: "))

        doc_ref.update({
            "name": new_name,
            "quantity": new_quantity,
            "price": new_price
        })

        print("Product updated successfully!")

    else:
        print("Product not found.")

def delete_product():
    """
    Delete a product from Firestore.
    """

    product_id = input("Enter product ID: ")

    doc_ref = db.collection("products").document(product_id)

    doc = doc_ref.get()

    if doc.exists:

        doc_ref.delete()

        print("Product deleted successfully!")

    else:
        print("Product not found.")

def main():
    """
    Main menu for the inventory system.
    """

    while True:

        print("\n==============================")
        print(" CLOUD INVENTORY MANAGER")
        print("==============================")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            update_product()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


main()