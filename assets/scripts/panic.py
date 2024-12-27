* For Confidence Intervals
* 1) One Mean
* 2) One Proportion
* 3) Two Means- Difference
* 4) Two Proportion -Diff
* 5) Slope
******************************
1) One Mean
******************************
P: "The parameter of interest
is the POPULATION mean "weight
in grams" mu"

A: "I assume a simple random
sample with independent obs.
and a sample size>30. 

ONLY if N<30
If the sample size is <30 
we assume or check that the 
sample looks roughly symmetric 
with no  outliers. If so we 
assume that the population is 
roughly  normal."

N: We will do a 1-sample mean 
Z or  T  90/95/99% Conf. intvl. 

Use T if possible.
If using T, say the degrees of
freedom = N-1 where N is sample
size.

I: The interval is 
sample mean +/- t_star * SD
S = sigma of pop/ sqrt(n)
So 
Margin of Error = t_star* SD
ME = t_star*sigma/sqrt(n)

use s instead of sigma in
formula if from sample

List the interval points.

* If using Z its usually
1.64 for 90%
1.96 for 95%
2.58 for 99%

The t-numbers should be a 
bit bigger. Worse case use 
Z if you need.

C: 
"We are 95% confident that
the population "mean weight 
in grams" is in the interval
[xx to xx]."

If a null/guess is in this 
interval there is not
compelling evidence to reject. 
If a null/guess is outside the
interval there is evidence to
reject it.
******************************
2) One Proportion
******************************
P: "The parameter of interest
is the POPULATION proportion 
of "people who voted" p"

A: "I assume a simple random
sample with independent obs.
I assume sample<10% population.
I check n*p>10 and n*(1-p)>10."

If not think about a binomial 
instead.

N: I do a 1-sample proportion 
Z  90/95/99% Conf. Intvl. 

I: The interval is 
sample mean +/- z_star * SD
S = sqrt[p*(1-p)/n]
So 
Margin of Error = z_star* SD
ME = z_star*sqrt[p*(1-p)/n]

List the interval points.

* If using Z its usually
1.65 for 90%
1.96 for 95%
2.58 for 99%

C: 
"We are 95% confident that
the population proportion
of "people who voted" is in the 
interval [xx to xx]."

If a null/guess is in this 
interval there is not
compelling evidence to reject. 

If a null/guess is outside the
interval there is evidence to
reject it.

******************************
3) Two Means
******************************
P: "The parameter of interest
is the POPULATION difference
in mean "weight in grams" 
mu1- mu2"

A: "I assume a simple random
sample with independent obs.
and a sample size n1>30 and
n2>30. 

ONLY if N1 or N2 <30
If the sample size is <30 
we assume or check that the 
sample looks roughly symmetric 
with no  outliers. If so we 
assume that the population is 
roughly  normal."

N: We will do a 2-sample mean 
Z or  T  90/95/99% Conf. intvl. 

Use T if possible.
If using T, say the degrees of
freedom = N1+N2-2 where 
N1 and N2 are the 2 sample
sizes.

I: The interval is 
sample Difference in means:
(mu1-mu2) +/- t_star * SD

SD = 
sqrt[sigma_1^2/n1 +sigma_2^2/n2]

Remember you need to square the
sigmas and divide by n1 and n2
and then square root. Can't add
sigmas! Use s rather than
sigma in formula if from 
sample.
  
Margin of Error = t_star* SD
ME = 
t_star*sqrt[sig1^2/n1+sig2^2/n2]

List the interval points.

* If using Z its usually
1.64 for 90%
1.96 for 95%
2.58 for 99%

The t-numbers should be a 
bit bigger. Worse case use 
Z if you need for partial cred.


C: 
"We are 95% confident that
the population difference in
mean "weights in grams" 
is in the
interval [xx to xx]."

If a null/guess is in this 
interval there is not
compelling evidence to reject. 

If a null/guess is outside the
interval there is evidence to
reject it.

******************************
4) Two Proportions
******************************
P: "The parameter of interest
is the POPULATION difference
in the proportion of people 
"who vote" p1- p2"

A: "I assume a simple random
sample with independent obs.
I assume both samples<10% 
population.

Check n*p1>10 and n*(1-p1)>10
Check n*p2>10 and n(1-p2)>10."

If not, think about a binomial
instead.

N: We will do a 2-sample proport 
Z 90/95/99% Conf. intvl. 

I: The interval is 
sample Difference in means:
(p1-p2) +/- z_star * SD

SD = 
sqrt[p1(1-p1)/n1 +p2*(11-p2)/n2]

Remember you need to add inside 
the square root. Can't add
sigmas!
  
Margin of Error = z_star* SD
ME = 
z_star*
sqrt[p1(1-p1)/n1 +p2*(1-p2)/n2]

List the interval points.

* If using Z its usually
1.64 for 90%
1.96 for 95%
2.58 for 99%

C: 
"We are 95% confident that
the population difference in
proportion of "people who vote"
is in the interval [xx to xx]."

If a null/guess is in this 
interval there is not
compelling evidence to reject. 

If a null/guess is outside the
interval there is evidence to
reject it.


******************************
5) SLOPE
******************************
P: "The parameter of interest
is the least-square SLOPE b1=m
between "weight in grams" (X)
and "height in inches" (Y)"

A: "I assume a simple random
sample with independent obs.
I assume the relationship
between X and Y is roughly
linear. I assume the residuals
are roughly normal and would 
want to check a normal prob
plot. We also assume that error
is homoskedastic-same size in 
absolute value for any X."


N: We will do a 1-sample slope 
T  90/95/99% Conf. intvl. 

Use T if possible.
If using T, say the degrees of
freedom = N-2 where 
N is the sample size.

YOU WILL NEED TO LOOK UP T
IN THE DISTRIBUTION SIDE. DO
T-Distr with N-2 DOF and CHOOSE
90/95/99% Area and let it find
-T and T. That's the T. 
Should be bigger than 
1.64/1.96/2.58

I: The interval is 
sample slope b1_hat +/- 
t_star * SE

SE = Whatever it says next 
to the slope in 2nd column. 
No dividing by N!

Margin of Error = t_star* SE

ME = 
t_star*Whatever the 2nd number 
by slope is.

List the interval points.

* If using Z its usually
1.64 for 90%
1.96 for 95%
2.58 for 99%

The t-numbers should be a 
bit bigger. Worse case use 
Z if you need

C: 
"We are 95% confident that
the population slope of the 
least-squares line between  X 
and Y defined above is in the 
interval [xx to xx]."

If a null/guess is in this 
interval there is not
compelling evidence to reject. 

If a null/guess is outside the
interval there is evidence to
reject it.
