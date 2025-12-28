# Aproxima raízes de reais não negativos com margem de erro especificada em um máximo de iterações

def square_root_bisection(value, tolerance = 0.001, it_max = 50):
    if value < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif value == 0 or value == 1:
        print(f"The square root of {value} is {value}")
        return value
    else:
        root = value/(1/(tolerance))
        for i in range(1, it_max):
            root = (value+root**2)/(2*root)
        if abs(root - value**0.5) <= tolerance:
            print(f"The square root of {value} is approximately {root}")
            return root
        else:
            print(f"Failed to converge within {it_max} iterations")
            return None
