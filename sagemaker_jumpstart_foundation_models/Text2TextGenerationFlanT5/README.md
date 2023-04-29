# SageMaker JumpStart Foundation Models - HuggingFace Text2Text Generation

This will use the notebook from aws/amazon-sagemaker-examples git repo [text2text-generation-flan-t5.ipynb](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/jumpstart-foundation-models/text2text-generation-flan-t5.ipynb)

## Pre-requisite
- AWS Accounts
- This will incur cost for AWS resources you use and also keep it running. To keep your cost at minimum you can always shutdown/tear down your systems. 

We will run notebook as per the instructions provided and then deploy to your AWS account. 

For deploying the REST API, we will be using 
- AWS Lambda
- Amazon API Gateway

## Few highlights to learn/know from Notebook 

**IPyWidgets** - **ipywidgets**, also known as jupyter-widgets or simply widgets, are interactive HTML widgets for Jupyter notebooks and the IPython kernel. [Ref](https://pypi.org/project/ipywidgets/)

example 
```
from ipywidgets import Dropdown
```

[FLAN-T5](https://huggingface.co/docs/transformers/model_doc/flan-t5) model comes with many variants based on the numbers of parameters. [Ref] (https://www.linkedin.com/pulse/small-overview-demo-o-google-flan-t5-model-balayogi-g)

- FLAN-T5 small
- FLAN-T5 base
- FLAN-T5 large
- FLAN-T5 XL
- FLAN-T5 XXL

**Multi-model endpoints** -  provide a scalable and cost-effective solution to deploying large numbers of models. They use the same fleet of resources and a shared serving container to host all of your models. This reduces hosting costs by improving endpoint utilization compared with using single-model endpoints. It also reduces deployment overhead because Amazon SageMaker manages loading models in memory and scaling them based on the traffic patterns to your endpoint. [Ref](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html)

