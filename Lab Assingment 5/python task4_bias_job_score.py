# -------------------------------------------------------------------
# Task 4 - Bias Analysis
# Topic: Job Applicant Scoring System
# -------------------------------------------------------------------
# Objective:
# To build a simple scoring system for job applicants
# and check if the system gives equal results (no gender bias).
#
# Bias means giving unfair advantage or disadvantage to someone
# based on gender, name, race, or any unrelated factor.
#
# Here, we will:
#   1. Create a scoring function based on applicant data.
#   2. Test it with male, female, and gender-neutral names.
#   3. Confirm that names do NOT affect scores.
# -------------------------------------------------------------------

def job_score(name, experience, skills, education_level):
    """
    Function: job_score
    Purpose: Calculate the applicant's total score.

    Parameters:
        name (str): Applicant's name (for display only).
        experience (int): Number of years of work experience.
        skills (int): Skill rating out of 10.
        education_level (int): Education rating (1–5 scale).

    Scoring logic:
        - Experience is important → multiplied by 2
        - Skills are highly valued → multiplied by 3
        - Education adds value → multiplied by 1.5

    Note:
        The function does not use 'name' in calculations.
        This ensures there is no gender or name bias.
    """
    score = 0
    score += experience * 2           # Each year of experience adds 2 points
    score += skills * 3               # Each skill point adds 3 points
    score += education_level * 1.5    # Education adds 1.5 per level
    return round(score, 2)            # Round off score to 2 decimals


# -------------------------------------------------------------------
# Section 1: Test with same data for different names
# -------------------------------------------------------------------
# This test ensures that gender or name does not affect the output.

print("---- TEST 1: Checking for Gender Bias ----")
john_score = job_score("John", 5, 8, 4)   # Male
mary_score = job_score("Mary", 5, 8, 4)   # Female
alex_score = job_score("Alex", 5, 8, 4)   # Gender-neutral

print(f"John's Score: {john_score}")
print(f"Mary's Score: {mary_score}")
print(f"Alex's Score: {alex_score}")

# Observation for Test 1
if john_score == mary_score == alex_score:
    print("✅ No bias found — all names treated equally.\n")
else:
    print("⚠️ Possible bias detected — scores differ!\n")


# -------------------------------------------------------------------
# Section 2: Test with different data (valid comparison)
# -------------------------------------------------------------------
# Here, we change experience/skills/education to show
# how scores logically change based on real factors.

print("---- TEST 2: Comparing Applicants with Different Data ----")
# Different experience and skill levels, same logic for all
john_score_2 = job_score("John", 3, 6, 3)
mary_score_2 = job_score("Mary", 7, 8, 4)
alex_score_2 = job_score("Alex", 10, 5, 5)

print(f"John (3 yrs exp, skill 6, edu 3): {john_score_2}")
print(f"Mary (7 yrs exp, skill 8, edu 4): {mary_score_2}")
print(f"Alex (10 yrs exp, skill 5, edu 5): {alex_score_2}")
print("✅ These differences are logical (based on data, not name).\n")


# -------------------------------------------------------------------
# Section 3: Test edge cases (zero or missing values)
# -------------------------------------------------------------------
print("---- TEST 3: Edge Cases ----")
# Low or missing experience
print("Case 1 - No experience:")
print("Score:", job_score("Taylor", 0, 7, 3))

# Low skills
print("\nCase 2 - Weak skill set:")
print("Score:", job_score("Sam", 5, 2, 4))

# Excellent in all areas
print("\nCase 3 - Strong profile:")
print("Score:", job_score("Riya", 10, 9, 5))
print("\n✅ These results depend only on data — no gender factor used.\n")


# -------------------------------------------------------------------
# Final Observation
# -------------------------------------------------------------------
print("---- CONCLUSION ----")
print("The system uses experience, skills, and education to calculate score.")
print("Names are only used for display — not for decision making.")
print("Hence, the scoring system is transparent and free from gender bias.")
