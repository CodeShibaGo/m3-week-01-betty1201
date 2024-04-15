def abbrev_name(name):
  return '.'.join(word[0].upper() for word in name.split())

# def abbrev_name(name):
#   first, last = name.upper().split()
#   return f"{first[0]}.{last[0]}"

