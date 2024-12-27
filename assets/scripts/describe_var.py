1) Describe 1 variable
2) Describing 2 Variables
including SLOPE,
correlation,and r-sq

*****************************
*****************************
* 1) Describing 1 Variable
*****************************
*****************************
SHAPE
* Descriptions of Shape ****
* Unimodal/ Bimodal
* Right & Left Skew,Symmetric

OUTLIER (if none say that!)
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

UNITS 
*What is X and what is Y?
*Explain units

**************************
Extra Vocab:

Percentile - where in order
 or % smaller than. So 28 
 percentile means bigger than
 28% of the data.

Quartile - 25, 50, and 75th
percentile

Z-Score = (X-Xbar)/SD

Outlier - x>75th +1.5*IQR or
          x<25th -1.5*IQR
      
5 Number Summary - 
Min, 25th, 50th, 75th, Max

Qualitative/Categorical -
variables you are or are not
"Blue" "American" 
You cannot have a value of 2.

Qualitative - can take number
values. Like weight or 
rebounds


*****************************
* 1 Variable Graphs

Boxplot - X-axis has to cover
range. Median is middle line.
Box goes from 25-75 perctile.
Whiskers are 75th+1.5*IQR
and 25th-1.5*IQR. Put dots
for outliers. UNLESS data
stops before outliers. Then
draw whiskers to end of data
only.

Stemplot- 

  | 0 | 2
0 | 1 | 5
24| 2 | 8
 
 means the left numbers are
 10, 22, 24 
 right numbers are
 2, 15, 28 
 
Cumulative Distribution -
 Percentiles on Y-Axis and
 X values on X-Axis.
 Tells you what % is below
 X.
 Median is X where Y=0.5 
 
Density Curve - a probability
curve. Always has a total
area of 1.
 
Histogram Example:

"The distribution of the 
sample of room sizes is 
bimodal and roughly symmetric 
with most room sizes
falling into two clusters: 
100 to 200 square feet and 
250 to 350 square feet. The 
median of the distribution 
is between 200 and 300 
square feet. The range of 
the  distribution is 
between 150 and 250 square 
feet. There  are no apparent
outliers."

Note it says square feet!
Note it doesn't precisely
say a median (gives range).
 
*****************************
*****************************
* 2) Describing 2 Variables
*****************************
*****************************
* Two Variables - X & Y
* D: Direction (+ -)
  U: Unusual features
     Outliers, gaps, clusters
  F: Form. Linear/Nonlinear
  S: Strength (Strong/Weak)
 + CONTEXT! Units.
*****************************

* Say four things
* 1) Positive or Negative
* 2) Strong or Weak
* 3) Clusters, Gaps, Outliers
* 4 Linear (straight line) or 
  non-linear (curve)
* 5) Units. What is X and what 
  is Y?

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
 MEASURES DIRECTION AND 
 STRENGTH of RELATIONSHIP.
 
 It is the sqrt(r^2) or
 the square root of 
 r-squared or the square
 root of the coefficient
 of determination!

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
* by the least-sq line with X

"The coefficient of 
determination is r2 ≈ 0.819.
This value indicates 
that 81.9% of the variation
in bullfrog mass can be 
explained by variation in
bullfrog length as 
described by the 
least-squares line.

IT IS CORRELATION SQUARED
r^2=r*r.

*****************************
******************************
* Interpretting a Regression.
*****************************
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

"A 1 millimeter increase
in length is associated 
with a 6.08 grams increase
in the predicted mass of a 
bullfrog"

********************
* Residual
********************

*A residual is the gap
*from the data point to the
*line. Can be + or -.

Diff between Y & prediction
*  residual= Y-Y_hat or 
* residual = Y-m*x -b
-->Y=Yhat+residual

weight = predict_w + residual

* Influential -- a data point
that strongly impacts the 
mean or slope.

* Leverage - how different is
the X variable from the rest
of the data.

* The "S" on a regression 
output is the avg. absolute
value of the residuals.

* Extrapolate -means predict
based on regression.
DO NOT EXTRAPOLATE far
beyond the Xs in the Data.

Normal Prob plot can tell
if residuals/data are normal.
Should be straight line up if
yes.

If asked to make linear say
put variable in logs or ln(x)
***************************
***************************
