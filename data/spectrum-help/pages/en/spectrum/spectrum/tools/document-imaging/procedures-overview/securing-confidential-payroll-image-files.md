---
title: "Securing Confidential Payroll Image Files | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/document-imaging/procedures-overview/securing-confidential-payroll-image-files"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/document-imaging/procedures-overview/securing-confidential-payroll-image-files"
---

# Securing Confidential Payroll Image Files

Images scanned in Confidential Payroll Timecard Entry are available for view to any operator that has security to run a Job Cost History Report in the Job Company.

## Solution

Add Job Company USERS to the Confidential Company with limited access to that company and limit the DI settings for that Operator in the Confidential Company.
The users being added will have no access to actually do anything in the Confidential PR Company; Level 1 in PA & no other module(s) is sufficient. In the [Document Imaging Installation - Security](/en/spectrum/spectrum/tools/document-imaging/installation-overview/document-imaging-installation---security) the operator's security can be set to a security level of 0, OR leave the operator's security at the default and add an Override to the EMPLOYEE Cabinet with a level of 0.

## Results

Any operator set up this way in the Confidential Company will no longer have access to view the time card images for Summary Transaction postings from the Confidential Company. They will see the "Summary Transaction" description, but there is no link to the scanned image. They will, however still be able to view transactions scanned in the regular Job company for Payroll.
Nothing needs to be done to those operators that you DO want to be able to view images from the Confidential Payroll in the regular company.
