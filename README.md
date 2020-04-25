# python_errors

## Description
It is a class for log to file errors on python. In order to debug complex software 
that can't be degugged on debugger like CLI commands, this class ca help you.

## Descripción
Es una clase para escribir logs de error a un archivo de forma sencilla.

Algunas ocasiones necesitamos enviar logs de error a un archivo de error y necesitamos
conocer el archivo, la hora, la línea, el mensaje de error y el tipo de error que se generó.
Esto hace la tarea de depurar el archivo mucho más sencilla.

## How to use? | ¿Cómo usarlo?

```python
from error_logger import ErrorLogger

# Declaring error logger
err = ErrorLogger("ERROR.log")

# Catching errors
try:
    print("Paso 2")
    raise Exception("Unknown Error on this code")

except Exception as e:
    # Only save the error log
    err.save(e)
```

This code makes a file called ERROR.log and save a text similar to this:
El código guarda un archivo llamado ERROR.log con un texto parecido a esto:
````
------- [2020-04-25 02:33:47.641708]:
        File: /Users/.../error_logger.py
        [Error: Exception]: Unknown Error on this code 
        Line: 18
