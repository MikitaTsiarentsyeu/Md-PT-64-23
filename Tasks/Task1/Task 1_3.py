def kmh_to_ms():
    km_h = input('Enter speed in km/h:\n')
    m_s = float(km_h)/3.6
    m_s = format(m_s,'.2f')
    print(f'{km_h}'' km/h = 'f'{m_s}'' m/s')
    input('Press Enter to exit...')
try:
    kmh_to_ms()
except:
    print('Wrong enter. Enter must contain only numbers.')
    input('Press Enter to exit...')