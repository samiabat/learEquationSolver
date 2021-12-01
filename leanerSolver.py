def lenearSolver(equation1, equation2):
    a, b, c, d, e, f = int(equation1[:equation1.find('x')]), int(equation1[equation1.find('+'):equation1.find('y')]),int(equation1[equation1.find('=')+1:]),int(equation2[:equation2.find('x')]),int(equation2[equation2.find('+'):equation2.find('y')]),int(equation1[equation2.find('=')+1:])
    x = ((c - b*f)/e) - (a - b*d /e)
    return "X = ", x , "Y =", (c - a * x)/b
print(lenearSolver(input(), input()))
