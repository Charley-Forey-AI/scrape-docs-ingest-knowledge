---
title: "Multiple Company Processing | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/about-the-main-menu/multiple-company-processing"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/about-the-main-menu/multiple-company-processing"
---

# Multiple Company Processing

The system is designed to allow multiple companies to be processed at the same time on
 one computer. This means that you can use the same software and yet keep totally separate sets
 of books for different business entities.
In addition to being able to process each of your companies
 separately, the software also has the capability to integrate certain portions of
 information in one company with another company’s information. Information about the
 different types of multiple company processing handled by the software is provided below.

## Consolidated Reporting

The simplest level of company integration allows you to
 combine data from multiple companies into a single report. This integration keeps each
 company’s files separate, but allows information to be combined on reports that you
 design.

## Shared Code Files

The next level of company integration is the sharing of code
 files. Some files are designed to be shared by all companies. These are known as
 ‘master’ files. Some of the master files used throughout the software include:

- HQ Compliance Codes

- HQ Earn Types

- HQ Frequency Codes

- HQ Liability Types

- HQ Payment Terms

- HQ Reviewers

- HQ State Codes

- HQ Units of Measure

There are also code files that are not ‘master’ files, yet can
 be set up to be shared by multiple companies. These files are set up by group. Groups
 are defined in HQ Groups and then assigned in HQ Company Setup to identify which code
 files the company will use. Code files of this type include:

- AR Customers

- AP Vendors and PM Firm Codes

- HQ Material Codes

- HQ Tax Codes and Rates

- JC Phase and Cost Types

- EM Cost and Revenue Codes

- EM Shops

Although you can set up your companies to use their own code
 files, sharing these files not only allows the designated companies access to the same
 codes, but also allows for setting up and maintaining the codes in any of the sharing
 companies. This can save you time, since you will not need to set up the same codes
 repeatedly for each new company you set up.

## Intercompany Processing

Intercompany accounting enables you to interface data entered
 in one company to another company. The accounting system uses both multi- and
 cross-company integration. In cross-company processing, you may only access one other
 company. In multi-company processing, you may access any of the other companies on your
 system. Because you control which company a module’s normal interfaces are sent to, it
 requires a carefully coordinated setup in the Company Parameters programs.

- Cross-Company – This type of processing allows you to
 interface with one specified company in another related module. An example of this
 is the one-to-one relationship between JC and AR. Billings or invoices posted to a
 job can only be updated to the AR company specified for the Job Cost company (in
 JC Company Parameters). (Note: This one-to-one relationship does not affect the
 ability to have multiple JC companies pointing to the same AR company.

- Multi-Company – This type of processing allows you to
 interface to any valid company in another related module. For example, you may
 have all your employees set up in one Payroll company, but the employees work on
 jobs set up in three different Job Cost companies. When posting timecards (in PR
 Timecard Entry), you specify the JC Co# to which each specific posting detail line
 will go.

Cross-company and multi-company setups will result in posted
 transactions that must update accounts in two General Ledger companies. To ensure these
 accounts balance in both companies, you must set up intercompany AR and AP accounts in
 GL Intercompany Accounts.
For example, the payroll in Co #1 updates a job in Co #2. In
 addition to the normal GL entries (for PR and JC), updates must also occur to the
 intercompany Receivable GL account in Co #1 and the intercompany Payable GL account in
 Co #2.

Related information

- [About the Main Menu](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/about-the-main-menu)
