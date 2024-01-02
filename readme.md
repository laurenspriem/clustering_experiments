This repository was used for testing clustering approaches for embeddings of faces, for my thesis within the context of an ADR study with [Ente Photos](https://ente.io). The tests are done on our private photo libraries, which we first indexes in the Ente app and then exported here. For these reasons, it is not possible to show the results from our tests. To still demonstrate the clustering, see the demonstration below on data from the LFW dataset that we indexed.

## Demonstration

For demonstration purposes, we can use the LFW dataset. We indexed the dataset in the Ente app and exported the resulting face crops and embeddings here.
The clustering can be viewed by running the `lfw_demonstration.ipynb` notebook. Afterwards, the resulting clusters are in `/data/lfw_demonstration_data/caches/new_clusters/thumbnails_clusters`.

In short:
- Run the `lfw_demonstration.ipynb` notebook
- View cluster results in `/data/lfw_demonstration_data/caches/new_clusters/thumbnails_clusters`
