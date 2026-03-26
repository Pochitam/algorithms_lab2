def generate_rectangles(n, step): 
    rec = []
    for i in range(n):
        rec.extend([((step*i, step*i), (step*(2*n-i), step*(2*n-i)))])
    return rec

def generate_points(n, num_points, p_x: int = 1000000007, p_y: int = 1000000009):
    mx_diap = 20*n
    return [(pow(p_x, 31, mx_diap), pow(p_y, 31, mx_diap)) for i in range(num_points)]
