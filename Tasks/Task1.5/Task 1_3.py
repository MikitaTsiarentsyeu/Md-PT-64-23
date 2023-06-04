import re
km_h = input('Enter speed in km/h:\n').replace(',','.')

if re.search(r'[a-zA-Zа-яА-я]',km_h):
    print('Enter must contain only numbers, no letters.')
elif len(km_h) == 0:
    print("Input can't be empty.")
elif re.search(r'[!@#$%:,"#?°]',km_h):
    print("Don't use special characters!")
elif re.search(r'[ ]',km_h):
    print("Don't use spaces!")
elif float(km_h) <= 0:
    print('The entered value is too low. The value must be more then 0.')
else:
    m_s = float(km_h)/3.6
    m_s = format(m_s,'.2f')
    print(f'{km_h}'' km/h = 'f'{m_s}'' m/s')
    input('Press Enter to exit...')
