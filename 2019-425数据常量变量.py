Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> X=100
>>> X
100
>>> Y=100
>>> Y
100
>>> Y=200
>>> Y
200
>>> Y=20
>>> X=15
>>> Z=25
>>> X+(Y-Z)
10
>>> X=10
>>> X+=2
>>> X
12
>>> H=9
>>> X-=3
>>> X=10
>>> X
10
>>> X=X+H
>>> X
19
>>> print('helllo world')
helllo world
>>> print("hello world")
hello world
>>> print 'hello world'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>> print "hello world"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello world")?
>>> 13%2
1
>>> 9%2
1
>>> 14%3
2
>>> 13//4
3
>>> 9//4
2
>>> 13/3
4.333333333333333
>>> 3**3
27
>>> 100>50
True
>>> 1--<20
SyntaxError: invalid syntax
>>> 100<20
False
>>> 41!=h
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    41!=h
NameError: name 'h' is not defined
>>> 4!='h'
True
>>> true and true
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    true and true
NameError: name 'true' is not defined
>>> 1==1 and 2==2
True
>>> 1==1 or 2==2
True
>>> 1==1 and 2==3
False
>>> 1==1 or 2==3
True
>>> 2==3
False
>>> 1==1 not 2==2
SyntaxError: invalid syntax
>>> 1==2 or 3>4
False
>>> not 4<=3
True
>>> not 4==4 and 4<3
False
>>> not 4==4 and 4>3
False
>>> not 1!=2
False
>>> not 1+3==4
False
>>> 1+3==4
True
>>> home ='america'
>>> if home =='america'
SyntaxError: invalid syntax
>>> home = 'america'
>>> if home =='mareica':
	print('helle wordl')
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> home = 'america'
>>> if homg ==('america'):
	print('hello world')
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if homg ==('america'):
	print('hello world')
else:
	print('hello xiaoxu')

	
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    if homg ==('america'):
NameError: name 'homg' is not defined
>>> home = 'america'
>>> if home ==('america'):
	print('hello,xiaoxu')
else:
	print('hello,world')

	
hello,xiaoxu
>>> if home ==('america'):
	print('hello,xiaoxu')
        else:
	print('hello,world')
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> if home ==('america'):
	print('hello,xiaoxu')
else:
	print('hello,world')

hello,xiaoxu
>>> 1==2
False
>>> 1>2
False
>>> jj ='aadd'
>>> if jj ==('aadd'):
	print('mmnn')
else:
	print('ssaa')

	
mmnn
>>> home = 'canada'
>>> if home ==('america')
SyntaxError: invalid syntax
>>> if home = ('maerica'):
	
SyntaxError: invalid syntax
>>> home = 'canada'
>>> if home ==('america'):
	print('aaee')
else:
	print('ccmm')

	
ccmm
>>> y=10
>>> x=11
>>> if y==10:
	if x==11:
		priny('x=y')

		
Traceback (most recent call last):
  File "<pyshell#93>", line 3, in <module>
    priny('x=y')
NameError: name 'priny' is not defined
>>> y=10
>>> x=20
>>> if y==10:
	if x==2-:
		
SyntaxError: invalid syntax
>>> y=10
>>> x=10
>>> if y==10:
	if x==10:
		print(x+y)

		
20
>>> x=100
>>> if x ==10:
	print('yes')
else:
	x==20:
		
SyntaxError: invalid syntax
>>> x=10
>>> if x=2:
	
SyntaxError: invalid syntax
>>> x==100
False
>>> x==100
False
>>> x=100
>>> if x==10:
	print('yes')
else x==20:
	
SyntaxError: invalid syntax
>>> x=100
>>> if x==10:
	print('yes')
elif 
