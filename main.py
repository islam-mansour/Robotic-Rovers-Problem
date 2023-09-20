import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--tests-file', metavar='tests_file', required=True, help='the path to test cases file')

def read_test_case(_file):
    try:
        x, y, dir = _file.readline().split()
        x, y = int(x), int(y)
        instructions = _file.readline().split()
        return x, y, dir, instructions
    except:
        exit() ## end of file, terminate


if __name__ == '__main__':

    args = parser.parse_args()

    test_cases_dir = args.tests_file
    _file = open(test_cases_dir, 'r')

    upper_x, upper_y = map(int, _file.readline().split())
    
    if upper_x < 0 or upper_y < 0:
        print("upper coordinates can't be less than zero")

    directions = ['N', 'E', 'S', 'W']
    change = [(0,1), (1,0), (0,-1), (-1,0)]

    while True:
        x, y, dir, instructions = read_test_case(_file)

        if x < 0 or x > upper_x or y < 0 or y > upper_y:
            print("Wrong coordinates")
            continue

        try:
            i = directions.index(dir)
        except:
            print("Direction doesn't exist")
            continue

        for instruction in instructions:
            if instruction == 'M':
                if x+change[i][0] not in range(0, upper_x+1) or y+change[i][1] not in range(0, upper_y+1):
                    #Can't move to this directions as it leads to out of bounds
                    pass
                else:
                    x += change[i][0]
                    y += change[i][1]
            elif instruction == 'L':
                i = i-1 if i!=0 else 3
            elif instruction == 'R':
                i = i+1 if i!=3 else 0
            else:
                #instruction doesn't exist
                pass

        print(x, y, directions[i])
                
            
        


