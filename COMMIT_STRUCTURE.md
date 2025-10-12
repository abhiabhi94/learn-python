# Commit Structure

This PR has been restructured into individual commits for easier review:

## Commits (in order):

1. **c82e993** - Chapter 7: Control Flow Statements
2. **95250a7** - Chapter 8: Functions  
3. **b8285f0** - Chapter 9: Strings
4. **0746e66** - Chapter 10: Objects and Classes
5. **6393242** - Chapter 11: Modules, packages and imports
6. **5346cc6** - Chapter 12: Playing with files
7. **2c47e63** - Chapter 13: Regular Expressions
8. **9e7b023** - Chapter 14: Threading
9. **e72f574** - Chapter 15: Database and mysql
10. **d47e215** - Chapter 16: Sending email
11. **0306f34** - Chapter 17: Websockets
12. **cb4ea9f** - Chapter 18: Parsing XML

## How to create separate PRs:

To create individual PRs for each chapter, you can cherry-pick specific commits:

```bash
# For Chapter 8
git checkout -b chapter-08-hinglish main
git cherry-pick 95250a7
git push origin chapter-08-hinglish

# For Chapter 9
git checkout -b chapter-09-hinglish main
git cherry-pick b8285f0
git push origin chapter-09-hinglish

# And so on...
```

Alternatively, use the GitHub UI to create PRs from individual commits.
