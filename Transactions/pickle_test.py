import pickle

class Deneme:    
    def printer(self, first_exp:str, num:int):
        print(f"First Exp: {first_exp}\nNum: {num}")

if __name__ == "__main__":
    deneme = Deneme()

    func = deneme.printer
    params = ("Pickle Test", 10)
    
    with open("params.pkl", "wb") as file:
        pickle.dump(func, file)
        pickle.dump(params, file)
    
    with open("params.pkl", "rb") as file:
        loaded_func = pickle.load(file)
        loaded_params = pickle.load(file)
    
    loaded_func(*loaded_params)