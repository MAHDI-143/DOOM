import platform

bit = platform.architecture()[0]

if bit == '64bit':
    import DOOM
elif bit == '32bit':
    print("32bit not supported")
