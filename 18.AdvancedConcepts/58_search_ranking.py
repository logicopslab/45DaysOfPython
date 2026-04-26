# search_ranking.py

def calculate_score(text, query_words):
    score = 0
    words = text.lower().split()

    for q in query_words:
        score += words.count(q)

    return score


def search(data, query):
    query_words = query.lower().split()
    results = []

    for item in data:
        score = calculate_score(item, query_words)

        if score > 0:
            results.append((item, score))

    # Sort by score (highest first)
    results.sort(key=lambda x: x[1], reverse=True)

    return results


def display_results(results):
    print("\nSearch Results:")
    for item, score in results:
        print(f"[Score: {score}] {item}")


def main():
    data = [
        "Python is great for backend development",
        "DevOps uses Python for automation",
        "Machine learning with Python is powerful",
        "Java is also used in backend systems"
    ]

    query = input("Enter search query: ")

    results = search(data, query)

    if results:
        display_results(results)
    else:
        print("No results found")


main()