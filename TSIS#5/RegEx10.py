import re

def camel_to_snake(camel_str):
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_str
    
camel_string = input()
snake_string = camel_to_snake(camel_string)
print(snake_string) 