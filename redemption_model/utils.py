from datetime import datetime, timedelta

def calculate_total_interest(facility_A, contractual_monthly_rate, beginning_default_period, end_default_period):

    #Transform string to date (yyyy-mm-dd)
    def transform_string_to_date(date):
        return datetime.strptime(date, '%Y-%m-%d')

    contractual_monthly_rate = float(contractual_monthly_rate) / 100
    facility_A = float(facility_A)
    beginning_default_period = transform_string_to_date(beginning_default_period)
    end_default_period = transform_string_to_date(end_default_period)

    #Original Loan Input
    REDEMPTION_STATEMENT_DATE = transform_string_to_date('2024-04-23')
    DATE_OF_LOAN = transform_string_to_date('2023-01-15')
    current_date = DATE_OF_LOAN
    #FINAL_MATURITY_DATE = transform_string_to_date('2024-03-24')

    #FACILITY_B = 250000 
    FACILITY_C = 25000
    ARRANGMENT_FEE = 5000
    DEFAULT_INTEREST_RATE = 0.02  #2%

    #Build Drawdowns
    BUILD_DRAWDOWNS = {
        transform_string_to_date('2023-02-14'): 25000,
        transform_string_to_date('2023-03-25'): 25000,
        transform_string_to_date('2023-05-03'): 25000,
        transform_string_to_date('2023-06-11'): 25000,
        transform_string_to_date('2023-07-20'): 25000,
        transform_string_to_date('2023-08-28'): 25000,
        transform_string_to_date('2023-10-06'): 25000,
        transform_string_to_date('2023-11-14'): 25000,
        transform_string_to_date('2023-12-23'): 25000,
        transform_string_to_date('2024-01-31'): 25000
    }

    #Capital Repayment
    CAPITAL_REPAYMENT = {
        transform_string_to_date('2024-02-23'): 100000
    }

    #Calculation of Inputs
    Interest_retention = FACILITY_C - ARRANGMENT_FEE
    Implied_daily_regular_rate = contractual_monthly_rate / 30
    #Implied_regulat_annual_rate = (1 + Implied_daily_regular_rate)**365 - 1 - **Not Used**
    Implied_daily_default_rate = DEFAULT_INTEREST_RATE / 30

    Opening_PB = facility_A + ARRANGMENT_FEE    # Initialized here - After initialization: Opening PB will be closing PB of the day before
    Interest_balance = Interest_retention       # Initialized here - After initialization: Max between Accrued Daily Interest and Interest rate

    #Extra variables defined here
    Accrued_daily_interest = 0
    one_day = timedelta(days=1) #One Day
    num_days = (REDEMPTION_STATEMENT_DATE - DATE_OF_LOAN).days + 1 #Number of Days that needs looping through


    for day in range(num_days):
        #Redefine Opening_PB and Interest_balance after initialization 
        if day != 0 :
            Opening_PB = CLOSING_PB
            if Accrued_daily_interest > Interest_retention:
                Interest_balance = Accrued_daily_interest

        #Look in the dictionary if Current_date exist otherwise return 0
        drawdown = BUILD_DRAWDOWNS.get(current_date, 0)

        #Boolean return if Current Date is between Beginning and end Default Period
        default_payment = beginning_default_period <= current_date <= end_default_period

        if default_payment:
            DailyRate = Implied_daily_default_rate 
        else:
            DailyRate = Implied_daily_regular_rate

        #Calculte Daily Interest
        daily_interest = (Opening_PB + drawdown + Interest_balance) * DailyRate

        #Look in the dictionary if Current_date exist otherwise return 0
        payment_received = CAPITAL_REPAYMENT.get(current_date, 0)

        #Calculate Closing PB
        CLOSING_PB = Opening_PB + drawdown - payment_received

        #Move to the next day
        current_date += one_day

        #Calculate Final Accrued Daily Interest
        Accrued_daily_interest += daily_interest

    return Accrued_daily_interest