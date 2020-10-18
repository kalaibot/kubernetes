# kubernetes

This repository contains k8s manifest for all deployments in eks

#cpu metrics for hpa
1000 units - 1000m (milli cores)
1000 m = 1 cpu
If you have 4 cores, then the CPU capacity of the node is 4000m

#memory metrics for hpa
the Container is given a default memory request of 256 MiB and a default memory limit of 512 MiB.

