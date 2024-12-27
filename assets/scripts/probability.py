**************************
* PROBABILITY RULES
**************************
 P(A and B) = P(A|B)*P(B)
 also = P(B|A)*P(A) 
So:
 P(B|A)*P(A) = P(A|B)*P(B)
where P(A|B) means P(A given B).

Also:
 P(B|A) = P(A and B)/ P(A)
 That's TRUE EVEN IF NOT INDP
***************************
* INDEPENDENT MEANS
P(A|B) = P(A) or P(B|A)=P(B)
or P(A|B)=P(A|B_complement)
(Can use to check independence)

IF INDEPENDENT THEN:
P(A and B) = P(A)*P(B).
(Another way to check indp).

Independent cant be mutually
exclusive. Mutually exclusive 
is P(B|A) =0. 
Because P(A and B)=0.
Sometimes mutually exclusive 
is called disjoint.

Also we always have
P(A or B)= P(A)+P(B)-P(A and B)
if indp P(A and B)=P(A)*P(B)
if mutually exclusive 
its A&B=0.

**** U SMILEY FACE
P(A u B) = P (A or B)

**** FROWNY FACE UPSIDE DOWN U 
P(A frown u B) =P (A and B)
---
Tree diagram. Every fork has
to have probab over branches
add to 1. Multiply down tree
to get prob at end. Prob at 
the end have to sum to 1.
100 people into tree=100 peep
at bottom.
---
To find prob(HIV|PosTest)=
p(HIV+PosTest)/
[p(HIV+PosTest)+p(NoHIV+PosTest)]
---
Remember E[#ATM|ATM>1] have to
change probs. Sum up the 
probabilities where ATM>1
and then divide each one
by this total. Probilities 
in E[X] need to sum to 1.
