try:
    import requests
except ImportError:
    raise SystemExit("missing 'requests' dependency")

fizzbuzz_template = "https://www.google.com/search?q=what+is+{}+%25+15&btnK=Google+Search&oq=what+is+{}+%25+15"
buzz_template = "https://www.google.com/search?q=what+is+{}+%25+5&btnK=Google+Search&oq=what+is+{}+%25+5"
fizz_template = "https://www.google.com/search?q=what+is+{}+%25+3&btnK=Google+Search&oq=what+is+{}+%25+3"


start = int(input("start: "))
end = int(input("end: "))

for k in range(start, end):
    FB = "fizzbuzz"
    F = "fizz"
    B = "BUZZ"
    N = str(k)
    buzz = requests.get(buzz_template.format(k, k)).text
    if "%s modulo 5 = " % k in buzz:
        buzzmod = int(buzz.split("%s modulo 5 = " % k)[1].split("<")[0])
    fizz = requests.get(fizz_template.format(k, k)).text
    if "%s modulo 3 = " % k in fizz:
        fizzmod = int(fizz.split("%s modulo 3 = " % k)[1].split("<")[0])

    print([[FB, F, F, F, F], [B, N, N, N, N], [B, N, N, N, N]][fizzmod][buzzmod])
    
# or a shittier alternative

S,E=1,100
L="zzuBzziF"[::-1]+"".join([str(n) for n in range(S,E)])
for n in range(S,E):NS=8+sum(len(str(i)) for i in range(S,n));print(L.__getitem__(slice(*([[(None, 8), (None, 4), (None, 4), (None, 4), (None, 4)],[(4, 8), (NS, NS+len(str(n))), (NS, NS+len(str(n))), (NS, NS+len(str(n))), (NS, NS+len(str(n)))],[(4, 8), (NS, NS+len(str(n))), (NS, NS+len(str(n))), (NS, NS+len(str(n))), (NS, NS+len(str(n)))]][n % 3][n % 5]))))

# https://discord.gg/a8JBAg
