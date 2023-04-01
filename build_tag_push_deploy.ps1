$version = "0.0.5"

.\destroydeploy.ps1
docker build -t highrisebot1 .
docker tag highrisebot1 "protonalialol/highrise_bot:$version"
docker push "protonalialol/highrise_bot:$version"

kubectl apply -f .\deployment.yaml