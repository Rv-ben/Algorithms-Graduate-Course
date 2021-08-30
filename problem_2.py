""" 1-to-2 PARTITION:
    Instance: A finite  set of positive  integers Z = { z1 , z2 , ... , zn }.
    Question: Is there a subset Z'of Zsuch that Sum of all numbers in Z'= 2 xSum  of all  numbers  in Z-Z'
        (a) Obtain  the  dynamic  programming  functional  equation  to  solve  the 1-to-2 PARTITION problem.
        (b) Give  an algorithm  to  implement  your  functional  equation.
        (c) Give  an  example  of  5  numbers  with  a  total  of  21 as  an  input  instance  for 1-to-2 PARTITION problem,  
            and  show how  your  algorithm  works on  this  input  instance.
        (d) What is  the complexity  of your  algorithm?
"""
from random import randint


def test(sum_of_z: int, sum_of_original):
    return (sum_of_z / 2) + sum_of_z == sum_of_original

def one_to_two_part(Z: list, sum_of_original: int, subsets: dict, solutions: list):

    N = len(Z)

    for i in range(N):
        subset = Z[0:i] + Z[i+1:N]
        subset_encoding = str(subset)
        
        # If we have never seen it before
        if not hasattr(subsets, subset_encoding):
            print(subset_encoding)
            subsets.update({subset_encoding: sum(subset)})

            # Test to see it is a solution
            if test(subsets[subset_encoding], sum_of_original):
                solutions.append(subset)
            
            # Test it's subsets
            one_to_two_part(subset, sum_of_original, subsets, solutions)


subsets = {}
solutions = []
set = [2, 2, 3, 1, 10]
set_sum = sum(set)
one_to_two_part(set, set_sum, subsets, solutions)

print(solutions)
