OK_FORMAT = True

test = {   'name': 'q1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> matrix_1=np.array([[1,2,3],[3,4,7],[5,6,7]], dtype=int)\n'
                                               '>>> matrix_2=np.array([[7,8,7],[9,10,7],[11,12,7]], dtype=int)\n'
                                               '>>> assert np.array_equal(np.matmul(matrix_1,matrix_2),mat_prod(matrix_1,matrix_2)) == True\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
