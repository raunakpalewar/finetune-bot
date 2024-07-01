from django.shortcuts import render
from openai import OpenAI

def finetunebot(request):

    api_key='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'
    client = OpenAI(api_key=api_key)

    client.files.create(
    file=open("/content/drive/MyDrive/x/india4.jsonl", "rb"),
    purpose="fine-tune"
    )


    api_key = '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'
    client = OpenAI(api_key=api_key)

    # Fine-tune the model
    file = client.files.create(
    file=open("/content/drive/MyDrive/x/india4.jsonl", "rb"),
    purpose="fine-tune"
    )

    # Create a fine-tuning job
    fine_tune_job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-3.5-turbo"
    )

    # Wait for the fine-tuning job to complete
    fine_tune_job_id = fine_tune_job['id']
    fine_tune_result = client.fine_tuning.jobs.retrieve(fine_tune_job_id)


    while fine_tune_result['status'] == 'in_progress':
        fine_tune_result = client.FineTune.retrieve(fine_tune_job_id)

    # Once fine-tuning is complete, use the fine-tuned model for generating responses
    fine_tuned_model_id = fine_tune_result['model']
    prompt = "Tell me about the culture of India."

    response = client.Completion.create(
    model=fine_tuned_model_id,
    prompt=prompt,
    temperature=0.7,
    max_tokens=150,
    )

    generated_response = response['choices'][0]['text']
    print("Generated Response:", generated_response)

    # Analyze the performance of the fine-tuned model
    analysis_result = client.FineTune.analyze(fine_tune_model_id)
    print("Analysis Result:", analysis_result)

    # Example code for checking existing fine-tuning jobs
    fine_tuning_jobs = client.fine_tuning.jobs.list()

    # Print job details
    for job in fine_tuning_jobs:
        print(job.id, job.status)


    api_key = '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'
    client = OpenAI(api_key=api_key)

    # Upload your training data
    file = client.files.create(
    file=open("/content/drive/MyDrive/x/india4.jsonl", "rb"),
    purpose="fine-tune"
    )

    # Create a fine-tuning job
    fine_tune_job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-3.5-turbo"
    )

    # Monitor the status of the fine-tuning job
    fine_tune_job_id = fine_tune_job.id
    fine_tune_result = client.fine_tuning.jobs.retrieve(fine_tune_job_id)

    # Wait for the fine-tuning job to complete
    while fine_tune_result['status'] == 'in_progress':
        fine_tune_result = client.fine_tuning.jobs.retrieve(fine_tune_job_id)

    # Get the fine-tuned model ID
    fine_tuned_model_id = fine_tune_result['fine_tuned_model']

    # Now, you can use the fine-tuned model for generating responses
    prompt = "Tell me about the culture of India."
    response = client.Completion.create(
    model=fine_tuned_model_id,
    prompt=prompt,
    temperature=0.7,
    max_tokens=150,
    )

    generated_response = response['choices'][0]['text']
    print("Generated Response:", generated_response)

    # Analyze the performance of the fine-tuned model
    analysis_result = client.fine_tuning.analyze(fine_tuned_model_id)
    print("Analysis Result:", analysis_result)

