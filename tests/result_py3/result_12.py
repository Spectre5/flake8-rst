('test_precisely',
 [('E402', 14, 4, 'module level import not at top of file', '    import matplotlib.pyplot as plt\n'),
  ('E402', 23, 4, 'module level import not at top of file', '    import numpy as np\n'),
  ('E501',
   7,
   83,
   'line too long (82 > 80 characters)',
   "   sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\n"),
  ('E702',
   17,
   26,
   'multiple statements on one line (semicolon)',
   "    plt.plot([1, 2, 3, 4]); plt.ylabel('some numbers');\n"),
  ('E703', 17, 54, 'statement ends with a semicolon', "    plt.plot([1, 2, 3, 4]); plt.ylabel('some numbers');\n"),
  ('F821', 26, 4, "undefined name 'hist'", '    hist(np.random.randn(10000), 100)\n')],
 {'logical lines': 7, 'physical lines': 10, 'tokens': 92})
