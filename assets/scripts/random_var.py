****************************
*****************************
*  RANDOM VARIABLES*********
* Calculating Expectation 
* or Mean and Variance and SD
* Adding or Subtraction
*****************************
****************************

Expected Value:
E[x]=sum(p(i)*x(i))

"Lets say X takes 3 values
with p =1/6 it is $1, with
p = 4/6 its $2 and with p =1/6 
it is $6."

We get 1/6*$1 +4/6*$2+1/6*$6=
$2.5. 
(This is fine w/ negatives too)

Variance
Var(X)=sum( p(i)*(x(i)-E[x])^2)

1/6*(1-2.5)^2 + 4/6*(2-2.5)^2+
1/6*(6-2.5)^2 = 
2.583 dollars-squared

Standard Dev = sqrt(Var)
StandDev=1.607 dollars
******************************
* E[X+10] =E[X] +10
or 
* E[X-.5]= E[X]-0.5

if we changed the payouts by
+10 so
1/6*11 + 4/6*12+ 1/6*16 = 
2.5+10=12.5

Or if we changed them by -.5
1/6*.5 + 4/6*1.5 +1/6*5.5 =
2.5-.5 = 2

* VAR AND StdDev DO NOT CHANGE
* IF YOU JUST ADD OR SUBTRACT
* They Do IF YOU MULTIPLY 
THOUGH

Multiply all numbers by 10
E[10*X] = 10*E[X]
1/6*10 + 4/6*20 +1/6*60=25

Variance is now 10^2 *var(x)
or
100*Var(x)

SD is 10*SD though. 
Z or T score wouldn't change

Same w/ fractions.
Var(.6X+.4Y)=
.36Var(X)+.16Var(Y)
if ind! then take sqrt for sd.

To restate for a constant 
number C (like 7):

E[c*x]=c*E[x]
var(c*x)=c^2*var(x)
sd(cx)=abs_val(c)*sd(x)

E[x+c]=E[x]+c
var(x+c)=var(x)
sd(x+c)=sd(x)

****************************
***************************
* ADDING INDP 
* RANDOM VARIABLES**
******************************
* What About X+Y 
* ONLY IF INDEPENDENT!!!
* E(X+Y) or mean(X+Y)=
E(X) + E(Y) or 
mean(X) + mean(Y)
**************************
* ONLY IF INDEPENDENT!!!
* Var(X+Y) = Var(X) + Var(Y)
*BUT SD(X+Y) is not! adder
* It is sqrt[Var(X)+ Var(Y)]

So if sd(x)=sigma_x
and sd(y)=sigma_y

sd(X+Y)=
sqrt[sigma_x^2+sigma_y^2]
IF INDEPENDENT!
******
Add/subtract NORMALS
stays normal with
mean mu1+mu2 and sd
=sqrt[Var(X)+ Var(Y)].

*************************
* Example Question

------------------------------
Each carton has 1 container 12 
eggs. The weight of cartons+
eggs is normal with mean 840g and
sd of 7.9g

(a) What is the probability a 
randomly selected carton will 
weigh more than 850 grams?

P( Z>(850-840)/7.9)=P(Z>1.27)=
0.1

(b) The weights of the empty  
containers is normal w mean 20g
and sd 1.7g. Assume independent
contained and egg.

Let the random variable X be 
the weight of a single egg.
 i) What is the mean of X ?
 ii) What is the standard 
 deviation of X ? 
 
So 840=20+12*E(x) -> E(x)=68.3
Var(full)=Var(container)+
var(X1)+var(x2)+..+var(x12).

If SD (c)=1.7, var(c)=1.7^2
 SD (full)=7.9,var(full)=7.9^2 
 Then 
 62.4=2.9+12*Var(X). 
 Var(x)=4.96. So SD(X)=
 sqrt(4.96)=2.23.
 
