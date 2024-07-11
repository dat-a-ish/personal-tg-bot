.PHONY: all login_to_ecr deploy_base

all: login_to_ecr deploy_base

login_to_ecr:
	aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws

deploy_base:
	docker buildx build -f base/Dockerfile -t public.ecr.aws/b4k2g9f3/egor-bot:latest --platform=linux/amd64 .; \
	docker push public.ecr.aws/b4k2g9f3/egor-bot:latest
