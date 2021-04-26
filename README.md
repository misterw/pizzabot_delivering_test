# PizzaBot delivering
Script instructs Pizzabot on how to deliver pizzas to all the houses in a neighborhood.

Script supports input in the next format: *<area_x>x<area_y> (<point_x>,<point_y>) [more points ...]*

Example: "5x5 (1,2) (4,4)"
## How to use
After cloning this repo, you can use it by next ways:
- Clone: `- git clone https://github.com/misterw/pizzabot_delivering_test.git`
### Command line:
- Go to directory `cd pizzabot_delivering_test/`
- Run `./pizzabot "5x5 (1,2) (4,4)"`
###  Python code:
- You can use usual imports `from pizzabot import pizzabot`
- And run using `pizzabot("5x5 (1,2) (4,4)")`
###  Unit tests:
- *tests.py* contains all unit tests. You are free to use it like you want
### Coverage:
- Run `pip install -r requirements-dev.txt`
- Run coverage: `coverage run -m unittest tests.py`
- Get report: `coverage report -m`
