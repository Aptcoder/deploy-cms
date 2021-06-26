

### Analyze, choose, and justify the appropriate resource option for deploying the app.


*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*


Analysis for costs 

| Vm | App service |
|-----|----------|
| The averga Vm costs about $0.5 per hour | The lowest possible plan for an app service is the free plan though limited |
| Costs for an engineer who would manage the instance, occasionally make upgrades to the underlying infrastructure | Azure manages upgrades along with payment with the service |
| You pay for the VMs as you go | You make payment for a plan before getting access |



Analysis for scalability 

| Vm | App service |
|-----|----------|
|In other to implement load balancing azure load balancer will have to be used |load balancing is a inbuilt feature with azure app service |
|Vertical scaling would require getting a new instance a redeploying app |Vertical scaling can be done without a need to redeploy
|


Analysis for availability

| Vm | App service |
|-----|----------|
| Azure guarantees around 99.9% up time for all VM deployments | Basic plans do not get Uptime guarantees but other apps running on subcription get a 99.5% uptime guarantee |
| Vms utilize azure traffic manager | App services utilize the traffic manager |
| An engineer is required to manage the availabilty of infrastructure | Underlying infrastructure is managed by azure |

Analysis for workflow

| Vm | App service |
|-----|----------|
|change of development stack is possible since you have access to the underlying os | Deployment stack is configured during the creation of the service |
|deployments have to be done manually by going into the VM or manually setting up CI | instant deployments using remote repositories and CI |


With respect to the analysis done above, I believe the appropriate solution for deploying the app is an App service solution.


An app service deployment will be cheaper giving how not much compute resources will be needed to keep the app going as it is lightweight. Using a app service reduces the amount of tasks left for the developer or deployment manager as he does not have to worry about managcompute resources ing the compute resources internals, operating system and security. An app service deployment provides a better workflow for deployments as deployments can be configured with CIs and testing carried out on the CIs before actual deployment. 


### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

A change in the complexity of the application such that more requests are bound to be coming in, and hence more compute capacity is needed which might exceed the  maximum for an app service 

A change in the level of security required by the CMS probably with change the information used might cause a change in decision to use a app service as for security considerations, using a VM would be better