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

## Acknowledgments

We would like to express our gratitude to the Code4Bench team for providing the dataset and enabling research and development in the field of automated program repair.
