

d= 3
c= 5


def sample_function(a: float=d, b: float=c) -> float:
    """_summary_

    _extended_summary_

    Parameters
    ----------
    a : float, optional
        _description_, by default d
    b : float, optional
        _description_, by default c

    Returns
    -------
    float
        _description_

    Raises
    ------
    ValueError
        _description_
    """
    val = a + b
    if a + b < 0:
        raise ValueError("Sum is negative")

a = 2
b = 3
print(sample_function(a, b))

print(sample_function(1,2))


print(sample_function(-10))



