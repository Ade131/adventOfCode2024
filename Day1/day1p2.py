from day1p1 import read_and_parse_input, calculate_total_distance
from collections import Counter

def calculate_similarity_score(leftList, rightList):
    right_counts = Counter(rightList)
    similarity_score = 0
    for num in leftList:
        similarity_score += num * right_counts.get(num, 0)
    return similarity_score

def main():
    leftList, rightList = read_and_parse_input("input.txt")
    totalDistance = calculate_total_distance(leftList, rightList)
    print("Total Distance: " + str(totalDistance))
    
    similarity_score = calculate_similarity_score(leftList, rightList)
    print("Similarity Score: " + str(similarity_score))

if __name__ == "__main__":
    main()
