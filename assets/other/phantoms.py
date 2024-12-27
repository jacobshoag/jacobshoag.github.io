# Type your text here******************************
*  Hypothesis Testing
* ( from a sample n>1 )
* 1) One Mean
* 2) One Proportion
* 3) Two Means- Difference
* 4) Two Proportion -Diff

P. state pop parameter
H. state hypothesis
A. state assumptions
N. name test
T. calc z/t-statistic
O. obtain p-val
M. make reject/ fail to reject
   decision
S: state conlusion in context
******************************
1) One Mean
******************************
P: "The parameter of interest
is the POPULATION mean "weight
in grams" mu"

(I put weight in grams to
remind you to say units)

H:  The null hypothesis is
         Ho:  mu=xx
The alternate hypothesis is
          Ha: mu>xx 
      
(or less than or not equal 
in Ha: as needed) 

A: Independent obs, 
simple random sample,
N>30.

ONLY if N<30
If the sample size is <30 
we assume or check that the 
sample looks roughly symmetric 
with no  outliers. If so we 
assume that the POPULATION is 
roughly  normal."

(reminder can do hypotehsis
test with normal pop even
with small sample)

N: We will do a 1-sample mean 
Z or  T  test with 
significance level alpha
(alpha = 0.05)  

Use T if possible!

If using T, say the degrees of
freedom = N-1 where N is sample
size.

T: The test or t-statistic is
( X_bar - mu0) / SD

where X_bar is the sample mean
mu0 is the null hypothesis
SD = sigma/sqrt(n)  
use s if from sample
or if they didn't give it
SD = 
sqrt( (1/n-1) *sum [x-xbar]^2) 

Plug this into calculator to
get t-value and list it.

t_stat = xx

O: Obtain p-value by looking 
t-val up in distribution!
Write 
P(t>t_stat) == p_val
or P(t<t_stat) == p_val 
or P(abs(t)>abs(t_stat)) == p_val 
as case may be. Can also
draw picture.

M: Make decision.

If p-value
is smaller than alpha 
(.05 often) then we REJECT the
null. So REJECT if t-stat is
bigger than cutoff
and if p-val is smaller.


FAIL TO REJECT if t-stat is
smaller than cutoff and p-val 
is bigger.

Never accept. Just can't
reject. 

(Best guess is still 
sample mean not null)

State:
  We reject the null that
  the popul. mean "weight
  in grams" equals xx.
  or
  We cannot reject the 
  null that the 
  population mean
  "weight in grams" equal xx.
******************************
2) One Proportion
******************************
P: "The parameter of interest
is the POPULATION proportion 
of "people who voted" p"

(I put people who voted
remind you to say units)

H:  The null hypothesis is
         Ho:  p=0.xx
The alternate hypothesis is
          Ha: p>0.xx
      
(or less than or not equal 
in Ha: as needed) 

A: "I assume a simple random
sample with independent obs.
I assume sample<10% population.
I check n*p>10 and n*(1-p)>10."

If not think about a binomial 
instead.

N: I do a 1-sample proportion 
Z test w signifigance
level alpha=.01

T: The test or z-statistic is
( p_hat - p0) / SD

where p_hat is the sample
proportion and
p0 is the null hypothesis
SD = sqrt[p0*(1-p0)/n]

Plug this into calculator to
get z-value and list it.

z_stat = xx

O: Obtain p-value by looking 
z-val up in distribution!
Write 
P(z>z_stat) == p_val
or P(z<z_stat) == p_val 
or P(abs(z)>abs(z_stat))=p_val 
as case may be. Can also
draw picture.

M: Make decision. 

If p-value
is smaller than alpha 
(.05 often) then we REJECT the
null. So REJECT if z-stat is
biger than cutoff and if 
p-val is smaller.

FAIL TO REJECT if z-stat is
smaller than cutoff and p-val
is biger.

Never accept. Just can't
reject. Best guess is still
sample proportion.

State:
  We reject the null that
  the population proportion
  of "people voting" is
  xx.
  or
  We cannot reject the 
  null that the population
  proportion of
  "people voting" is xx.

******************************
3) Difference in Means
******************************
P: "The parameter of interest
is the POPULATION DIFFERENCE
in mean "recovery time"
between "new surgery" (mu_new) 
and "old surgery" (mu_old)" 

(I put recovery time 
and old/new for groups1,2 to
remind you to say units
and be careful about
direction.)

H:  The null hypothesis is
      Ho:  mu_new-mu_old=0
