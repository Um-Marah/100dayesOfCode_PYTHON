# this program to applay the Paython Operators 1 $$ day10
a = 10
b = 2.0
c = -6
d = -11.0
#Arithmetic operators 
sum = a+b #Addition
sub = a-b #subtraction
mul = c*d #multiplication
div = b/d #division
exp = a**b #exponentiation
floord = c//d #floor division
mod = a%d #modulus
text = "the sum of (10 + 2.0) = {}\nthe sub of (10 - 2.0) = {}\nthe mul of (-6 * -11.0) = {}\nthe div of (2.0 / -11.0) = {}\nthe exp of (10 ** 2) = {}\nthe floorDivision of (-6 // -11.0) = {}\nthe mode of (10 % -11.6) = {}\n"
print(text.format(sum,sub,mul,div,exp,floord,mod))
#Assignment operators
a = 10
b = 20.0
c = -6
d = -11.0
e = 2
f = 8
g = 3
h = 5
i = 40
a+=3
b*=5
c**=2
d//=8
e&=2
f<<=8
g^=8
h%=20
i-=10
print(a,b,c,d,e,f,g,h,i)
#Comparison operators
print(a == b)
print(c<d)
print(e>f)
print(g!=h)
print(i>=a)
print(g>=d)