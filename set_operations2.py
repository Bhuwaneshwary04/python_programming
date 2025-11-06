"""Q.10
Set Operations on Employee Skills
You are managing a list of employee skills in two sets: Team A Skills and Team B Skills.
The skills in each team are stored as follows:
team_a_skills = {"Python", "Java", "SQL", "Machine Learning"}
team_b_skills = {"Python", "JavaScript", "SQL", "Data Analysis"}

Perform the following set operations:
1. Use copy() to create a copy of the team_a_skills set.
2. Use isdisjoint() to check if there are any common skills between team_a_skills and team_b_skills.
3. Use issubset() to check if team_a_skills is a subset of team_b_skills.
4. Use issuperset() to check if team_b_skills is a superset of team_a_skills.
5. Use pop() to remove a random skill from team_b_skills and print the removed skill.
6. Use update() to add the skills from team_a_skills to team_b_skills.
7. Finally, use clear() to remove all skills from the team_a_skills set.
"""

# Initial skill sets for Team A and Team B 
team_a_skills = {"Python", "Java", "SQL", "Machine Learning"}
team_b_skills = {"Python", "JavaScript", "SQL", "Data Analysis"} 

# 1. Use copy() to create a copy of the team_a_skills set
team_a_skills_copy = team_a_skills.copy()
print("Copy of team_a_skills:", team_a_skills_copy)

# 2. Use isdisjoint() to check if there are any common skills between team_a_skills and team_b_skills
are_disjoint = team_a_skills.isdisjoint(team_b_skills) 
print("Are Team A and Team B skills disjoint?", are_disjoint) 

# 3. Use issubset() to check if team_a_skills is a subset of team_b_skills
is_subset = team_a_skills.issubset(team_b_skills)
print("Is team_a_skills a subset of team_b_skills?", is_subset)

# 4. Use issuperset() to check if team_b_skills is a superset of team_a_skills
is_superset = team_b_skills.issuperset(team_a_skills)
print("Is team_b_skills a superset of team_a_skills?", is_superset) 

# 5. Use pop() to remove a random skill from team_b_skills and print the removed skill
removed_skill = team_b_skills.pop()
print("Removed skill from team_b_skills:", removed_skill) 
print("Updated team_b_skills:", team_b_skills) 

# 6. Use update() to add the skills from team_a_skills to team_b_skills
team_b_skills.update(team_a_skills) 
print("Updated team_b_skills after adding team_a_skills:", team_b_skills)

# 7. Finally, use clear() to remove all skills from the team_a_skills set
team_a_skills.clear()
print("team_a_skills after clear():", team_a_skills)
