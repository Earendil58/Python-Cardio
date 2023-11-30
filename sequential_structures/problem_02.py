# A very important law is being voted in Congress. 
# Develop a program that allows entering the number of votes in favor and against, 
# and reports the percentage obtained in each case.

votes_in_favor = int(input('Enter the amount of votes in favor of the law: '))
votes_against = int(input('Enter the amount of votes against the law: '))

total_votes = votes_in_favor + votes_against
percentage_of_votes_in_favor = round((votes_in_favor * 100) / total_votes,2)
percentage_of_votes_against = round((votes_against * 100) / total_votes,2)

print(f'The percentage for favorable votes is {percentage_of_votes_in_favor}%')
print(f'The percentage of opossing votes is {percentage_of_votes_against}%')