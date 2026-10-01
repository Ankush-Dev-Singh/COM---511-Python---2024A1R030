# Write a program to count votes in a simple election. The first input line contains the candidate names, separated by commas. The next line contains the number of voters, n. Each of the following n lines contains one vote: a candidate name entered by a voter. Count a vote only when it matches a listed candidate. Candidate-name matching must be case-insensitive. Ignore invalid votes. Print all candidates and their vote counts in descending order of votes. If candidates have the same vote count, print them in alphabetical order. Then print the winner or winners. If two or more candidates tie for the highest vote count, announce all of them as winners, in alphabetical order. If no valid votes are cast, print the candidate results followed by No valid votes were cast.

# Input Format

# first line contains candidate names separated by commas.
# The second line contains an integer n, the number of voters.
# Each of the next n lines contains one candidate name entered as a vote.# Count votes in a simple election

# Input candidate names
candidates = input().split(",")

# Remove extra spaces and create dictionary
votes = {}

for candidate in candidates:
    candidate = candidate.strip()
    votes[candidate] = 0

# Number of voters
n = int(input())

# Take votes
for i in range(n):
    vote = input().strip()

    # Check vote ignoring case
    for candidate in votes:
        if vote.lower() == candidate.lower():
            votes[candidate] += 1
            break

# Sort candidates:
# First by votes (descending)
# Then by name (alphabetically)
result = sorted(votes.items(), key=lambda x: (-x[1], x[0].lower()))

# Print results
print("Election Results:")

for candidate, count in result:
    print(candidate + ":", count)

# Check if there are any valid votes
highest = result[0][1]

if highest == 0:
    print("No valid votes were cast.")
else:
    winners = []

    for candidate, count in result:
        if count == highest:
            winners.append(candidate)

    print("Winner(s):", ", ".join(winners))
    print("Highest Votes:", highest)
