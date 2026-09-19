age = int(input("Enter your age: "))
is_employed = input("Are you employed? (True/Leave blank if False): ") == "True"
credit_score = float(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income: "))
has_collateral = input("Do you have collateral? (True/Leave blank if False): ") == "True"

if age >= 21 and is_employed:
	print("You meet the baseline requirements for a loan.")

	if credit_score >= 700:
		print("You have a high credit score.")
		if annual_income >= 100000:
			base_rate = 4.5
			print("You have a high annual income and credit score. Your base rate is", base_rate, "%.")
		else:
			base_rate = 5.0
			print("You have a high credit score but your annual income is below $100,000. Your base rate is", base_rate, "%.")
	elif credit_score >= 600:
		if has_collateral:
			base_rate = 7.0
			print("You have a moderate credit score and collateral. Your base rate is", base_rate, "%.")
		elif annual_income >= 40000:
			base_rate = 8.0
			print("You have a moderate credit score and sufficient income. Your base rate is", base_rate, "%.")
		else:
			base_rate = 9.5
			print("You have a moderate credit score but low income and no collateral. Your base rate is", base_rate, "%.")
	else:
		print("Rejected: Your credit score is too low for a loan.")
else:
	print("Rejected: You do not meet the baseline requirements for a loan.")
