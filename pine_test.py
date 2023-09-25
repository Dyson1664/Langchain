import pinecone

pinecone.init(
	api_key='4d33ec05-5575-441b-8df5-4cba62aa2e19',
	environment='us-west4-gcp-free'
)
index = pinecone.Index('p1')