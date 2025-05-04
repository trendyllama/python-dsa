from TreeNode import TreeNode


def dfs(root: TreeNode, target, path: tuple = ()) -> tuple | None:
    """ """
    path = path + (root,)

    if root.value == target:
        return path

    for child in root.children:
        path_found = dfs(child, target, path)

        if path_found is not None:
            return path_found

    return None
