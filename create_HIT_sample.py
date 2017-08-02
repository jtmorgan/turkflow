#! /usr/bin/env python
# Copyright 2017 Amazon.com, Inc. or its affiliates

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import boto3
from pprint import pprint
import json

# Before connecting to MTurk, set up your AWS account and IAM settings as described here:
# https://blog.mturk.com/how-to-use-iam-to-control-api-access-to-your-mturk-account-76fe2c2e66e2
#
# Follow AWS best practices for setting up credentials here:
# http://boto3.readthedocs.io/en/latest/guide/configuration.html

# Use the Amazon Mechanical Turk Sandbox to publish test Human Intelligence Tasks (HITs) without paying any money.
# Sign up for a Sandbox account at https://requestersandbox.mturk.com/ with the same credentials as your main MTurk account.
client = boto3.client(
    service_name = 'mturk',
#     endpoint_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com',
    endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com/',
    region_name = 'us-east-1',
)


# Uncomment the below to connect to the live marketplace
# Region is always us-east-1
# client = boto3.client(service_name = 'mturk', region_name='us-east-1')

# Test that you can connect to the API by checking your account balance
user_balance = client.get_account_balance()

# In Sandbox this always returns $10,000
print("Your account balance is {}".format(user_balance['AvailableBalance']))

#get information about all of your hits: http://boto3.readthedocs.io/en/latest/reference/services/mturk.html#MTurk.Client.list_hits

# response = client.list_hits(
# #     NextToken='string', #don't know how to use this
#     MaxResults=100
# )

# pprint(response)

#get info about an assignment: http://boto3.readthedocs.io/en/latest/reference/services/mturk.html#MTurk.Client.get_assignment
#this assignment was a rejected one from the latest top articles US batch

# response = client.get_assignment(
#     AssignmentId='354P56DE9K4AH276K1BJDU3J19ZS7X'
# )
#
# pprint(response)

#get all responses for a particular hit: http://boto3.readthedocs.io/en/latest/reference/services/mturk.html#MTurk.Client.list_assignments_for_hit

response = client.list_assignments_for_hit(
    HITId='3D4BBDG7ZHX9MIJTV1DRXPS0ZN5C3E',
#     NextToken='string',
    MaxResults=100,
    AssignmentStatuses=[
        'Rejected',
    ]
)

pprint(response)

# questionSampleFile = open("my_question.xml", "r")
# questionSample = questionSampleFile.read()
#
# # Create a qualification with Locale In('US', 'CA') requirement attached
# localRequirements = [{
#     'QualificationTypeId': '00000000000000000071',
#     'Comparator': 'In',
#     'LocaleValues': [{
#         'Country': 'US'
#     }, {
#         'Country': 'CA'
#     }],
#     'RequiredToPreview': True
# }]
#
# # Create the HIT
# response = client.create_hit(
#     MaxAssignments = 10,
#     LifetimeInSeconds = 600,
#     AssignmentDurationInSeconds = 600,
#     Reward ='0.20',
#     Title = 'Answer a simple question',
#     Keywords = 'question, answer, research',
#     Description = 'Answer a simple question',
#     Question = questionSample,
#     QualificationRequirements = localRequirements
# )
#
# # The response included several fields that will be helpful later
# hit_type_id = response['HIT']['HITTypeId']
# hit_id = response['HIT']['HITId']
# print "Your HIT has been created. You can see it at this link:"
# print "https://workersandbox.mturk.com/mturk/preview?groupId={}".format(hit_type_id)
# print "Your HIT ID is: {}".format(hit_id)