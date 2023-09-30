import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    proba_dist = {}
    links = len(corpus[page])

    if links:
        for key in corpus:
            proba_dist[key] = (1 - damping_factor) / len(corpus)
        for key in corpus[page]:
            proba_dist[key] += damping_factor / links
    else:
        for key in corpus:
            proba_dist[key] = 1 / len(corpus)

    return proba_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1
    """
    page_visits = {page_name: 0 for page_name in corpus}

    page = None

    for i in range(n):
        if not page:
            page = random.choice(list(corpus.keys()))
            page_visits[page] += 1
        else:
            current_distribution = transition_model(corpus, page, damping_factor)
            choices = list(current_distribution.keys())
            weights = [current_distribution[key] for key in choices]
            page = random.choices(choices, weights).pop()
            page_visits[page] += 1

    page_visits = {key: (value / n) for key, value in page_visits.items()}
    return page_visits


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.
    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    num_pages = len(corpus)
    init_rank = 1 / num_pages
    random_choice_prob = (1 - damping_factor) / len(corpus)

    # Initial page_rank
    page_ranks = {page_name: init_rank for page_name in corpus}
    new_ranks = {page_name: None for page_name in corpus}
    max_rank_change = init_rank

    # Iteratively calculate page rank until no change > 0.001
    while max_rank_change > 0.001:

        max_rank_change = 0

        for page_name in corpus:
            surf_choice_prob = 0
            for other_page in corpus:
                # If other page has no links pick a random page.
                if len(corpus[other_page]) == 0:
                    surf_choice_prob += page_ranks[other_page] * init_rank
                # Else if other_page has a link to page_name/s, it randomly picks from all links on other_page:
                elif page_name in corpus[other_page]:
                    surf_choice_prob += page_ranks[other_page] / len(corpus[other_page])
            # Calculate new page rank
            new_rank = random_choice_prob + (damping_factor * surf_choice_prob)
            new_ranks[page_name] = new_rank

        # Normalise the new page ranks:
        norm_factor = sum(new_ranks.values())
        new_ranks = {page: (rank / norm_factor) for page, rank in new_ranks.items()}

        # Find max change in page rank:
        for page_name in corpus:
            rank_change = abs(page_ranks[page_name] - new_ranks[page_name])
            if rank_change > max_rank_change:
                max_rank_change = rank_change

        # Update page ranks to the new ranks:
        page_ranks = new_ranks.copy()

    return page_ranks


if __name__ == "__main__":
    main()
