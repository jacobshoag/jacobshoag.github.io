 Purchase
NumWorks
Calculator
Emulator
Educators
Support
 Jacob
Explore
My scripts
Calculator
variable_descibe.py

This script is private

Created on April 30, 2023

6.92 KB


 


1) Describing 1 Variable
2) Describing 2 Variables

*****************************
*****************************
* 1) Describing 1 Variable
*****************************
*****************************
U-SOCS

UNITS 
*What is X ?
*Explain units

SHAPE
* Descriptions of Shape ****
* Unimodal/ Bimodal
* Right or Left Skew, Symmetric

OUTLIER
* Outliers. Gaps. 
* Clusters - like bunches

CENTER
* Mean or Median or Mode 
* Mode is most common

SPREAD
*Range (Max-Min).
 * Range is diffrence 
 * Not interval. So 4,6,9,3, 
 * has a range of 9-3=6 NOT
 * 9 to 3
 DO SUBTRACTION!
 
*IQR 75-25th% 
*Again do SUBTRACTION 
not interval!

*Standard Deviation is 
a spread too

*******************************
Extra Vocab:

Percentile - where in order
 or % smaller than. So 28 
 percentile means bigger than
 28% of the data.

Quartile - 25, 50, and 75th
percentile. Written Q1,Q2,Q3.

Z-Score = (X-Xbar)/SD

Outlier - x>75th +1.5*IQR or
          x<25th -1.5*IQR
*****************************
* 1 Variable Graphs

Boxplot - X-axis has to cover
range. Median is middle line.
Box goes from 25-75 perctile.
Whiskers are 75th+1.5*IQR
and 25th-1.5*IQR. Put dots
for outliers.

Stemplot- 

  | 0 | 2
0 | 1 | 5
24| 2 | 8
 
 means the left numbers are
 10, 22, 24 
 right numbers are
 2, 15, 28 
 
 
*****************************
*****************************
* 2) Describing 2 Variables
*****************************
*****************************
* Two Variables - X & Y
U-DUFS
  U: UNITS
* D: Direction (+ -)
  U: Unusual features
     Outliers, gaps, clusters
  F: Form. Linear/Nonlinear
  S: Strength (Strong/Weak)
 + CONTEXT.
*****************************

* Say five things:
* 1) Units. Define X and Y
* 2) Positive or Negative
* 3) Strong or Weak
* 4) Clusters or Large outliers
* 5 Linear (straight line) or 
  non-linear (curve)


"The scatterplot reveals a 
strong, positive, roughly linear 
association between the mass 
and length of bullfrogs. There 
are no points that seriously 
from the straight-line pattern 
of the points in the plot."

Definitions:
* Positive means: X up = Y up
* Negative means: X up= Ydown
* Linear means constant slope
* Strong=High R-squared. Most
* of variance explained by 
* relationship. 
* Weak= Most of variance of
  Y not explained by line.

*******************************
Extra Vocab:

Correlation (r) - between
 -1 and 1. Farther from zero
 is a stronger relationship.
Does not change when
you multiply or add to 
X & Y.

Dependent Variable - Y var.
Variable on left-hand side

Independent Variable - X var.
Variable on right-hand side

****************************
* Interpretting the R-Squared
* R2 is also called the
* Coefficient of 
  Determination
****************************

*This is the % of variation
*in Y that can be explained
* by the % variation in X

"The coefficient of 
determination is r2 ≈ 0.819.
This value indicates 
that 81.9% of the variation
in bullfrog mass can be 
explained by variation in
bullfrog length as 
described by the 
least-squares line.

*****************************


********************************
* Interpretting a Regression.
********************************
y_triangle_on_top = b0+b1*X 

b0: this is the intercept
it is the predicted value
of Y when X=0.

b1: this is the slope.
it was calculated by finding
the value that minimizes the
sum of squared residuals.

"A 1 unit increase in X
is associated with a b1
unit increase in the
predicted value of Y"

" The predicted mass of a 
bullfrog increases by
6.086 grams for each 
additional millimeter of
length. "

"

********************
* Residual
********************

*A residual is the gap
*from the data point to the
*line. Can be + or -.
*Diff between Y & prediction
* residual= Y-Y_hat or 
* residual = Y-m*x -b


* Influential -- a data point
that strongly impacts the 
mean or slope.

* Leverage - how different is
the X variable from the rest
of the data.

***************************
***************************
* Experimental Design
***************************
***************************
* Treatments: Placebo, Drug

* Factor: Levels of the Drug
Like how many grams

* Experimental Units: 
  People or Classes or what
  gets assigned to a treatment
  
* Response Variable: What gets
impacted. Like your weight 

******************************
* Matched Pair- Like Identical
*Twins
*****************************
This improves the precision
of estimated treatment impact
because it lowers variation
due to other factors like
your starting weight


****************************
* Five Number summary *
****************************
* Min, 25th% , 50th%, 75%, Max
******************************

 
*****************************
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

if we changed the payouts by +10
1/6*11 + 4/6*12+ 1/6*16 = 2.5+10
=12.5

Or if we changed them by -.5
1/6*.5 + 4/6*1.5 +1/6*5.5 =
2.5-.5 = 2

* VAR AND StdDev DO NOT CHANGE
* IF YOU JUST ADD OR SUBTRACT
* They Do IF YOU MULTIPLY THOUGH

Multiply all numbers by 10
E[10*X] = 10*E[X]
1/6*10 + 4/6*20 +1/6*60=25

Variance is now 10^2 *var(x) or
100*Var(x)

SD is 10*SD though. 
Z or T score wouldn't change
****************************

****************************
***************************
* ADDING INDP RANDOM VARIABLES**
******************************
* What About X+Y 
* ONLY IF INDEPENDENT!!!
* E(X+Y) or mean(X+Y)=
E(X) + E(Y) or mean(X) + mean(Y)
********************************
* ONLY IF INDEPENDENT!!!
* Var(X+Y) = Var(X) + Var(Y)
*BUT SD(X+Y) is not! sd(x)+sd(y)
* It is sqrt[Var(X)+ Var(Y)]
******************************
******************************
* PROBABILITY RULES
******************************
******************************
* P(A and B) = P(A|B)*P(B) and
* P(A and B) = P(B|A)*P(A) 

So:
* P(B|A)*P(A) = P(A|B)*P(B)
where P(A|B) means P(A given B).
Also:
* P(B|A) = P(A and B)/ P(A)
* Above is TRUE EVEN IF NOT INDP
*******************************
*******************************
* INDEPENDENT MEANS
P(A|B) = P(A) or P(B|A)=P(B)
or P(A|B)=P(A|B_complement)
(Can use to check independence)

IF INDEPENDENT THEN:
P(A and B) = P(A)*P(B).
(Another way to check indp).

Independent cant be mutually
exclusive. Mutually exclusive is
P(B|A) =0. Because P(A and B)=0.
Sometimes mutually exclusive is
called disjoint.

Also we always have
P(A or B)= P(A)+P(B)-P(A and B)
if indp P(A and B)=P(A)*P(B)
if mutually exclusive its A&B=0.

**** U SMILEY FACE
P(A u B) = P (A or B)

**** FROWNY FACE UPSIDE DOWN U 
P(A frown u B) =P (A and B)
