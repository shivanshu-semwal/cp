import json
import operator

# Go the URL below on your browser and download the file to the same directory as this script
# https://codeforces.com/api/problemset.problems

data = json.load(open("./problemset.problems.json"))
contests = set()
problems = data["result"]["problems"]

for problem in problems:
    contests.add(problem["contestId"])

for contest in contests:
    print(contest)