from error_logger import ErrorLogger

if __name__ == "__main__":
    # Declaring error logger
    err = ErrorLogger("ERROR.log")

    try:
        print("Paso 1")
        a, b, c = d

    except Exception as e:
        # Print error text and save the error
        print(err.get_error(e))
        err.save(e)

    try:
        print("Paso 2")
        raise Exception("Unknown Error on this code")

    except Exception as e:
        # Only save the error log
        err.save(e)