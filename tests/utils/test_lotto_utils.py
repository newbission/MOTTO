from pytest import raises
from app.utils.lotto_utils import pick_numbers

TEST_COMBINATION = [1, 2, 3, 4, 5]
TEST_SEED = "test-seed"

def test_invalid_k_returns_minus_one():
    """k가 1보다 작은 값일 때 -1을 반환해야함."""
    combination = [1, 2, 3, 4, 5]
    seed = "any-seed"
    assert pick_numbers(combination, seed, k=0) == -1

def test_pick_numbers_in_combination():
    """뽑은 번호가 조합에 있어야함"""
    result = pick_numbers(TEST_COMBINATION, TEST_SEED, k=1)
    assert result in TEST_COMBINATION

    results = pick_numbers(TEST_COMBINATION, TEST_SEED, k=5)
    assert set(results).issubset(set(TEST_COMBINATION))


def test_pick_single_number():
    """k=1일 때, 주어진 리스트에서 숫자 하나만 뽑아야 함"""
    result = pick_numbers(TEST_COMBINATION, TEST_SEED, k=1)

    # 정수인지 판단해 숫자하나만 반환하는지 테스트
    assert isinstance(result, int)


def test_pick_same_numbers():
    """같은 시드를 넘기면 같은 값을 반환해야 함"""
    result1 = pick_numbers(TEST_COMBINATION, TEST_SEED, k=1)
    result2 = pick_numbers(TEST_COMBINATION, TEST_SEED, k=1)
    assert result1 == result2

    result1 = pick_numbers(TEST_COMBINATION, TEST_SEED, k=5)
    result2 = pick_numbers(TEST_COMBINATION, TEST_SEED, k=5)
    assert result1 == result2

def test_k_greater_than_combination_length_raises_error():
    """k가 조합의 길이보다 클 때 ValueError가 발생하는지 테스트"""
    with raises(ValueError):
        pick_numbers(TEST_COMBINATION, "any-seed", k=6)
        
def test_result_length_equals_k():
    """k > 1일 때, 반환된 리스트의 길이가 k와 같은지 테스트"""
    k_value = 3
    results = pick_numbers(TEST_COMBINATION, TEST_SEED, k=k_value)
    assert len(results) == k_value
    
def test_results_are_unique():
    """k > 1일 때, 반환된 값들이 모두 유니크한지 테스트"""
    results = pick_numbers(list(range(20)), "unique-seed", k=10)
    # 리스트를 set으로 변환했을 때 길이가 같다면 모든 원소가 유니크함
    assert len(results) == len(set(results))
    
def test_different_seeds_produce_different_results():
    """다른 시드 값을 사용하면 다른 결과가 반환되는지 테스트"""
    result1 = pick_numbers(TEST_COMBINATION, "seed-1", k=3)
    result2 = pick_numbers(TEST_COMBINATION, "seed-2", k=3)
    # 시드가 다르므로 결과가 다를 확률이 매우 높음
    assert result1 != result2
    
import pytest
from app.utils.lotto_utils import pick_numbers

def test_empty_combination_raises_error():
    """비어있는 조합에서 숫자를 뽑으려 할 때 ValueError가 발생하는지 테스트"""
    with pytest.raises(ValueError):
        pick_numbers([], "empty-seed", k=1)