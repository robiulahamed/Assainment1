#implment   program name with greeds
def greet():
    name = input("Enter your name: ")

    message = f"Hello, {name}! you are very great work "
    print(message)


greet()


#chek adult or minor programe 
def check_age():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")


check_age()


# read and write file 
input_file = "input_data.txt"
output_file = "output_data.txt"

def process_data(input_file, output_file):
    try:
        
        with open(input_file, 'r') as f:
            
            data = f.read()

            
            processed_data = data.upper()

       
        with open(output_file, 'w') as f:

            f.write(processed_data)

        print("Processing complete. Check", output_file, "for the result.")
    except FileNotFoundError:
        print("File not found:", input_file)


process_data(input_file, output_file)