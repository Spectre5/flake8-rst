('test_precisely',
 [('E128',
   9,
   12,
   'continuation line under-indented for visual indent',
   u'        data = {"key1": "value1", "key2": "value2"}\n'),
  ('E133', 11, 8, 'closing bracket is missing indentation', None),
  ('E251', 16, 20, 'unexpected spaces around keyword / parameter equals', None),
  ('E251', 16, 22, 'unexpected spaces around keyword / parameter equals', None),
  ('E133', 17, 12, 'closing bracket is missing indentation', None),
  ('F821', 8, 21, "undefined name 'Table'", u'        data_table.insert(),\n'),
  ('F821', 8, 41, "undefined name 'metadata'", u'        data_table.insert(),\n'),
  ('F821', 9, 12, "undefined name 'Column'", u'        data = {"key1": "value1", "key2": "value2"}\n'),
  ('F821', 9, 25, "undefined name 'Integer'", u'        data = {"key1": "value1", "key2": "value2"}\n'),
  ('F821', 10, 12, "undefined name 'Column'", u'    )\n'),
  ('F821', 10, 27, "undefined name 'JSONB'", u'    )\n'),
  ('F821', 13, 13, "undefined name 'engine'", None)],
 {'logical lines': 3, 'physical lines': 10, 'tokens': 68})