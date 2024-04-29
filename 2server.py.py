# Define two fuzzy sets
set1 = FuzzySet({"a": 0.8, "b": 0.6, "c": 0.4})
set2 = FuzzySet({"b": 0.7, "c": 0.3, "d": 0.9})

# Union
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Complement
complement_set = set1.complement()
print("Complement:", complement_set)

# Difference
difference_set = set1.difference(set2)
print("Difference:", difference_set)

# Cartesian product (fuzzy relation)
relation = FuzzyRelation.cartesian_product(set1, set2)
print("Fuzzy Relation (Cartesian Product):", relation)

# Max-min composition
other_relation = FuzzyRelation({("b", "x"): 0.5, ("c", "y"): 0.7, ("b", "y"): 0.2})
composition_result = relation.max_min_composition(other_relation)
print("Max-min Composition:", composition_result)
