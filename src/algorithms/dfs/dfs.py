from TreeNode import TreeNode, sample_root_node, print_tree
from typing import Any, Tuple, Optional

print_tree(sample_root_node)


def dfs(root: TreeNode, target: Any, path: Tuple = ()) -> Optional[Tuple]:
    """_summary_

    Args:
        root (TreeNode): _description_
        target (Any): _description_
        path (Tuple, optional): _description_. Defaults to ().

    Returns:
        Optional[Tuple]: _description_
    """

    path = path + (root,)

    if root.value == target:
        return path

    for child in root.children:
        path_found = dfs(child, target, path)

        if path_found is not None:
            return path_found

    return None


node = dfs(sample_root_node, "F")
print(node)
