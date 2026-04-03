---
title: "Which Business Issues Do Cost Centers Solve? | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/installation/cost-centers/which-business-issues-do-cost-centers-solve"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/installation/cost-centers/which-business-issues-do-cost-centers-solve"
---

# Which Business Issues Do Cost Centers Solve?

Cost centers provide critical business functionality.
In the most basic terms, cost center functionality provides:

- Flexible financial statement and reporting tools

- Data entry validation

- Transactional-based security

## Flexible Financial Statement and Reporting Tools

While transactional data is captured at the lowest level by cost center, reporting is done at the group level. This means that changes in your reporting requirements do not necessitate a restatement of all your historical data. Instead, you simply create new reporting groups to accommodate your new reporting needs.
What Are Cost Groups?
Cost groups are a collection of cost centers or a collection of other cost groups. While transactional data is captured at the lowest level by cost center, reporting is done at the group level. This means that changes in your reporting requirements do not necessitate a restatement of all of your historical data. Instead, you simply create new groups to accommodate your new reporting needs.
For example, groups can be used to define the cost centers that comprise a branch location. Think of cost groups as the building blocks for your reports. Moving the blocks around doesn't change the underlying data, but allows you to present it in different ways. If the company reorganizes, they can just create a new group of cost centers to represent the new structure. Instead of changing the underlying data, we instead change the definition of the "responsibility group."
Because cost groups can be created or modified at any time, the structure remains flexible as the organization grows and changes.

## Data Entry Validation

Cost centers provide validation during data entry as well--only transactions that are valid for a cost center are allowed. Except in a few instances, the cost center will default in automatically based on hierarchy rules. This helps the data entry user by eliminating the need for any extra key strokes.
The type of element determines whether or not the cost center defaults in automatically. The term element is used to indicate a type of data associated with a cost center.

## Transactions with Defaulting or Assigned Cost Centers

Transactions for elements with assigned cost centers will automatically default in the proper cost center. The cost center owns the element. The element "owns" the transaction. For example, when entering an A/P invoice to a job, the job's cost center will automatically default. This means that only charges to that job's cost center will be allowed.
While this is similar to the "auto-default job division to G/L department" feature, cost centers use this logic throughout Spectrum on all transactions, not just direct job cost ones. It also reduces one keystroke as you do not have to click away the "Changing G/L code department to match job division" warning message.
These elements have an Assigned Cost Center:

- Job

- Employee

- A/R Contract

- Payroll Department Expense

- Equipment

- Fixed Asset Department

- Inventory Warehouse

- Inventory G/L Department

- Work Order Site

These elements have an Optional Cost Center:
These are used to override the cost center on the Assigned Cost Center elements.

- Phase

- Equipment Cost Category

- Fixed Asset

Spectrum first looks to see if there is an optional cost center on the phase, cost category code or fixed asset code. If one is found, it defaults in. If not, then it defaults in the cost center of the job, equipment, or fixed asset department.

## Transactions with User-entered or Shared Cost Centers

Certain types of transactions are allowed across cost centers. Typically, these are activities that are indirect in nature and the user is prompted to enter the appropriate cost center. For example, when entering an A/P invoice for office rent, the user is prompted to enter the cost center that will incur the charge.
These elements may have a Shared Cost Center

- G/L Account

- Vendor

- Customer


- Payroll Deduction & Add-on

- Cash Management Bank

- Human Resources Location

- Inventory Item
 Note: Most transactions default in the appropriate cost center. Only transactions that do not include elements with assigned or optional cost centers will require entry. This saves data entry time and reduces errors.

The cost center functionality found in Spectrum allows companies to share certain information with others in the company without sharing all information. Cost centers can be configured to provide access to records for one group and yet restricted for others.
Cost centers control access to the management information within Spectrum. Users can print reports that contain only information associated with the cost centers they are assigned. Information associated with cost centers that users are not assigned to is automatically suppressed. This feature saves time when evaluating information contained within reports and inquiries because only the relevant information is included.
How does security work with the different types of elements?
Remember that elements can be assigned, shared, or optional when it comes to cost centers.
Assigned elements always require a cost center, thus enforcing security. There are times that this may be too restrictive, so there are ways to override this general rule. Certain elements are optional and can be used to override the main element's cost center on an as-needed basis. These overrides to the general rule provide greater flexibility and control.
An example of this is the phase code. It is optional to enter a cost center on a job-phase-cost type combination, but if you do, it supersedes the cost center on the job. When no cost center exists at the phase level, the job's cost center is used.
If the cost center for the phase is different than the cost center for the job, the user will need security access to both cost centers in order to "see" the information on the phase.
Additional overrides are available, but they are outside the scope of this session. Accounting and security overrides can be configured as desired.

Related information

- [Are Cost Centers Right for You?](/en/spectrum/spectrum/system-administration/installation/cost-centers/are-cost-centers-right-for-you)

- [Cost Center Implementation Overview](/en/spectrum/spectrum/system-administration/installation/cost-centers/cost-center-implementation-overview)
