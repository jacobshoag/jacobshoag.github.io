Type 1 Error is
rejecting a correct null.

Happens with prob alpha. 

alpha =0.05 means that if the 
null is true we'd still see
this X 5% of the time.

When we reject based on that,
we know if the null is true
we will reject 5% of the time.
So type 1 has prob alpha.

It is P(reject H0| H0 is true).
---------------------------
Type 2 Error is fail to reject a
wrong hypothesis.

It's  
P(FailtoReject|H0false or Ha)

So if I have H0 mu=25 and
Ha= mu>25 =bomb, then
Type I is a false alarm. 
Reject when only 25.

A Type 2 error is accept wrong
bomb is over 25 but fail to 
reject. 
Did not evacuate real bomb.

------------------------
Power = 1-P(Fail|Ha)

Power is odds of rejecting 
a false null. 
Power =1-P(Type 2 Error).

Power goes up when the null
is more wrong (mu gets
farther from null). It 
goes up when alpha goes up
(from 0.05 to 0.1). It goes
up when the sample size goes
up.
