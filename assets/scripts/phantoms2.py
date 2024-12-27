*  Hypothesis Testing
* 1) Slope
* 2) Chi-Sq 1 dimension:
  Goodness of Fit
* 3) Chi-Sq 2 dimension:

     Homogenous/Independence

P. state pop parameter
H. state hypothesis
A. state assumptions
N. name test
T. calc t-statistic
O. obtain p-val
M. make reject/ fail toreject
   decision
S: state conlusion in context

*****************************
1) SLOPE
*****************************
P: "The parameter of interest
is the slope of 
the POPULATION least squares
line between "weight
in grams" and 
"height in inches" beta1=m

(I put weight and height 
to remind you to say units)

H:  The null hypothesis is
     Ho:  beta1=0
The alternate hypothesis is
      Ha: beta1 not equal 0
      
(or less than or greater
in Ha: as needed. 
Usually not equal though!) 

A: Independent obs, 
simple random sample.

ASSUME the Relationship
is Linear.

Assume the Residuals are
Normally Distributed.

Assume the Variance of
Residuals is Constant.

Assume the Residuals are
Independent.

N: We will do a T  test 
on an least squares slope
with 
significance level alpha
(alpha = 0.05)  

Say the degrees of
freedom = N-2 where 
N is sample size.

T: The test or t-statistic is
( Slope_hat-null)  / SD

where Slope_hat is the 
sample slope.
null is 99.9% of time=0.

If they didn't give you
the slope, and they gave
you the data, use calcul.

If they didn't give you
the slope, but gave you
sy, sx, and r (correlation)
then slope =(sy*r)/sx

Plug t-score into calculator 
to get t-value and list it.

t_stat = xx

You are very unlikely to need
this but the standard error
for the slope is also
SE(b1)= S/ (sx*sqrt(n-1))
where sx is stdev x and S
is reported in the st dev
of residuals in the table.

O: Obtain p-value by looking 
t-val up in distribution!
Write 
or P(abs(t)>abs(t_stat))== XX 
Can also draw picture.

M: Make decision.

If p-value
is smaller than alpha 
(.05 often) then we REJECT 
the null. So REJECT if
t-stat is big and if
p-value is small.


FAIL TO REJECT if t-stat is
small and p-value is big.
Never accept null. Just can't
reject it. 

(Best guess is still 
sample slope not null)

State:
  We reject the null that
  the popul. least squares
  slope between "weight
  in grams and height
  in inches" equals 0.
  or
  We cannot reject 
  the null that
  the popul. least squares
  slope between "weight
  in grams and height
  in inches" equals 0.
*****************************
2) Chi-Squared: Goodness
*****************************
Need at least 3 categories
else do proportion

P:   
"The parameters of interest
are the POPULATION proportins 
of "green M&Ms" p1"
"blue M&Ms" p2 and
"yellow M&Ms" p3"

(I put in M&Ms to
remind you to give context)

H:  The null hypothesis is
         Ho:  p1=.5
              and
              p2=.3
              and 
              p3=.2
        
OFTEN IT IS :
    H0: p1=p2=p3

The alternate hypothesis is
          Ha: 
At least 1 pi is not equal
to the expected value.
      


A: "I assume the N observtion 
(M&Ms)
are a random sample 
with independent obs.
I assume sample<10% popultion

I CHECK that all BOXES have
an EXPECTED count of at
least 5"!!!

N: I will do a Chi-Sq test
of goodness of fit with
alpha =0.05.

Say DOF = #Groups-1

T: The test is sum of
( Observed - Expected)^2 / E

where expected =pi*N
where N is the total
number of M&Ms drawn.

Plug this into calculator to
get chi-sq value and list it.

chi-sq=xx

O: Obtain p-value from Calc.

Write 
P(x-sq>xx) == p_val

(ITS ONLY EVER GREATER HERE)

M: Make decision. 
If p-value
is smaller than alpha 
(.05 SAY) then we REJECT the
null. So REJECT if chi-sq is
big and if p-value is small.

FAIL TO REJECT if chi-sq is
small and p-value is big.
Never accept null. Just can't
reject it. 
Best guess is still
sample values.

State:
  We reject the null that
  all the population 
  proportions
  of "M&M colors" match
  the expected value.
  
  alternately if the null
  is all equal:
  
  We reject the null that
  all the population 
  proportions of "M&M colors"
  are equal.
  
  
  or
  
  We cannot reject the
  null assumption that
  all the population 
  proportions
  of "M&M colors" match
  the expected value.
  
*****************************
3) Chi-Squared:
Homogenous/Independence
*****************************
Need at least 3x2 categories
else do proportion

P: 
  
"The parameters of interest
are the POPULATION proportins 
of "green" for 
regular M&M p1_reg and
peanut M&M  p1_peanut

of "blue" for 
regular M&M p2_reg and
peanut M&M  p2_peanut

and

of "yellow" for 
regular M&M p3_reg and
peanut M&M  p3_peanut

(I put in M&Ms to
remind you to give context)

H:  The null hypothesis is
     Ho:   There is
     no difference in
     the proportions
     of "different
     colors" by type of
     "M&M".


The alternate hypothesis is
          Ha: 
    At least 1 proportion
    is not equal across
    types of "M&Ms".
      

A: "I assume the N  
observations (M&Ms)
are a random sample 
with independent obs.
I assume sample<10% populatin

I CHECK that all BOXES have
an EXPECTED count of at
least 5"!!!

N: I will do a Chi-Sq test
of goodness of fit with
alpha =0.05.

Say DOF =
(#Rows-1)*(#Column-1)

T: The test is sum of
(Observed - Expected)^2 /Exp

where expected =
row*_tot*colum_tot/total N

where N is the total
number of M&Ms drawn.

Plug this into calculator to
get chi-sq value and list it.

chi-sq=xx

O: Obtain p-value from Calc.

Write 
P(x-sq>xx) == p_val

(ITS ONLY EVER GREATER HERE)

M: Make decision. 
If p-value
is smaller than alpha 
(.05 say )then we REJECT the
null. So REJECT if chi-sq is
big and if p-value is small.

FAIL TO REJECT if chi-sq is
small and p-value is big.
Never accept null. Just can't
reject it. Best guess 
is still sample values.

State:
  We reject the null that
  all the population 
  proportions
  of "M&M colors" are the same
  for regular and peanut 
  M&Ms.
  
 
  
  or
  
  We cannot reject 
  the null that
  all the population 
  proportions
  of "M&M colors" are the same
  for regular and peanut 
  M&Ms.
