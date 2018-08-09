# Lin Xin

def number_check():
    CN_mobile = \
    [134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,
     187,188,147,178,1705]
    CN_union = \
    [130,131,132,155,156,185,186,145,176,1709]
    CN_telecom = \
    [133,153,180,181,189,177,1700]

    number = input('Enter Your number: ')
    while (not number.isdigit()) or (len(number) != 11):
        if not number.isdigit():
            print('Please input a number !')
        else:
            print('Invalid length, your number should be in 11 digits !')
        number = input('Enter Your number: ')

    isCN_mobile = (int(number[:3]) in CN_mobile) or (int(number[:4]) in CN_mobile)
    isCN_union = (int(number[:3]) in CN_union) or (int(number[:4]) in CN_union)
    isCN_telecom = (int(number[:3]) in CN_telecom) or (int(number[:4]) in CN_telecom)
    if isCN_mobile:
        print('Operator : China Mobile ')
        print('We\'re sending verification code via text to your phone: ' + number)
    elif isCN_union:
        print('Operator : China Union ')
        print('We\'re sending verification code via text to your phone: ' + number)
    elif isCN_telecom:
        print('Operator : China Telecom ')
        print('We\'re sending verification code via text to your phone: ' + number)
    else:
        print('No such a operator !')
        number_check()

number_check()