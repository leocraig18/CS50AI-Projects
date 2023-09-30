import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    # Create an empty list to append probabilities to.
    person_probabilities = []

    # Iterate through each person in people dictionary.
    for person in people:
        if people[person]["mother"] is None and people[person]["father"] is None:
            if person in one_gene:
                genes = 1
                gene_probability = PROBS["gene"][1]
            elif person in two_genes:
                genes = 2
                gene_probability = PROBS["gene"][2]
            else:
                genes = 0
                gene_probability = PROBS["gene"][0]

        else:
            # Compute mothers gene inheritance probability.
            if people[person]["mother"] in one_gene:
                gene_from_mother = 0.5
                no_gene_from_mother = 0.5
            elif people[person]["mother"] in two_genes:
                gene_from_mother = 1 - PROBS["mutation"]
                no_gene_from_mother = PROBS["mutation"]
            else:
                gene_from_mother = PROBS["mutation"]
                no_gene_from_mother = 1 - PROBS["mutation"]

            # Compute fathers gene inheritance probability.
            if people[person]["father"] in one_gene:
                gene_from_father = 0.5
                no_gene_from_father = 0.5
            elif people[person]["father"] in two_genes:
                gene_from_father = 1 - PROBS["mutation"]
                no_gene_from_father = PROBS["mutation"]
            else:
                gene_from_father = PROBS["mutation"]
                no_gene_from_father = 1 - PROBS["mutation"]

            # Compute person gene prob based on parents genes.
            if person in one_gene:
                genes = 1
                gene_probability = (gene_from_father * no_gene_from_mother) + (no_gene_from_father * gene_from_mother)
            elif person in two_genes:
                genes = 2
                gene_probability = gene_from_father * gene_from_mother
            else:
                genes = 0
                gene_probability = no_gene_from_father * no_gene_from_mother

        # Compute trait probability:
        if person in have_trait:
            trait_probability = PROBS["trait"][genes][True]
        else:
            trait_probability = PROBS["trait"][genes][False]

        # Compute joint probability and append to list.
        person_joint_probability = gene_probability * trait_probability
        person_probabilities.append(person_joint_probability)

    # Calculate total join probability from items in list.
    total_joint_probability = 1
    for num in person_probabilities:
        total_joint_probability *= num

    return total_joint_probability


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        if person in one_gene:
            probabilities[person]["gene"][1] += p
        elif person in two_genes:
            probabilities[person]["gene"][2] += p
        else:
            probabilities[person]["gene"][0] += p

        if person in have_trait:
            probabilities[person]["trait"][True] += p
        else:
            probabilities[person]["trait"][False] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """

    # Iterate for sum of gene probabilities

    for person in probabilities:

        # Init some variables.
        sum_of_gene_probs = 0

        for gene_value in probabilities[person]['gene'].values():
            sum_of_gene_probs += gene_value

        # Calculate gene weighting 'a'.
        a_genes = 1 / sum_of_gene_probs

        # Apply weighting to each gene value probability.
        for gene_value in probabilities[person]['gene']:
            probabilities[person]['gene'][gene_value] *= a_genes

    # Same for trait probability.
    for person in probabilities:
        sum_of_trait_probs = 0
        for trait_value in probabilities[person]['trait'].values():
            sum_of_trait_probs += trait_value

        a_trait = 1 / sum_of_trait_probs

        for gene_value in probabilities[person]['trait']:
            probabilities[person]['trait'][gene_value] *= a_trait


if __name__ == "__main__":
    main()
