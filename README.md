# Lemay.ai-Interview-part2 - Model Deployment Demonstration

Reason for choosing this Model:-

The distilbert-base-cased-distilled-squad Question Answering Model was my top choice due to its lightweight nature, making it easy to deploy and run on various systems. This model is also quite popular in the NLP community, which means that there is a wealth of resources and support available for it. In addition to its popularity, the distilbert-base-cased-distilled-squad model is also highly efficient, allowing for faster inference times and lower resource usage. Overall, the distilbert-base-cased-distilled-squad Question Answering Model was the ideal choice for my project, offering a balance of performance, efficiency, and ease of use.


Instructions:
1. Clone the repository
2. Build docker image using command "docker build -t huggingface-demo ."
3. Create a container using docker image with the following command "docker run -p 8000:8000 huggingface-demo"
4. Open file "mynotebook.ipynb" and run all cells to make a request and receive a response
