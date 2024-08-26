print("Once upon a time...")
######
# TREENODE CLASS
######
from src.data_structures.tree_node import StoryTreeNode


######
# VARIABLES FOR TREE
######
story_root = StoryTreeNode(
    """
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you:
1 ) Roar back!
2 ) Run to the left...
"""
)
user_choice = input("What is your name?")
choice_a = StoryTreeNode(
    """
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""
)
choice_a_1 = StoryTreeNode(
    """
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.
YOU HAVE ESCAPED THE WILDERNESS.
"""
)
choice_a_2 = StoryTreeNode(
    """
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.
YOU REMAIN LOST.
"""
)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

choice_b = StoryTreeNode(
    """
You come across a clearing full of flowers.
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""
)
choice_b_1 = StoryTreeNode(
    """
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.
YOU REMAIN LOST.
"""
)
choice_b_2 = StoryTreeNode(
    """
The bear understands and apologizes for startling you. Your new friend shows you a
path leading out of the forest.
YOU HAVE ESCAPED THE WILDERNESS.
"""
)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

######
# TESTING AREA
######
print(story_root.story_piece)
print(user_choice)
print(story_root.add_child(choice_a))
story_root.add_child(choice_b)
story_root.traverse()
