from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/1sh4ylh7lyop/Llama/workflows/workflow-eb5b16"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="e833d0e91eca4173b9aaf25e2bf51a3a"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)

