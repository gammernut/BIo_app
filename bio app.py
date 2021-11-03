def title():
    print('bio app gammernut 6/16/2021')


def get_user_name():
    user_name = None
    user_name = input('what is your name?')
    user_name = user_name.strip().title()
    return user_name


def get_user_gender():
    user_gender = None
    user_gender = input("What is your gender? Male(1), Female(2), or Other(3) ?")
    user_gender = user_gender.upper().strip()
    if user_gender == "1":  # male

        user_conformation = input("Your pronoun for this session is He, is this correct?")

    elif user_gender == "2":  # female

        input("Your pronoun for this session is She, is this correct?")
    else:

        user_gender = "3"  # 3 or anything else? other / nonbinary

        input("Your pronoun for this session is They/Them, is this correct?")

    return user_gender


def get_user_age():
    user_age = None
    while True:
        try:
            user_age = int(input("enter your age "))
            break
        except ValueError:
            print("Please input a number")
            continue
    return user_age


def show_data():
    name = get_user_name()
    age = get_user_age()
    gender = get_user_gender()

    print(f"your name is {name}")
    print(f"your age is {age}")
    print(f"your pronouns are {gender}")
    print(f"your age is {age}, your name is {name} and your gender is {gender} thank you for using Gammernut's "
          f"friendly fucking privilege checker!")


title()

show_data()