The alternate hypothesis is
      Ha: mu_new-mu_old <0 
      
(or greater than or not equal 
in Ha: as needed.) 

A: Independent obs for both, 
data from both groups is
simple random sample,
N1>30 and N2>30.

ONLY if N<30
If the sample size is <30 
for either
we assume or check that the 
sample looks roughly 
symmetric 
with no  outliers. If so we 
assume that the POPULATION is 
roughly  normal."

(reminder can do hypothesis
test with small sample if
pop is normal.)

N: We will do a 2-sample
difference in means 
Z or  T  test with 
significance level alpha
(alpha = 0.05)  

Use T if possible!

If using T, say the degrees 
of freedom = N1+N2-2 where 
N1 and N2 are sample sizes.

T: The test or t-statistic is
((X1_bar-X2_bar)-(mu1-mu2))/
SD

where X1_bar and X2_bar are 
the sample means. If just
given a difference plug 
in that.

mu1-mu2 is the null 
hypothesis difference. 
almost always zero.

So if null is zero:
t=(X1_bar-X2_bar)/SD

SD = 
sqrt[(sig1^2/n1)+(sig2^2/n2)]   
if you know the pop. sigma.
OTHERWISE use s instead of
sigma.

Plug this into calculator to
get t-value and list it.

t_stat = xx

O: Obtain p-value by looking 
t-val up in distribution!
Write the whole line:
P(t>t_stat) == p_val
or P(t<t_stat) == p_val 
or P(abs(t)>abs(t_stat))== p_val 
as case may be. Can also
draw picture.

M: Make decision.

If p-value
is smaller than alpha 
(.05 often) then we REJECT the
null. So REJECT if t-stat is
biger than cutoff and 
p-val is smaller.

FAIL TO REJECT if t-stat is
smaller than cutoff and p-val
is bigger.
Never accept. Just can't
reject it. Best guess is still
sample diff.

State:
  We reject the null that
  the population difference
  in mean "weight in grams"
  for group1 and group2
  equals 0.
  or
  We cannot reject the 
  null that the population 
  difference in mean 
  "weight in grams" for 
  group1 and group2.
  
  
 ******************************
4) Two Proportions
******************************
P: "The parameter of interest
is the Difference in
POPULATION proportion2 
of "people who voted" in 
group1 (p1) versus group2 (p2)


(I put people who voted
remind you to say units)

H:  The null hypothesis is
         Ho:  p1-p2=0.xx
The alternate hypothesis is
          Ha: p1-p2>0.xx 
      
(or less than or not equal 
in Ha: as needed) 


A: "I assume a both are 
simple random sample 
with independent obs.
I assume for both 
sample<10% population.
I check n*p1>10 and 
n*(1-p1)>10."
I check n*p2>10 and 
n*(1-p2)>10."

If not think about a binomial 
instead.

N: I do a 2-sample 
difference in proportions 
Z test w signifigance
level alpha=.01

T: The test or z-statistic is
(p1_hat-p2_hat -(p1-p2))/ SD

where p1_hat and p2_hat are 
the sample proportions. 
If just given a difference 
plug in that.

p1-p2 is the null 
hypothesis difference. 
almost always zero. If its
zero calculate
p_pool=
(Grp1Yes+Grp2Yes)/(n1+n2)

So if null is zero:
z=(p1_hat-p2_hat)/SD
where
SD=
sqrt[p_pool(1-p_pool)/n1+
p_pool(1-p_pool)/n2]

(if null isnt zero then
use sqrt[p01(1-p01)/n1+
p02(1-p02)/n2])
------
Plug this into calculator to
get z-value and list it.

z_stat = xx

O: Obtain p-value by looking 
z-val up in distribution!
Write 
P(z>z_stat) == pval
or P(z<z_stat) == pval 
or P(abs(z)>abs(z_stat))=pval 
as case may be. Can also
draw picture.

M: Make decision. 

If p-value
is smaller than alpha 
(.05 often) then we REJECT the
null. So REJECT if z-stat is
bigger than cutoff and if
p-val is smaller.

FAIL TO REJECT if z-stat is
smaller than cutoff and pval
is bigger.
Never accept. Just can't
reject. Best guess still
sample diff.

State:
  We reject the null that
  the population difference
  in proportion
  of "people voting" between
  group1 and group2 is
  0.
  
  or
  We reject the null that
  the population difference
  in proportion
  of "people voting" between
  group1 and group2 is
  0.