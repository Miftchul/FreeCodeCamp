temp = "5 degrees"
cel = 0

try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
except ValueError:
    print("Input suhu tidak valid:", temp)

print(cel)
