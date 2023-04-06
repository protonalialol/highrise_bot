$version = "v0.4.5"

.\destroydeploy.ps1

docker build -t highrisebot1 . --build-arg BOT_VERSION=$version
docker tag highrisebot1 "protonalialol/highrise_bot:$version"
docker push "protonalialol/highrise_bot:$version"

kubectl apply -f .\deployment.yaml
Start-Sleep 17
kubectl logs -f deployment/highrisebot