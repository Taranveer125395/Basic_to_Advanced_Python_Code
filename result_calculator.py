a = int(input('Enter Your Punjabi Marks: '))
b = int(input('Enter Your English Marks: '))
c = int(input('Enter Your Mathematics Marks: '))
d = int(input('Enter Your Physics Marks: '))
e = int(input('Enter Your Chemistry Marks: '))

f = a + b + c + d + e
g = (f / 500) * 100

print('---------------Result Details----------------')
print(f'Punjabi: {a}')
print(f'English: {b}')
print(f'Mathematics: {c}')
print(f'Physics: {d}')
print(f'Chemistry: {e}')

if g < 33:
    print('Fail in All Subjects')
    print('Result: Fail')

elif a < 33 and b < 33 and c < 33:
    print('Fail in Examination & Repeat the Class')
    print('Result: Fail')

elif a < 33 and b < 33 and d < 33:
    print('Fail in Examination & Repeat the Class')
    print('Result: Fail')

elif a < 33 and b < 33 and e < 33:
    print('Fail in Examination & Repeat the Class')
    print('Result: Fail')

elif a < 33 and c < 33 and d < 33:
    print('Fail in Examination & Repeat the Class')
    print('Result: Fail')

elif a < 33 and c < 33 and e < 33:
    print('Fail in Examination & Repeat the Class')
    print('Result: Fail')

elif a < 33 and d < 33 and e < 33:
    print('Fail in Examination & Repeat the Class')
    print('Result: Fail')

elif b < 33 and c < 33 and d < 33:
    print('Fail in Examination & Repeat the Class')
    print('Result: Fail')

elif b < 33 and c < 33 and e < 33:
    print('Fail in Examination & Repeat the Class')
    print('Result: Fail')

elif b < 33 and d < 33 and e < 33:
    print('Fail in Examination & Repeat the Class')
    print('Result: Fail')

elif c < 33 and d < 33 and e < 33:
    print('Fail in Examination & Repeat the Class')
    print('Result: Fail')

elif a < 33 and b < 33:
    print('Reappear in Punjabi and English')

elif a < 33 and c < 33:
    print('Reappear in Punjabi and Mathematics')

elif a < 33 and d < 33:
    print('Reappear in Punjabi and Physics')

elif a < 33 and e < 33:
    print('Reappear in Punjabi and Chemistry')

elif b < 33 and c < 33:
    print('Reappear in English and Mathematics')

elif b < 33 and d < 33:
    print('Reappear in English and Physics')

elif b < 33 and e < 33:
    print('Reappear in English and Chemistry')

elif c < 33 and d < 33:
    print('Reappear in Mathematics and Physics')

elif c < 33 and e < 33:
    print('Reappear in Mathematics and Chemistry')

elif d < 33 and e < 33:
    print('Reappear in Physics and Chemistry')

elif a < 33:
    print('Reappear in Punjabi')

elif b < 33:
    print('Reappear in English')

elif c < 33:
    print('Reappear in Mathematics')

elif d < 33:
    print('Reappear in Physics')

elif e < 33:
    print('Reappear in Chemistry')

else:
    print(f'Total: {f}')
    print(f'Percentage: {g}')
    print('Result: PASS')

if g >= 90:
    print('Grade: A+')
    
elif g < 90 and g >= 80:
    print('Grade: A')
    
elif g < 80 and g >= 70:
    print('Grade: B+')
    
elif g < 70 and g >= 60:
    print('Grade: B')
    
elif g < 60 and g >= 50:
    print('Grade: C+')
    
elif g < 50 and g >= 40:
    print('Grade: C')
    
elif g < 40 and g >= 33:
    print('Grade: D')
    
else:
    print('Grade: F')
    