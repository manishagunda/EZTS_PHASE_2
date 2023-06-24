Families={
    "a":
      {"aa":{"aaa","aab"},
       "ab":{"aba","abb"},
       "ac":{"aca","acb"}},
    "b":
    {"ba":{"baa","bab"},
     "bb":{"bba","bbb"},
     "bc":{"bca","bcb"}},
    "c":
    {"ca":"caa","cb":"cba"}
     }
for parent,children in Families.items():
    print(f"{parent} has {len(children)}kid(s):")
    print(f"{',and '.join([str(child) for child in[*children]])}")
    