try :

    num = int(input("Enter the number: "))
    result = 100/num


except ValueError:
    print("Give us only Integer Value !")

except ZeroDivisionError:
    print("You are trying to divide by Zero")

else:
    print("Ye tab Run Hota hai jab Exception na aaye")
    print("try barabar execute hone ke baad me")
    print(result)

finally:
    print("Ye run hona hi hai")