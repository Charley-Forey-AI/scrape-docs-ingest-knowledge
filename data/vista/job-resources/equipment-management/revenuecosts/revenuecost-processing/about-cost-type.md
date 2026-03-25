---
title: "About Cost Type | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-cost-type"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-cost-type"
---

# About Cost Type

All hours posted in this program will be posted to the Labor
 Cost Type specified in EM Company Parameters (Labor tab).
 The cost type determines to which GL
 expense account (in the EM Department file) the labor costs will be posted; however, if
 you have set up override expense accounts by cost code, then the cost code specified
 during maintenance timecard entry will determine the GL expense account to which the
 labor costs will be posted. The offsetting entry will be posted to the ‘Labor Fixed Rate
 GL Account’ account for the department.
Important: If you are using the data security feature for
 the 'bEmployee' datatype and have secured the PR Employees table (PREH) in VA Secure
 Tables and Datatypes), it will not affect posting in this program. This program uses the
 PREHName view, allowing for posting employee maintenance timecards, regardless of the
 employees to which the user has been given access. However, the amount of information
 provided by this view is minimal (i.e. PRCo, Employee, LastName, FirstName, MidName,
 SortName, ActiveYN, InsCode, PRDept, Craft, Class, JCCo, Job, EMFixedRate, Suffix, and
 Email).
