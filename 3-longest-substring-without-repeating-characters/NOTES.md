```
# max length is distance + 1 btwn left and right pointers  without repeating characters (r - l) + 1
# iterate through string every time come accross c that is not repeating, count++ and add c to visited
# keep moving right pointer until come across c that is repeating
# then need to set res to count if count > res, reset count, reset visited, and move left pointer plus 1
# then do the same thing
```