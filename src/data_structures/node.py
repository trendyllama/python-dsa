from typing import Optional, Any, Self


class Node:
    def __init__(self, value: Any, link_node: Optional[Self] = None):
        self.value = value
        self.link_node = link_node

    def set_next_node(self, link_node: Self) -> None:
        self.link_node = link_node

    def get_next_node(self) -> Optional[Self]:
        return self.link_node

    def get_value(self) -> Any:
        return self.value
