---
title: "Cost Centers | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/installation/cost-centers"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/installation/cost-centers"
---

# Cost Centers

The term cost center describes a division, location, branch, or other subset of the company that has its own processing needs while relying on shared information from one or more other cost centers.
Cost centers are used by companies with multiple
 divisions/locations/branches (or any other company-defined sub-category) to share selected
 company records with others — without sharing all of the branch-specific records.

## Benefits of Cost Centers

- User-Defined Terminology Within Spectrum Enterprise, you define the meaning of the cost center; this meaning is then used throughout the system. For example, let's assume that you want to title your cost centers as profit centers; anytime you see a cost center field it will be labeled as such. Likewise, you then define what you are going to call a group of cost centers. Your labels appear throughout the system.

- Enforce Accounting Policies Cost centers are used to enforce your accounting policies as only transactions for authorized cost centers will be allowed. While similar to the "auto default job division to G/L department" feature, this happens throughout Spectrum.

- Streamline Your Chart of Accounts Utilizing cost centers can simplify your chart of accounts by eliminating duplicate accounts that have been set up for other departments. Instead of having 30 different G/L codes set up for Direct Labor, have one code set up with 30 cost centers. This makes it easier on those who enter transactions into Spectrum.

- Multiple Company Features with Single Company Flexibility Cost centers provide the security, selection, and validation features currently available when using multiple Spectrum companies, while providing the added flexibility of being able to share data and report across companies. Each cost center is balanced (debits and credits equal) through the use of an intra-cost center account. Each cost center is treated as if it were a unique company, yet vendors, customers, employees, and other maintenance files can be shared among the cost centers.

- Effectively Increases the G/L Length Cost centers can also be considered a tool for increasing the length of the G/L structure. Every G/L account code used in Spectrum will be posted to General Ledger with a cost center assigned to it. This provides a coding structure up to 25 digits long, where the first 3 digits represent the company code, the next 12 digits represent the G/L account code, and the final 10 digits represent the cost center.
Note: Why not just make the G/L mask larger? Because this gives you flexibility to have up to 25 digits in your coding structure while not requiring entry of all 25 digits during data entry. Instead, only the G/L code is entered, and the company code and cost center portions of G/L structure automatically default.

Related information

- [Which Business Issues Do Cost Centers Solve?](/en/spectrum/spectrum/system-administration/installation/cost-centers/which-business-issues-do-cost-centers-solve)

- [Are Cost Centers Right for You?](/en/spectrum/spectrum/system-administration/installation/cost-centers/are-cost-centers-right-for-you)
