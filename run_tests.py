import pytest
def start_tests():
    pytest.main(["api/users/auth/tests.py"])
    pytest.main(["alchemy/utils/test_repository.py"])

start_tests()