def gen_bin_tree(height: int, root: int):
    tree = {str(root): []}
    left_func = lambda root: root * 4
    right_func = lambda root: root + 1

    if ((abs(height) != height) or (abs(root) != root)):
        return "Height or root must be a non-negative integer"
    elif type(height) != int or type(root) != int:
        return "Height or root must be an integer value"
    else:
        if (height == 0):
            return tree
        else:
            l_l = left_func(root)
            r_l = right_func(root)
            print(l_l, r_l)
            a = gen_bin_tree(root=l_l, height=height - 1)
            tree[str(root)].append(a)
            b = gen_bin_tree(root=r_l, height=height - 1)
            tree[str(root)].append(b)
        return tree
