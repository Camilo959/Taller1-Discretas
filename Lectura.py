class Lectura:

    def __init__(self):
        pass

    def read(self, route): 

        try:
            with open(route, 'r') as f_obj:
                lines = f_obj.readlines()
            return lines
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")

            return 'Error'