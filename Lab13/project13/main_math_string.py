import sys
sys.path.append("..")
import project13.math_utils as mu
from project13.string_utils import capitalize_words, count_letters

def demo():
    print(mu.add(2,3))
    print(capitalize_words("hello world"))

if __name__ == "__main__":
    demo()
