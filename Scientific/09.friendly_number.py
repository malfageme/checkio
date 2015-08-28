def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    powers_list = [(base**x,y) for x,y in enumerate(powers)]
    g = 0
    final_power = ''
    for power in powers_list[::-1]:
        g = float(number) / power[0]
        if abs(g) >= 1:
            final_power = power[1]
            break
    if decimals>0:
        g_str = ("%#."+str(decimals)+"f") % (g)
    else:
        g_str = str(int(g))
    return "".join([g_str,final_power,suffix])


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'


