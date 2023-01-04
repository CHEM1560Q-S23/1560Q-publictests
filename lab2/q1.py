OK_FORMAT = True

test = {   'name': 'q1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> pop_by_precinct = [120000, 40200, 30000, 15000, 5000, 15000]\n'
                                               '>>> vote_share = [0.6, 0.3, 0.4, 0.5, 0.7, 0.2]\n'
                                               '>>> assert num_precincts_needed(pop_by_precinct,vote_share) == 110060\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> pop_by_precinct = [1]\n>>> vote_share = [2]\n>>> assert num_precincts_needed(pop_by_precinct,vote_share) == 2\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
