# k8s-talk
Code/exercises for my k8s talk. Relies heavily on the [official k8s python library](https://github.com/kubernetes-incubator/client-python)

## pytest
Pytest folder contains stub tests intended to be ran using pytest. Where possible there's hints given on what routes to follow
in the documentation, but other than the first test it's intended you write the code to get the test to pass/fail as expected.

## minikube
Minikube folder contains a dockerfile and k8s manifest file for deploying runner.py as a deployment into kubernetes. Given runner contains
some of the code/concepts needed to work in the pytest folder, it's advised you do the pytest section first to get to grips with k8s concepts
as a programmer.