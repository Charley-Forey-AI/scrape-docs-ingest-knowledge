---
title: "Enterprise Installation - Company tab | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/enterprise-management/enterprise-installation/enterprise-installation---company-tab"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/enterprise-management/enterprise-installation/enterprise-installation---company-tab"
---

# Enterprise Installation - Company tab

Use this screen to add and remove companies in order to create a general list for reference purposes.
This screen also allows you to apply cost centers on a company-by-company basis by selecting a company from the list and then selecting the Cost Centers button and selecting to use cost centers.
Regardless of whether the list includes one company or several companies, this screen provides a convenient way to view existing companies when new operators are being set up. System Administrators are not limited to using companies from this list; other companies may be created for unrelated purposes (for example, confidential purposes), and these companies do not need to be included here.
Important: Please see the [Cost Center Setup Considerations](/en/spectrum/spectrum/tools/enterprise-management/enterprise-installation/enterprise-installation---company-tab/understanding-cost-centers/cost-center-conversion-and-setup/cost-center-setup-considerations) before turning on cost centers in any company.
Once you apply cost centers to a company, you must use cost centers while in that company.
Fields / ButtonsDescriptions
Add Company buttonUse this button to add companies to the list. Enter a company code and company name in the window that displays; if the company code entered already exists, the company name will display. When a company is added, Spectrum determines whether the Company Installation settings have been recorded yet for this company. If so, no changes are recorded in the new company. If not, then settings in the Company Installation screen for the current company are copied into the new company.
Edit buttonSelect a record and then select this button to open the Edit Company Settings window. Use this window to apply cost centers on a company-by-company basis. If you choose to activate cost centers for a company, you must use them while in this company. Users who have access to only one cost center will notice no difference in how the software operates without cost centers.Important: Before you can use the cost center feature, the Use cost centers option must be set to Yes in this window.

Remove buttonSelect the company you wish to remove and then select this button. Removing a company here does not prevent other operators from accessing the company, nor does it delete company files.To remove company access for specific operators, go to the System Administrator > Security > Operator Maintenance > Edit Operator - Companies tab, select the company to remove and then select the Delete button.

Cost centers?An indicator of whether cost centers are in use for the given company.
Sample company?An indicator of whether the given company is serving as a sample company for testing purposes.

## Edit button

When you select Edit, the Edit Company Settings window appears.
Fields / ButtonsDescriptions
Use cost centersChoose whether cost centers are to be used in the given company. Selecting Yes enables the Cost center label and Cost group label fields.Note: Select Pending if you're still configuring cost center coding but want to allow data entry and reporting to function as if they were activated.

Options
Cost center label(Optional) Name the cost center.
Cost group label(Optional) Name the cost group. A cost center group is a collection of cost centers. For example, if you were using cost centers to represent different branch locations, you might enter "NE Region" or "SW Region" here.

Allow G/L account overrides by cost center?Select this checkbox if you want to enable G/L account overrides throughout the software.If you leave this checkbox clear:

- The Override buttons do NOT display in the module installation screens.

- The G/L Accounts tab on the Cost Center Maintenance screen is disabled.

Entity tracking?Select this checkbox if cost center entities are to be used in this company. If enabled, an Entities option is available from the Employee Info Bar and Authorized entity hyperlinks are available from applicable screens throughout the application.
Sample company?Select if the current company is to serve as a sample company for testing purposes.
