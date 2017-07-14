def invert(d):
  result = {}
  for key in d:
    value = d[key]
    result[value] = key
  return result

subs = {
  "-": "_dash_",
  "$": "_dollar_",
  "*": "_star_"
}

#placements = invert(replacements)
unsubs = {v: k for k, v in subs.items()}

# Todo: These will probably have to get more sophisticated as we go.

def munge(s):
  """clj symbol (as a string) -> acceptable python ID"""
  return _munge(subs, s)

def unmunge(s):
  """munged clj symbol (as a string) -> original clj symbol"""
  return _munge(unsubs, s)

def _munge(d, s):
  """Munge a string identifier, returning a new string using replacements in d"""
  for s1 in d:
    s = s.replace(s1, d[s1])
  return s

