
example = "thiS iS eXmaple"
print(example.title()) # This Is Exmaple
print(example.swapcase()) # THIs Is ExMAPLE

example = "lllllthiS iS eXmaplerrrrr"
print(example.lstrip('l')) #thiS iS eXmaplerrrrr
print(example.rstrip('r')) #lllllthiS iS eXmaple

example = "this is first example" 
print(example.replace('first','second')) #this is first example

#join: Convert the list back to string with link word
name = 'new file name'
name_list = name.split() # ['new', 'file', 'name']
file_name = '_'.join(name_list) # new_file_name
print(name_list)
print(file_name)

