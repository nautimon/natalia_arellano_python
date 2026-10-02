# Section 1
name = "Sam"
age = 20
height = 5.7
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#Section 2
name = input("What is your name? ")
birth_year = int(input("What year were you born? "))
age = 2026 - birth_year

print(f"Hi {name}, your age is approximately {age}")

# Section 3
number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))

print(f"{number1} * {number2} = {number1 * number2}")

# Section 4
store_name = "nauti's kawaii corner"
item1 = "Hello Kitty Sticker Book"
item1_price = 15.99
item1_quantity = 1
item2 = "Moomin Dot Journal"
item2_price = 25.00
item2_quantity = 1
pre_tax_total = (item1_price * item1_quantity) + (item2_price * item2_quantity)
tax = pre_tax_total * 0.08625
total = pre_tax_total + tax

print()
print()
print()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(f"              {store_name}")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print()
print(f"{item1_quantity} x  {item1}           $ {item1_price:.2f}")
print(f"{item2_quantity} x  {item2}                 $ {item2_price:.2f}")
print()
print(f"Subtotal:                               $ {pre_tax_total:.2f}")
print(f"Sales Tax (8.625%):                      $ {tax:.2f}")
print()
print(f"Total:                                  $ {total:.2f}")
print()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("       Thank you for shopping with us!     ")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print()
print()
print()

# Section 5
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
hobby = input("Enter your favorite hobby: ")
fun_fact = input("Enter a fun fact about yourself: ")
birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year

print()
print()
print()
print("   ______________________________")
print(r" / \                             \.")
print(r" \_ |                            |.")
print("    |                            |.")
print(f"           PROFILE: {name}     ")
print("    |                            |.")
print("    |                            |.")
print(f"     Hometown: {hometown}")
print(f"     Hobby: {hobby}")
print(f"     Fun Fact: {fun_fact}")
print(f"     Age: {age}")
print("    |                            |.")
print("    |                            |.")
print("    |                            |.")
print("    |   _________________________|___")
print("    |  /                            /.")
print(r"    \_/____________________________/.")
print()
print()
print()
