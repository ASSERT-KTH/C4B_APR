# Code4Bench Automated Program Repair

Code4Bench is a comprehensive benchmark that provides multidimensional data for analyzing Codeforces programming challenges. The dataset offered by Code4Bench includes various aspects of code submissions, judgments, languages, problem descriptions, test cases, and user demographics. It follows a structured schema and includes tables such as source, verdicts, languages, problems, testcases, user, countries, states, realfaultslocations, and more.

## Purpose

The purpose of this repository is to utilize the Code4Bench dataset for automating program repair. Our focus is on generating fault-inducing tests using the dataset's buggy and accepted versions of code submissions.

## Approach

Our approach involves the following steps:

1. Consecutive Versions: Selecting two consecutive versions of a user's code - one buggy and one accepted.
1. Fault-Inducing Tests: Generating tests that expose faults in the buggy version of the code.
1. Test Size Filter: Filtering problems based on having all tests smaller than a certain length.
1. Submission Size Filter: Limiting submissions to a certain size for manageability and efficiency.

## Rejected Code Labels

For rejected code submissions, we focus on the following labels:

- Time limit
- Wrong answer
- Accepted
- Runtime error
- Memory limit

## Sanity Check and Verification Process

To ensure the quality and consistency of the dataset, we perform a sanity check and verification process:

1. Verification Process: For each submission with verdict=1 (accepted), all tests should pass. For each submission with verdict=2 (rejected), at least one test should fail.
1. Handling Inconsistencies: If a submission with verdict=2 has no failing test, the problem (and related submissions) should be removed from the dataset.

## Size Limits

To maintain a manageable dataset, the following size limits are applied:

- Source Size Limit: Both rejected and accepted code submissions should have a limit of 100,000 characters.
- Input Size Limit: The input size for all tests should be limited to 1,000 characters.

## Balancing Accepted and Rejected Submissions

We aim to have a balanced representation of accepted and rejected submissions in the dataset, ensuring a comprehensive analysis.

## Problem Pair

Each problem pair consists of a code version that is accepted and another version that is rejected. Along with these versions, a set of tests is provided that pass on both versions.

## Tracking First Acceptance and Last Failure

For each problem, we track the first instance of acceptance and the last occurrence of failure.

## Dataset Size

The Code4Bench dataset consists of the following:

- Submissions: 5,670 (accepted/rejected)
- Problems: 336
- Testcases: 21,354

With this dataset, we aim to create a curated subset for automated program repair, ensuring a balanced representation of accepted and rejected submissions while maintaining a manageable size.

## Fields definition
<table>
<thead><tr><th>Field Name</th><th>Description</th></tr></thead><tbody>
 <thead><tr><th colspan="2" >source</th></tr></thead><tbody>
 <tr><td>id</td><td>A unique number</td></tr>
 <tr><td>submission</td><td>ID number given by Codeforces to this submission</td></tr>
 <tr><td>sourceCode</td><td>The submitted source code</td></tr>
 <tr><td>author</td><td>ID number of submitter</td></tr>
 <tr><td>memory</td><td>The memory used by this submission</td></tr>
 <tr><td>time</td><td>The execution time of this submission</td></tr>
 <tr><td>sent</td><td>The submission time by user</td></tr>
 <tr><td>countLine</td><td>The number of lines of code</td></tr>
 <tr><td>problems_id</td><td>Problem ID number</td></tr>
 <tr><td>verdicts</td><td>The Codeforces' judgment on this submission</td></tr>
 <tr><td>languages_id</td><td>The language in which this submission is written</td></tr>
 <tr><td>test_res</td><td>A tuple contains (A boolean showing if expected data is equal to output, code's output, expected result, testcase id)</td></tr>
 <tr><td>sanity</td><td>A boolean indicates the result of the sanity check (False for the Buggy version and True for the accepted version)</td></tr>
 
 <thead><tr><th colspan="2" >problems</th></tr></thead><tbody>
 
 <tr><td>id</td><td>A unique number</td></tr>
 <tr><td>fullname</td><td>The ID number of competition and name of problem</td></tr>
 <tr><td>contest</td><td>ID number of competition</td></tr>
 <tr><td>name</td><td>ID number of problem section</td></tr>
 <tr><td>context</td><td>The description of problem</td></tr>
 
 <thead><tr><th colspan="2" >testcases</th></tr></thead><tbody>
 
 <tr><td>id</td><td>A unique number</td></tr>
 <tr><td>inputData</td><td>Input data for problem</td></tr>
 <tr><td>expectedResult</td><td>Expected output for problem</td></tr>
 <tr><td>problems_id</td><td>ID number of corresponding problem</td></tr>
 <tr><td>isValid</td><td>Whether test case is complete or deficient</td></tr>
 
</tbody></table>

## Acknowledgments

We would like to express our gratitude to the Code4Bench team for providing the dataset and enabling research and development in the field of automated program repair.
