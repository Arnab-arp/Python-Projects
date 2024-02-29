s = '12:40:22AM'

def timeConversion(s):
    final_output = ""
    time = s.split(':')
    if time[0] == '12' and time[-1][2:] == 'PM':
        pass
    elif time[0] == '12' and time[-1][2:] == 'AM':
        time[0] = '00'
    elif time[-1][2:] == 'PM':
        time[0] = str(int(time[0]) + 12)
    for i in time:
        final_output += i + ":"
    final_output = final_output[0:-3]
    print(final_output)
    return final_output
timeConversion(s)
