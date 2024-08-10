def calculate_average(scores):
    """Calculate the average of a list of scores."""
    return sum(scores) / len(scores) if scores else 0

def main():
    scores = list(map(int, input("Enter scores separated by space: ").split()))
    average = calculate_average(scores)
    print(f"Average Score: {average}")

if __name__ == "__main__":
    main()
