import random
def generate_password(length=8):
    if length < 5:
        return print("La contraseña no puede tener menos de 5 caracteres.")
    elif length > 10:
        return print("La contraseña no puede tener más de 10 caracteres.")
    else:
        special_chracters = ["@", "#", "$", "&"]
        upper = chr(random.randint(65, 90))
        lower = chr(random.randint(97, 122))
        special = random.choice(special_chracters)
        number = random.randint(1000000, 9999999)
        password = upper + lower + special + str(number)
        length_password = random.sample(password, length)
        password = ("").join(length_password)
        return print(password)

new_password = generate_password(int(input("Eliga cuantos caracteres quiere tener su contraseña (debe ser entre 5 y 10 caracteres): ")))

