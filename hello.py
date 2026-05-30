import pyfiglet
from termcolor import cprint


result = pyfiglet.figlet_format("Hello  World !  = )\nMy  name  is  Ben ,  \nand  this  is  the  start  of\n")
cprint(result, "cyan", attrs=["bold"])
result = pyfiglet.figlet_format("MY CODING \nJOURNEY ! ")
cprint(result, "red", attrs=["bold"])
result = pyfiglet.figlet_format("\nI'm  learning  \nas  I  build,  \nand  my  goal  is  \nto  make  the\n")
cprint(result, "yellow", attrs=["bold"])
result = pyfiglet.figlet_format("THE  BEST  PORTFOLIO  \nPOSSIBLE !!")
cprint(result, "green", attrs=["bold"])
result = pyfiglet.figlet_format("\nI  hope  you  fancy  my  projects  =3")
cprint(result, "cyan", attrs=["bold"])



