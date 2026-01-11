Testing the API
To test the secured endpoints, you must first obtain an Authentication Token. Follow these steps using a tool like Postman, Insomnia, or cURL.

1. Get Your Token
Send a POST request to:

http://127.0.0.1:8000/api-token-auth/

Body (JSON):

JSON

{
    "username": "your_username",
    "password": "your_password"
}
Response: You will receive a key like "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b".

2. Testing the Inventory Items Endpoint (/items/)
This endpoint manages your primary stock data.

Headers required for all requests:

Key: Authorization

Value: Token YOUR_TOKEN_HERE

A. List All Items (GET)
URL: http://127.0.0.1:8000/api/v1/inventory/items/

Action: Retrieves all items you have permission to view.

B. Create a New Item (POST)
URL: http://127.0.0.1:8000/api/v1/inventory/items/

Body (JSON):

JSON

{
    "name": "Industrial Widget",
    "description": "Heavy-duty steel widget",
    "price": "45.00",
    "stock_level": 5,
    "reorder_point": 10
}
3. Testing the Low Stock Endpoint (/levels/)
This is a "smart" read-only endpoint used for inventory auditing.

URL: http://127.0.0.1:8000/api/v1/inventory/levels/

Method: GET

What it does: It automatically compares stock_level to reorder_point.

Expectation: If you created the "Industrial Widget" above with a stock of 5 and a reorder point of 10, it will appear in this list. If you update the stock to 15, it will automatically disappear from this list.

4. Testing Object-Level Permissions
To verify that your security logic works:

Create User A and User B.

Have User A create an item.

Try to DELETE or PUT (update) that item using User B's token.

Expected Result: The API should return a 403 Forbidden status code.