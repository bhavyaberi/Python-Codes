import random


def captcha_generator(n):
    captcha = ""
    letters = "qwertyuioplkjhgfdsazxcvbnm"
    letters += letters.upper()
    letters += "1234567890"
    letters += "!@#$%&*?/"
    while n:
        captcha += random.choice(letters)
        n -= 1
    return captcha


if __name__ == "__main__":
    captcha = captcha_generator(5)

    print("Enter Captcha: ", captcha)
    user_captcha = input()
    if captcha == user_captcha:
        print("Captcha matched.")
    else:
        print("Captcha did not match.")
