def input_value(answersList, typeOfValue = int):
    
    for item in answersList:
        try:
            text = "Please enter the "+ item + ": "
            x = typeOfValue(input(text))
        except ValueError:
            print(f"Only {typeOfValue} are allowed")

