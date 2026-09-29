owner_age = input('PLease input the owner age --->')
monthly_revenue = float(input('Please input the monthly revenue --->'))
cc = input('Please enter your credit score')
yrs = float(input('Please enter your year in business --->'))
has_default = bool(input('Does your business have defaults?'))
cn = input('Please input the collateral name --->')
cv = float(input('Please input the collateral value'))

#baseline requirement

max_loan = 0
base_feee = 0

if owner_age >= 21 and yrs == 2.0 and has_default == False:
    print('Baseline passed')
    if cc >= 720:#tier1
        max_loan = monthly_revenue * 3
        print('Maximum loanable amount is set to',max_loan)
        print('High credit score')
        if monthly_revenue >= 50000:
            print ('Revenue higher than 50K')
            base_feee = max_loan * 0.015
            print('Base fee rate is set to',base_feee)
        else:
            print ('Revenue lower than 50k')
            base_feee = max_loan * 0.025
            print('Base fee rate is set to',base_feee)
        if cv >= max_loan:
            print('collateral',cn, 'with a value of',cv, 'is ACCEPTED')
        else:
            print('rejected: Insufficient collateral value for',cn)

        surge_fee_rate = max_loan * base_feee
        print('Additional charge of ', surge_fee_rate)
        if max_loan % 500 != 0:
            print('Additional charge added')
            surge_fee_rate += 250
            print('Updated base fee is ', surge_fee_rate)
    elif 620 <= cc <720:
        print('You have a average credit score')
        max_loan = monthly_revenue * 1.5
        print('Maximum loanable amount is set to',max_loan)
        print('Mid credit score')
        if yrs >= 5.0:
            print('Your business is more than five years')
            base_feee = max_loan * 0.02
            print('Base fee rate is set to',base_feee)
        else:
            print('Your business is less than five years')
            base_feee = max_loan * 0.035
            print('Base fee rate is set to',base_feee)
    elif cc < 620:
         print('Rejected : Credit score below the requirement')
else:
     print('Invalid : Do not meet the baseline requirement')


