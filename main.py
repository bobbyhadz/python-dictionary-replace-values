# Replace values in a dictionary in Python

my_dict = {
    'name': 'default',
    'site': 'default',
    'id': 1,
    'topic': 'Python'
}


my_dict.update(
    {'name': 'borislav',
     'site': 'bobbyhadz.com'
    }
)

# 👇️ {'name': 'borislav', 'site': 'bobbyhadz.com', 'id': 1, 'topic': 'Python'}
print(my_dict)
