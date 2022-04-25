
def main():

    print("Welcome!Input the number of hours on Earth so you can see how many hours pass by on Europa")
    
    userInput = int(input("How many Europa days go by for every x Earth day"))

    Europa = userInput * 3.551 #hours for 1 day in Europa 85.224

    

    print(f"{userInput} days on Earth is {Europa}days compared to Europa, isn't that crazy? One day in Europa is 85.224hours")
main()