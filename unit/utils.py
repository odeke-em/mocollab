#!/usr/bin/env python3

import doctest

def load_clauses_f(f, clause):
    """
    >>> attributes = (
    ...   "CONQUEST START", # Simulate a bit of noisy variables here
    ...   "POWER-UPS START",
    ...   "Health-PUP 28 21",
    ...   "Speed-PUP 13 8",
    ...   "Attack-PUP 15 9",
    ...   "POWER-UPS END",
    ...   "CONQUEST END",)
    >>> itr = map(lambda l: l, attributes)
    >>> # To mimick a normal iterator for which '__next__'
    >>> # marches forward the head pointer
    >>> store = load_clauses_f(itr, 'POWER-UPS')
    >>> store['Attack-PUP'] == [['15', '9']]
    True
    >>> store['Health-PUP'] == [['28', '21']]
    True
    """
    store = {}
    clause_len = len(clause)

    # Find the start clause
    for line in f:
        if line == '': # End of file encountered
            return store

        clause_index = line.find(clause)
        if clause_index < 0:
            continue

        start_index = line[clause_index + clause_len:].find('START')
        if start_index >= 0:
            break

        # TODO: Throw an error? Because the clause has been encountered

    for line in f:
        if line == '': # EOF
            break
            
        if line.find(clause) >= 0:
            if line.find('END') >= 0:
                break

        fields = line.strip('\n').split(' ')
        fields = [field.lstrip(' ') for field in fields if field]
        if len(fields) <= 1:
            continue
        key, *rest = fields
        store.setdefault(key, []).append(rest)

    return store

def load_clauses_f_map(f, clause, mapper):
    """
    >>> attributes = (
    ...   "TRAVERSE START", # Simulate a bit of noisy variables here
    ...   "POWER-UPS START",
    ...   "Health-PUP 22 21",
    ...   "Speed-PUP 23 8",
    ...   "Attack-PUP 95 9",
    ...   "POWER-UPS END",
    ...   "TRAVERSE END",)
    >>> itr = map(lambda l: l, attributes)
    >>> # To mimick a normal iterator for which '__next__'
    >>> # marches forward the head pointer
    >>> store = load_clauses_f_map(itr, 'POWER-UPS', int)
    >>> store['Attack-PUP'] == [(95, 9,)]
    True
    >>> store['Speed-PUP'] == [(23, 8,)]
    True
    """

    fields_dict = load_clauses_f(f, clause)
    for field, attrListing in fields_dict.items():
        mapping = []
        for attrs in attrListing:
            mapping.append(tuple(map(mapper, attrs)))
        fields_dict[field] = mapping

    return fields_dict

if __name__ == '__main__':
    doctest.testmod()
