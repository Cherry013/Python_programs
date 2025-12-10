try:
    age = int(input("Enter you age: "))
    if age > 18:
        print("Pass")
    else:
        print("Fail")

except Exception as e:
    print(f"You've entered Inavalid Integer with exception ==>({e}) , you need to enter numbers like --> 12,15,18etc..")
    age = int(input("Enetr your age: "))
    if age > 18:
        print("Pass")
    else:
        print("Fail")

finally:
    print("Completed")


# import turtle as t


# s = t.Turtle()
# s.speed("fastest")
# s.circle(100)
# s.setheading(s.heading()+50)
# s.circle(100)

# screen = t.Screen()
# screen.exitonclick()
