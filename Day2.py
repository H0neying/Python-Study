#This code has been written by Jongheon Yeo(H0neying) @SNU ECE
#If you want to contact me, please send an email to zkdnqh12@snu.ac.kr

#Week 2. Boolean Algebra and Control Flow

####################
#1. Boolean Algebra#
####################

#1.1. Boolean Variables: True and False
t = (1 == 1)
print(t)

f = (1 != 1)
print(f)

print('Note: True, False. 첫 글자는 꼭 대문자!! \n')

#1.2. Comparison Operators
same = (1 == 1)
different = (1 != 2)
big = (2 > 1)
small = (1 < 2)
ge = (1 <= 2)
le = (2 >= 1)

print('1 == 1:', same)
print('1 != 2:', different)
print('2 > 1:', big)
print('1 < 2:', small)
print('1 <= 2:', ge)
print('2 >= 1:', le, '\n')


#1.3. Boolean Operators
t = True
f = False
print('not operator(not)')
print('not True:', not t)
print('not False:', not f, '\n')

print('and operator(&, and)')
print('True and True:', t and t)
print('True and False:', t & f)
print('False and True:', f & t)
print('False and False:', f & f, '\n')

print('or operator(|, or)')
print('True or True:', t or t)
print('True or False:', t | f)
print('False or True:', f | t)
print('False or False:', f | f, '\n')



#1.4. Boolean type of other Datatype
#파이썬은 False, 0, 빈 자료(나중에 배움)을 제외하면 전부 True로 생각한다!
print('bool() 함수에 대해 Araboza')
print('bool(True):', bool(True))
print('bool(False):', bool(False), '\n')

print('bool(1):', bool(1))
print('bool(0):', bool(0))
print('bool(-1):', bool(-1))
print("bool('a'):", bool('a'))
print("bool('False'):", bool('False'), '\n')

print('고1 때의 추억을 되살려볼까?')
print('(True and False) or True:', (True and False) or True)
print('not(False and True) or False:', not(False and True) or False)
print('(not(False or True) or True) == (True and False):', (not(False or True) or True) == (True and False), '\n')

#Control Flow 1: if
print("if(bool):"
      "if 함수는 bool 자료를 받아, True인 경우 아래 내용을 실행하고, False라면 그냥 지나간다.")

if(True):
    print('True')

if(False):
    print('메롱')

print('if 안에도 if가 있을 수 있다!')
print('자연수를 넣어주세요:')
n = int(input())
if(n%2 == 0):
    if(n%3 == 0):
        print('n은 6의 배수입니다')
    if(n%3 == 1 or n%3 == 2):
        print('n은 짝수이지만, 3의 배수는 아닙니다.')

#Control Flow 1-1: else
print('그치만...저렇게 일일히 다 쓰긴 귀찮은걸')

print('자연수를 넣어주세요:')
n = int(input())
if(n%2 == 0):
    if(n%3 == 0):
        print('n은 6의 배수입니다')
    else:
        print('n은 짝수이지만, 3의 배수는 아닙니다.')
else:
    print('n은 홀수입니다')

print('\n')

#Control Flow 1-2: elif
print('자연수를 넣어주세요:')
n = int(input())
if(n%2 == 0):
    if(n%3 == 0):
        print('n은 6의 배수입니다')
    elif(n%3 == 1):
        print('n은 짝수이고, 3으로 나눈 나머지는 1입니다.')
    else:
        print('n은 짝수이지만, 3으로 나눈 나머지는 2입니다.')
else:
    print('n은 홀수입니다')


#Control Flow 2: while



#Control Flow 3: for
