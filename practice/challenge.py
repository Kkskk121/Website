def solution(area):
    # Your code here
    squares = generateSq(area)
    panels = []
    for i in range(len(squares) - 1, -1,-1):
        if area%squares[i] == 0:
            panels = panels + [squares[i]] * (area/squares[i])
            return panels
        
        else:
            panels = panels + [squares[i]] * (area//squares[i])
            area = area - (squares[i] * (area//squares[i]))
            print(area)
            



def generateSq(limit):
    i = 1
    squares = []
    while i**2 <= limit:
        squares.append(i**2)
        i+=1
    return squares
        
print(solution(5686))