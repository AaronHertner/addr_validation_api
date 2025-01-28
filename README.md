# Address Validator API  

This project acts as a middleware API that will accept requests and redirect them to the DeepSeek API  
To test yourself clone and run main.py
This will create an endpoint -> 0.0.0.0:8080/validate_addrress which accepts three variables  

1. A business name
2. An initial address
3. Any suggested address  
  
The returned result will be a JSON object containing DeepSeeks best approximation for a suggested address and some reasoning. Helpful as an 'OpenSource' address validator.