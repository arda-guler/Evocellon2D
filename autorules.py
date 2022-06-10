import random as rng
import math

def get_state(cell):
    try:
        if cell.state:
            return cell.state
        else:
            return False
    except:
        return False

def rand_init():
    if rng.uniform(0, 1) < 0.7:
        return False
    else:
        return True

def game_of_life(t, c, n1, n2, n3, n4, n5, n6, n7, n8):
    sc = c.state

    s1 = get_state(n1)
    s2 = get_state(n2)
    s3 = get_state(n3)
    s4 = get_state(n4)
    s5 = get_state(n5)
    s6 = get_state(n6)
    s7 = get_state(n7)
    s8 = get_state(n8)

    sn = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8

    if sc:
        if sn < 2:
            return False
        elif 2 <= sn <= 3:
            return True
        elif 4 < sn:
            return False

    else:
        if sn == 3:
            return True
        else:
            return False

# Example for a time-based algorithm
def trigoperiodic(t, c, n1, n2, n3, n4, n5, n6, n7, n8):
    sc = c.state
    x = c.index[0]
    y = c.index[1]
    
    if abs(math.cos(t/10) * 1000) < (x**2 + y**2) < abs(math.sin(t/10) * 1000):
        return True
    else:
        return False

def day_n_night(t, c, n1, n2, n3, n4, n5, n6, n7, n8):
    sc = c.state

    s1 = get_state(n1)
    s2 = get_state(n2)
    s3 = get_state(n3)
    s4 = get_state(n4)
    s5 = get_state(n5)
    s6 = get_state(n6)
    s7 = get_state(n7)
    s8 = get_state(n8)

    sn = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8

    if not sc:
        if sn == 3 or sn == 6 or sn == 7 or sn == 8:
            return True
        else:
            return False

    else:
        if sn == 3 or sn == 4 or sn == 6 or sn == 7 or sn == 8:
            return True
        else:
            return False

    
