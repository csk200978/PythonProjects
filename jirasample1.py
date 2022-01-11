from jira import JIRA
import re

options = {"server": 'https://jira.broadridge.net', 'verify' : False}
#options = {"server": "https://jira.atlassian.com", "verify" : "false"}
jira1 = JIRA()
jira = JIRA(options)
ipeproject = jira.project("IPE")
print (ipeproject._base_url)
# Get all projects viewable by anonymous users.
projects = jira.projects()

# Sort available project keys, then return the second, third, and fourth keys.
keys = sorted([project.key for project in projects])[2:5]
print (keys)
#issue = jira.issue("IPE-29113")
# Find all comments made by Atlassians on this issue.
#atl_comments = [
#comment
#for comment in issue.fields.comment.comments
#if re.search(r"@broadridge.com$", comment.author.emailAddress)]