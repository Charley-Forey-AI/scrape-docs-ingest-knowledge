---
title: "Frequently Asked Questions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-contracts/frequently-asked-questions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/service-contracts/frequently-asked-questions"
---

# Frequently Asked Questions

FAQs to help while using Service Contracts.

## What options do I have to recognize revenue for Service Contracts?

- Straight Line Across Fiscal Periods Here, revenue is recognized evenly over the life of the contract. In other words, the amount recognized is calculated by taking the contract value divided by the number of fiscal periods.

- Apportioned by the Scheduled Visit Dates Revenue is recognized by allocating revenue over the life of the contract by dividing the total contract amount by the number of scheduled visits, and then assigned the apportioned amounts to the fiscal periods in which the visits are scheduled.

- Apportioned by the Budgeted Cost of Scheduled Visits With this basis method, revenue is recognized over the life of the contract by proportionally dividing the total contract amount by the budgeted cost of scheduled visits, and then assigning the apportioned amounts to the fiscal periods in which the visits are scheduled.

- As Billed When this basis method is used, revenue is recognized when the Service Contract is invoiced.

- Other Basis To utilize this method, the user will manually modify the deferred revenue schedule.

## What is the difference between earned revenue and deferred revenue?

Earned Revenue: The portion of the total contract amount that has been booked as revenue in the General Ledger.
Deferred Revenue: The portion of the total contract amount that is not recognized at the outset of a contract (or for an on-going contract, the portion of contract amount not yet recognized).

## How can I set a default earned revenue basis for my service contract?

Use the Contract Type File Maintenance screen to define the default earned revenue method for this type of contract.

## What does "WARNING – New earned revenue basis requires you to build the deferred revenue schedule. Click OK to start the build or Cancel to revert to the prior basis" mean?

This message will appear when both these conditions exist:

- You try to exit the screen after changing from the "As Billed" method to any other method.

- There are already G/L Distribution History records for this contract.

Since you are changing the earning methodology, the deferred revenue schedule must be setup accordingly. When switching from "As Billed", the software will determine if there are any earned revenue G/L distribution records already present for this contract. If there are, you will be required to perform the "Build Schedule" process in order to reset the earned revenue basis.
Note: Please consult with your outside accountant or CPA before changing earned revenue methodologies.

## Why am I getting a message saying that I am not allowed to change the earned revenue basis?

This error message will appear when the user attempts to change the Contract Type or the Earned Revenue Basis under the following situations:

- As Billed: If the current basis is "As Billed", then the Contract Type must be set to "Allow As Billed" revenue recognition. This error message will appear when this is not the case.

- Not As Billed: If the current basis is not "As Billed", then the Contract Type must be set to "Allow Scheduled Deferred Revenue Processing for this Contract Type." This error message will appear when this is not the case.

## What does "WARNING – This contract type is not authorized for the current earned revenue basis" mean?

This error message will appear when the user attempts to change the Contract Type or the Earned Revenue Basis under the following situations:

- As Billed: If the current basis is "As Billed", then the Contract Type must be set to "Allow As Billed" revenue recognition. This error message will appear when this is not the case.

- Not As Billed: If the current basis is not "As Billed", then the Contract Type must be set to "Allow Scheduled Deferred Revenue Processing for this Contract Type." This error message will appear when this is not the case.

## Why am I seeing the Unscheduled Deferred Revenue window?

The total of the scheduled transactions does not equal the total contract amount. In other words, the total deferred revenue on the schedule does not tie to the contract amount. To resolve, select the "Build schedule" option to create the schedule or select "Enter deferred revenue" to return to the Billing tab where you can modify the deferred revenue value.

## How do I correct "ERROR – Contract end date must be within the current fiscal calendar before calculating the schedule. Contract your Controller to extend the calendar date range"?

This error indicates that the end date of the service contract is not found on the G/L Fiscal Calendar. To resolve this error message, simply go to General Ledger > Period End > Fiscal Calendar Maintenance and select Add Year.

## What is the "Mid-month" convention?

When using the straight-line method this accounting rule assumes that the service contract was created in the middle of the month. This means that in the first month half of the revenue will be earned.
Note that a 12 month contract is really 13 periods.

