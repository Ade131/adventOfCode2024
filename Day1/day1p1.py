def read_and_parse_input(file_path):
    leftList = []
    rightList = []
    
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        parts = line.split("   ")
        if len(parts) >= 2:
            leftList.append(int(parts[0].strip()))
            rightList.append(int(parts[1].strip()))
    
    return leftList, rightList

def calculate_total_distance(leftList, rightList):
    leftList.sort()
    rightList.sort()
    
    totalDistance = 0
    for i in range(len(leftList)):
        totalDistance += abs(leftList[i] - rightList[i])
    
    return totalDistance

def main():
    leftList, rightList = read_and_parse_input("input.txt")
    totalDistance = calculate_total_distance(leftList, rightList)
    print("Total Distance: " + str(totalDistance))

if __name__ == "__main__":
    main()
