from django.shortcuts import render
from django.http import HttpResponse
import boto3
from decouple import config


def invoke_lambda_function():
    client = boto3.client('lambda', region_name= config('region_name'), aws_access_key_id= config('aws_access_key_id'), aws_secret_access_key= config('aws_secret_access_key'))
    response = client.invoke(
        FunctionName='lambdafunction',
        InvocationType='RequestResponse'
    )
    return response['Payload'].read()


def invoke_lambda_function_django(request):
    if request.method == 'POST':
        response = invoke_lambda_function()
        return HttpResponse(response)
    else:
        return render(request, 'app/index.html')