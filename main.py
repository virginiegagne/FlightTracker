from api import utils
from api import fetcher


def main_wrapper():
    #attributes are a thing
    print(f"This is the start of our python project. This function's name is {main_wrapper.__name__}")


    #Code here
    fetcher.states_accessor()
    fetcher.tracks_accessor()

    print("This is the end of our python project")

    pass

if __name__ == "__main__":
    main_wrapper()
#