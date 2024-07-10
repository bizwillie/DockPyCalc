# tests/test_memory.py

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add the parent directory to Python's path
from memory import Memory

@pytest.fixture
def memory_instance():
    return Memory()

def test_memory_add(memory_instance):
    memory_instance.add(10)
    assert memory_instance.history == [10]
    memory_instance.add(20)
    assert memory_instance.history == [10, 20]

def test_memory_recall(memory_instance):
    memory_instance.add(10)
    memory_instance.add(20)
    assert memory_instance.recall() == 20

def test_memory_clear(memory_instance):
    memory_instance.add(10)
    memory_instance.add(20)
    memory_instance.clear()
    assert memory_instance.history == []

# Add more tests as needed for other memory functions
