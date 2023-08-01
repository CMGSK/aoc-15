# Solved by reasoning
# clearly the password must match two pair of letters and a three letter consecutive chain.
# since closest password will be editing as few digits to the right as possible,
# we are looking for a pattern in which we see an XXYZZ pattern
# therefore, from 'hxbxwxba' input, closest is hxbx (fixed) then the same last letter, x, then the pattern
# from x, yzz.
#
# First result hxbxxyzz.
#
# The second comes to the same thing, we gotta increase the letters, then coil them around the rules.
# increasing z we cant get our pattern right so closest will be cc, therefore, previous letter will be b,
# and previous to this, two a. Since we cant increase the letter up to a, we increase
# the fifth letter from the last position.
#
# Second result hxcaabcc.


