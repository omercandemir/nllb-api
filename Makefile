all:
	docker build -f Dockerfile.build -t nllb-api .
	docker run --rm -e SERVER_PORT=7860 -p 7860:7860 nllb-api

gpu:
	docker build -f Dockerfile.cuda-build -t nllb-api .
	docker run --rm --gpus all -e SERVER_PORT=7860 -p 7860:7860 nllb-api

hf:
	docker build -t nllb-api .
	docker run --rm -p 7860:7860 nllb-api
