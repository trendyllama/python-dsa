from TreeNode import TreeNode


def dfs(root: TreeNode, target, path: tuple = ()) -> tuple | None:
    """
    Example:
    >>> root = TreeNode("A")
    >>> two = TreeNode("B")
    >>> three = TreeNode("C")
    >>> root.children = [three, two]
    >>> path = dfs(root, "C")
    >>> print(path)
    (A, C)
    >>> path = dfs(root, "D")
    >>> print(path)
    None

    """
    path = path + (root,)

    if root.value == target:
        return path

    for child in root.children:
        path_found = dfs(child, target, path)

        if path_found is not None:
            return path_found

    return None
