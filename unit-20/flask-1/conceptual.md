## Conceptual Exercise

Answer the following questions below:

##### What are important differences between Python and JavaScript? #####
* Indentation and spacing matter to python, but not to JS
* Python uses classes to define objects, whereas js objects multiple ways
* From what I've seen, JS is a stronger functional programming option
* Python seems to rely heavily on frameworks and libararies
* JS is primarily used only in web development

##### Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you can try to get a missing key (like "c") *without* your programming crashing. 

```python
my_dict = {"a": 1, "b": 2}

value = my_dict.get("c")

try:
  value = my_dict["c"]
  print(value)
except KeyError:
  print("Key 'c' is not present in the dictionary")
  ```

##### What is a unit test? #####
* A test that checks one piece in isolation

##### What is an integration test? #####
* Taking individual pieces and testing they function correctly in conjuction

##### What is the role of web application framework, like Flask? #####
* It provides a standardized structure and set of tools for building web applications. They typically provide libraries,modules, and tools that help developers focus on building high level functionality. 

##### You can pass information to Flask either as a parameter in a route URL  (like `/foods/pretzel`) or using a URL query param (like `foods?type=pretzel`). How might you choose which one is a better fit for an application? #####
* You should set it as a route route if the subject is the main focus of a page (a pretty horse toy), and params if it modifies it (different colors the horse comes in)

##### How do you collect data from a URL placeholder parameter using Flask? #####
* By defining a route with a variable in the path and passing that similarly named argument into the route function

##### How do you collect data from the query string using Flask? #####
  * `request.args.get`

##### How do you collect data from the body of the request using Flask? #####
* `request.form`

##### What is a cookie and what kinds of things are they commonly used for? #####
* A cookie is a piece of information held in the browser that is attached to all requests sent to the server

##### What is the session object in Flask? #####
* A magical dictionary used to store data across multiple reqeusts

##### What does Flask's `jsonify()` do? #####
* Converts python into json formateed response object that can be returned in a flask view
