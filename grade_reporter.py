# Starting list of scores (do not change)
scores = [72, 45, 90, 61, 38]

passed_count = 0
failed_count = 0
total_score = 0
total_students = len(scores)

for score in scores:
    total_score += score
    
    # Determine the grade using if / elif / else
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    print(f"Score: {score} - Grade: {grade}")
    
    # Count passes and fails
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

# Calculate average rounded to one decimal place
average = round(total_score / total_students, 1)

print("\n--- Summary ---")
print(f"Number that passed: {passed_count}")
print(f"Number that failed: {failed_count}")
print(f"Class Average: {average}")
