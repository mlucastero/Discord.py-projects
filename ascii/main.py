import ascii_magic 
local = ascii_magic.from_image_file('/users/matthewha/code-ha/python-projects/ascii/ty.png', columns=250)
#web = ascii_magic.from_url('', columns=100, char="",)
ascii_magic.to_terminal(local)