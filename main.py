from api import utils



def main_wrapper():
    #attributes are a thing
    print(f"This is the start of our python project. This function's name is {main_wrapper.__name__}")


    #Code here
    utils.solid_example_1(example_param_1 = 'hi', example_param_2 = 2)
    utils.solid_example_2()
    utils.solid_example_3()


    print("This is the end of our python project")

    pass

if __name__ == "__main__":
    main_wrapper()
#