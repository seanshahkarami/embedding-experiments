# Embedding Experiments

This is just a placeholder for experiments I want to keep.

## Hover Example

This is an example of a "live preview" scatter plot. You just point it to some 2D embedding CSV you've created with `path`, `x`, `y` columns like:

```csv
path,x,y
/Users/sean/git/clustering-experiments/storage.sagecontinuum.org/api/v1/data/imagesampler-top/sage-imagesampler-top-0.3.0/000048b02d15bdaa/1676613622344516622-sample.jpg,10.954836,-80.4852
/Users/sean/git/clustering-experiments/storage.sagecontinuum.org/api/v1/data/imagesampler-top/sage-imagesampler-top-0.3.0/000048b02d15bdaa/1676894416538609108-sample.jpg,57.219654,-31.755716
/Users/sean/git/clustering-experiments/storage.sagecontinuum.org/api/v1/data/imagesampler-top/sage-imagesampler-top-0.3.0/000048b02d15bdaa/1677016816992384095-sample.jpg,-38.43397,53.8036
/Users/sean/git/clustering-experiments/storage.sagecontinuum.org/api/v1/data/imagesampler-top/sage-imagesampler-top-0.3.0/000048b02d15bdaa/1676970015415392590-sample.jpg,14.081677,-40.781773
/Users/sean/git/clustering-experiments/storage.sagecontinuum.org/api/v1/data/imagesampler-top/sage-imagesampler-top-0.3.0/000048b02d15bdaa/1676458816148552620-sample.jpg,23.879906,-69.15058
```

Then, you can view it with:

```sh
python3 hover_example.py path_to_embedding.csv
```