- Period 1: 50% of the monthly amount.

- Period 2: 100% of the monthly amount.

- Period 3: 100% of the monthly amount.

- Period 4: 100% of the monthly amount.

- Period 5: 100% of the monthly amount.

- Period 6: 100% of the monthly amount.

- Period 7: 100% of the monthly amount.

- Period 8: 100% of the monthly amount.

- Period 9: 100% of the monthly amount.

- Period 10: 100% of the monthly amount.

- Period 11: 100% of the monthly amount.

- Period 12: 100% of the monthly amount.

- Period 13: 50% of the monthly amount.

## How is the Mid-Month convention applied to Service Contracts?

- 1st of the Month Start Dates: Service contracts that start on the first day of the month will not have the Mid-Month convention applied to them. As the contract starts on the first day of the month, the entire month's worth of revenue will be recognized.

- 2nd through 31st Start Dates: The Mid-Month convention is used for any service contract that does not start on the first day of the month. Tip: If your company elects to not utilize the Mid-Month convention, set the service contract start date to the first day of the month.

## Which earned revenue basis will be used when I activate a Proposed Contract?

The newly activated contract will use the earned revenue basis based on its Contract Type. The default earned revenue basis is defined in Contract Type File Maintenance.

## Does the Renew Service Contract option build the Earned Revenue Schedule on the new contract?

Yes, the Earned Revenue Schedule is automatically built based on the earned revenue basis you define in the Renew Service Contract window. While this method will default from the expired contract, you can override it if desired.

## How does the Renew Service Contract determine the Schedule G/L begin date?

The system will either use the contract's Start Date or the current Service Contract Processing Date, which ever is later.
 In the unusual case where the minimum Service Contract Processing Date is later than the End Date of the contract, then the End Date will serve as the Schedule G/L begin date. Here the entire contract amount will occur in the last day of the contract.

## Does the Copy Contract option build the Earned Revenue Schedule on the new contract?

Yes, the Earned Revenue Schedule is automatically built based on the earned revenue basis you define in the Copy Contract window. While this method will default from the expired contract, you can override it if desired.
Tip: Use the Copy Contract feature to create new Service Contracts from a template. It may be desirable to set the Earned Revenue Basis on the template contract to Other. During the Copy Contract Update, the user will be prompted to enter the appropriate Earned Revenue Basis for the new contract.

## Can I create new service contracts from a template?

Yes, use the Copy Contract feature to create new Service Contracts from a template.
Tip: If you want the user to define the Earned Revenue Basis each time they use the Copy Contract feature, simply set the method to Other. During the Copy Contract Update, the user will be prompted to enter the appropriate Earned Revenue Basis for the new contract.

## What is the difference between Actual and Standard Cost?

- Actual cost: This method is recommended for companies using "direct work order costing" accounts.

- Standard cost: This uses estimates and standards – backwards compatibility.

## How do I record Extra Work on a Service Contract?

Extra work is defined as work order billing amounts (including Labor, Material, Other Charges and Flat rate tasks) that reference the service contract # in the work order transaction detail. Create a new work order for the site in the Work Order module. When you enter labor, material and other charges, enter the service contract number for each transaction you want to bill for. You also mark the 'Bill customer for this entry' checkbox.

## Why won't my components copy over to a new Site's Service Contract when I use the Copy button?

Components are smaller pieces of equipment on your main piece of equipment. This is primarily done for warranty tracking. While two different sites will have the same equipment (either matching on the equipment code or equipment type), it will not normally be the case that the components will be numbered the same.
When setting up components, a sequential numbering system is used to keep track of these smaller pieces of equipment. The system does not require the user to create a maintenance list of component codes, thus it is possible that the components will be setup with different codes.
For example, assume that you have entered three components into Site A's blower motor in this order:

- 01-motor

- 02-fan blade

- 03-fan housing

When you set up components on Site B's blower motor, they were set up as:

- 01-fan blade

- 02-motor

- 03-fan housing

Because the system does not require you to create a maintenance list of these codes, it is not possible to copy them from one site + equipment to another.
