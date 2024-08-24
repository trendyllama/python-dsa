
class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def set_next_node(self, link_node):
        self.link_node = link_node

    def get_next_node(self):
        return self.link_node

    def get_value(self):
        return self.value


class LinkedList:
  def __init__(self, head_node: Node = None):
    self.head_node = head_node
  
  def insert(self, new_node):
    current_node = self.head_node

    if not current_node:
      self.head_node = new_node

    while(current_node):
      next_node = current_node.get_next_node()
      if not next_node:
        current_node.set_next_node(new_node)
      current_node = next_node


  def __iter__(self):
    current_node = self.head_node
    while(current_node):
      yield current_node.get_value()
      current_node = current_node.get_next_node() 