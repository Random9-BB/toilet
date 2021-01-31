print("-----------v1.0.0------------")
a = input("请输入罗马数字（务必正确输入！！！）：")
c = list(a)
roman_numerals = 0
Serial_number = 0
b = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
while len(c) != 0:
    if int(b[c[Serial_number]]) < int(b[c[Serial_number+1]]):
        sum = b[c[Serial_number+1]]-b[c[Serial_number]]
        c.pop(0)
        c.pop(0)
    else:
        sum = b[c[Serial_number]]
        c.pop(0)
        if len(c) == 1:
            roman_numerals = roman_numerals + b[c[0]]
            c.pop(0)
    roman_numerals = roman_numerals + sum
print(roman_numerals)
print("--------------a num?ER lab product--------------")