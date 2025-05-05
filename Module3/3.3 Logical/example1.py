# The negation of a conjunction is the disjunction of the negations.

# The negation of a disjunction is the conjunction of the negations.
p=False
q=False

not (p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)

