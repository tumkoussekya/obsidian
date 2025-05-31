### 2. Intermediate COCOMO Model

The basic COCOMO model assumes that the effort is only a function of the number of lines of code and some constants evaluated according to the different software systems. However, in reality, no system’s effort and schedule can be solely calculated based on Lines of Code. For that, various other factors such as reliability, experience, and Capability. These factors are known as ****Cost Drivers (multipliers)**** and the Intermediate Model utilizes 15 such drivers for cost estimation.

*Intermediate COCOMO Model equation:*

> E = a*(KLOC)b * EAF PM
> 
> Tdev = c*(E)d
> 
> Where,
> 
> - E is effort applied in Person-Months
> - KLOC is the estimated size of the software product indicate in Kilo Lines of Code
> - EAF is the Effort Adjustment Factor (EAF) is a multiplier used to refine the effort estimate obtained from the basic COCOMO model.
> - Tdev is the development time in months
> - a, b, c are constants determined by the category of software project given in below table.

| Software Projects | a   | b    | c   | d    |
| ----------------- | --- | ---- | --- | ---- |
| Organic           | 3.2 | 1.05 | 2.5 | 0.38 |
| Semi-Detached     | 3.0 | 1.12 | 2.5 | 0.35 |
| Embedded          | 2.8 | 1.20 | 2.5 | 0.32 |

### 3. Detailed COCOMO Model

Detailed COCOMO goes beyond Basic and Intermediate COCOMO by diving deeper into project-specific factors. It considers a wider range of parameters, like team experience, development practices, and software complexity. By analyzing these factors in more detail, Detailed COCOMO provides a highly accurate estimation of effort, time, and cost for software projects. It’s like zooming in on a project’s unique characteristics to get a clearer picture of what it will take to complete it successfully.
