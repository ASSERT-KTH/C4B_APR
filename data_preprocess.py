import pandas as pd

'''
    execute this sql code on submission table and get json files

    SELECT id, submission, sourceCode, author, memory, time, sent, countLine, problems_id, verdicts_id, languages_id, isduplicated
    FROM code4bench.source
    WHERE languages_id=8 AND LENGTH(sourceCode) < 100000;

'''

# Step 1: Read JSON files for code submissions, test cases, and problem details
code_df = pd.read_json('python_submission_10000.json')
tc_df = pd.read_json('testcases_py.json')
problem_df = pd.read_json('problems_py.json')

# Step 2: Convert the 'sent' column in the code submissions dataframe to datetime format
code_df['sent'] = pd.to_datetime(code_df['sent'])

# Step 3: Define a function to filter rows based on specific conditions
def filter_rows(group):
    # Get the last row with verdicts_id == 1
    last_verdict_1 = group[group['verdicts_id'] == 1].head(1)
    # Get the last row with verdicts_id in (2, 3, 4)
    last_verdict_234 = group[group['verdicts_id'].isin([2, 3, 5, 6])].tail(1)
    # Concatenate the two dataframes and return
    return pd.concat([last_verdict_1, last_verdict_234])

# Step 4: Group the code submissions dataframe by author and problems_id and apply the filter function to keep relevant rows
code_df = code_df.groupby(['author', 'problems_id']).apply(filter_rows).reset_index(drop=True)

# Step 5: Group the code submissions dataframe again by author and problems_id and filter out groups with only one row
def filter_rows(group):
    # Check if the count of rows in the group is greater than one
    if len(group) > 1:
        # Return True to keep the group
        return True
    else:
        # Return False to drop the group
        return False

code_df = code_df.groupby(['author', 'problems_id']).filter(filter_rows)

# Step 6: Create a list of unique problem IDs from the filtered code submissions dataframe
problems_list = code_df['problems_id'].unique().tolist()

# Step 7: Filter the test cases dataframe based on the problem IDs obtained from the code submissions dataframe
tc_df = tc_df[tc_df['problems_id'].isin(problems_list)]

# Step 8: Calculate the lengths of input data in the test cases dataframe
lengths = tc_df['inputdata'].apply(lambda x: len(x))

# Step 9: Filter the test cases dataframe to include only rows with input data length less than or equal to 50
tc_df = tc_df[lengths <= 50]

# Step 10: Filter the problem details dataframe to include only rows with problem IDs present in the code submissions dataframe
problem_df = problem_df[problem_df['id'].isin(problems_list)]

# Step 11: Define a function to evaluate code submissions against test cases using subprocess module

# Step 12: Iterate over code submissions and test cases, execute the code, and compare the output with expected results
code_df['test_res'] = code_df.apply(lambda row: judge(row, tc_df), axis=1)

# Step 13: Define a function to check the sanity of evaluation results
def check_sanity(data):
    result = all(item[0] for item in data)
    return result

# Step 14: Apply the sanity check function to the evaluation results for each code submission
code_df['sanity'] = code_df['test_res'].apply(lambda x: check_sanity(x))

# Step 15: Identify code submissions with a verdict of 1 and failed sanity check
el_acc = code_df.loc[(code_df['verdicts_id'] == 1) & (code_df['sanity'] == False), ['author', 'problems_id']].values.tolist()

# Step 16: Remove the identified code submissions from the code submissions dataframe
for i in el_acc:
    condition = code_df.loc[(code_df['author'] == i[0]) & (code_df['problems_id'] == i[1])]
    code_df.drop(condition.index, inplace=True)

# Step 17: Identify code submissions with a verdict of 2 and passed sanity check
el_rej = code_df.loc[(code_df['verdicts_id'] == 2) & (code_df['sanity'] == True), ['problems_id']].values.tolist()

# Step 18: Remove the identified code submissions from the code submissions dataframe
for i in el_rej:
    condition = code_df.loc[(code_df['problems_id'] == i[0])]
    code_df.drop(condition.index, inplace=True)

# Step 19: Create a list of unique problem IDs from the updated code submissions dataframe
problems_list = code_df['problems_id'].unique().tolist()

# Step 20: Filter the problem details dataframe based on the updated problem IDs
problem_df = problem_df[problem_df['id'].isin(problems_list)]

# Step 21: Write the updated code submissions, problem details, and test cases dataframes to CSV files
code_df.to_csv('cb_submission_res.csv', index=False)
problem_df.to_csv('cb_problem_res.csv', index=False)
tc_df.to_csv('cb_testcase_res.csv', index=False)