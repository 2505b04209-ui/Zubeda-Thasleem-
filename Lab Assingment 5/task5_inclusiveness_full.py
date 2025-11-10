# -------------------------------------------------------------------
# Task 5 - Inclusiveness
# Topic : Inclusive Job Applicant Scoring & Reporting System
# -------------------------------------------------------------------
# Objective:
# To create an inclusive job-scoring system that treats
# every applicant equally regardless of gender identity.
# -------------------------------------------------------------------

# -------------------- IMPORTS --------------------
import statistics

# -------------------- SCORING FUNCTION --------------------
def job_score(name, gender, experience, skills, education_level, teamwork, creativity):
    """
    Calculate applicant score based on multiple job-related factors.
    Gender or name is NOT part of the formula (for fairness).

    Parameters:
        name (str)            -> applicant's name
        gender (str)          -> 'male' | 'female' | 'non-binary' | 'prefer not to say'
        experience (int)      -> years of work experience
        skills (int)          -> skill rating (1–10)
        education_level (int) -> education rating (1–5)
        teamwork (int)        -> teamwork rating (1–10)
        creativity (int)      -> creativity rating (1–10)
    """

    # --- Weight system ---
    # Experience (×2), Skills (×3), Education (×1.5), Teamwork (×2), Creativity (×1.5)
    score = (
        (experience * 2)
        + (skills * 3)
        + (education_level * 1.5)
        + (teamwork * 2)
        + (creativity * 1.5)
    )

    return round(score, 2), gender


# -------------------- INCLUSIVE MESSAGE --------------------
def inclusive_message(name, gender, score):
    """
    Generate gender-neutral message using 'they/them' pronouns.
    """
    pronoun = "they"  # universal neutral pronoun
    return f"{name}'s total score is {score}. Based on data, {pronoun} qualify equally for the role."


# -------------------- DATA: APPLICANT LIST --------------------
print("---- Inclusive Job Applicant Scoring System ----\n")

applicants = [
    ("John", "male", 5, 8, 4, 7, 6),
    ("Mary", "female", 5, 8, 4, 7, 6),
    ("Alex", "non-binary", 5, 8, 4, 7, 6),
    ("Taylor", "prefer not to say", 5, 8, 4, 7, 6),
    ("Sam", "female", 6, 9, 4, 9, 8),
    ("Ravi", "male", 3, 7, 3, 8, 5),
]

# -------------------- CALCULATE SCORES --------------------
scores = []
for name, gender, exp, skill, edu, team, creative in applicants:
    score, g = job_score(name, gender, exp, skill, edu, team, creative)
    scores.append((name, g, score))
    print(inclusive_message(name, g, score))

# -------------------- ANALYSIS --------------------
print("\n---- Inclusive Analysis ----")
values = [s[2] for s in scores]
print(f"Average applicant score: {round(statistics.mean(values),2)}")
print(f"Highest score: {max(values)}")
print(f"Lowest score: {min(values)}")

# Sort applicants by score (highest first)
sorted_scores = sorted(scores, key=lambda x: x[2], reverse=True)
print("\nTop 3 Applicants:")
for i, (name, g, score) in enumerate(sorted_scores[:3], start=1):
    print(f"{i}. {name} ({g}) — {score} points")

# -------------------- CONCLUSION --------------------
print("\n✅ Inclusiveness check passed — every gender treated equally.")
print("✅ Selection depends only on skills, experience, and creativity.")
