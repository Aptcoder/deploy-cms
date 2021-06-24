

### Analyze, choose, and justify the appropriate resource option for deploying the app.


*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

In terms of cost, Virtual machines tend to be more expensive than app services and given how this is a simple CMS, I do not see a reason to spend so much,hence I will pick a App service deployment in terms of cost.

In terms of scalabilty,the CMS doesn't have a lot of moving parts and by assumption won't be getting a lot of back to back requests hence might not need much compute resources. The VMs can adjusted using a vertical or horizontal scaling while scaling is also offered for app services with a compute resource limit.

In terms of availability, on a VM, the developer would have to manage the ensure the VMs are up at all time with app running as expected while for an app service deployment this is managed by the service.

In terms of workflow, deployments on VMs are more laborous compared to an app service deployent where you can use CI offering and deploy from online repositories without having to worry about the internals of the compute service

With respect to the analysis done above, I believe the appropriate solution for deploying the app is an App service solution.


An app service deployment will be cheaper giving how not much compute resources will be needed to keep the app going as it is lightweight. Using a app service reduces the amount of tasks left for the developer or deployment manager as he does not have to worry about managcompute resources ing the compute resources internals, operating system and security. An app service deployment provides a better workflow for deployments as deployments can be configured with CIs and testing carried out on the CIs before actual deployment. 


### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

A change in the complexity of the application such that more requests are bound to be coming in, and hence more compute capacity is needed which might exceed the  maximum for an app service 

A change in the level of security required by the CMS probably with change the information used might cause a change in decision to use a app service as for security considerations, using a VM would be better