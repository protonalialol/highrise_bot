$version = "v1.0.4"

kubectl delete deployment highrisebot
docker build -t highrisebot1 .
docker tag highrisebot1 "protonalialol/highrise_bot:$version"
docker push "protonalialol/highrise_bot:$version"

kubectl apply -f .\deployment.yaml