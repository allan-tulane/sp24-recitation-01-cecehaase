from main import binary_search, compare_search, linear_search, print_results


def test_linear_search():
  """ done. """
  assert linear_search([1,2,3,4,5], 5) == 4
  assert linear_search([1,2,3,4,5], 1) == 0
  assert linear_search([1,2,3,4,5], 6) == -1


def test_binary_search():
  assert binary_search([1,2,3,4,5], 5) == 4
  assert binary_search([1,2,3,4,5], 1) == 0
  assert binary_search([1,2,3,4,5], 6) == -1
  assert binary_search([2,4,6,8,10], 6) == 2
  assert binary_search([3,6,9,12,15], 15) == 4
  ###


def test_compare_search():
  res = compare_search(sizes=[10, 100])
  print(res)
  assert res[0][0] == 10
  assert res[1][0] == 100
  assert res[0][1] < 1
  assert res[1][1] < 1
  print(print_results(res))

