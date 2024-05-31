import matri

assert matri.extraer_matricula("...Hola.M.undo..") == 4
assert matri.extraer_matricula("........") == 1
assert matri.extraer_matricula(" ") == 0   