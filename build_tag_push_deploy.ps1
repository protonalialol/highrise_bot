$version = "0.0.7-test"

docker build -t highrisebot1 .
docker tag highrisebot1 "protonalialol/highrise_bot:$version"
docker push "protonalialol/highrise_bot:$version"

.\destroydeploy.ps1
kubectl apply -f .\deployment.yaml