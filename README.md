# Concrete Crack and Depth Detection using Deep Learning

A Flask web app that detects cracks in concrete surface images and estimates how severe they are. A CNN classifies each uploaded image as cracked or uncracked with a confidence score. For cracked images, a lightweight U-Net-style model predicts a depth-intensity map, and the app projects it forward to 1, 5 and 10 years and plots the growth.

## Features
- Image upload with crack / no-crack classification and confidence score
- Depth-intensity heatmaps for cracked images
- Illustrative 1/5/10-year depth growth projection and graph
- User registration, login and profile pages
- Prediction history stored in SQLite

## How it works
1. **Classifier:** a PyTorch CNN trained on SDNET2018 images (64x64) labels each image as cracked or uncracked.
2. **Depth model:** a lightweight U-Net-style encoder-decoder trained on 3,000 crack images predicts a depth-intensity map. SDNET2018 has no depth labels, so training targets were generated with OpenCV Canny edge detection and Gaussian blur. Training MSE fell from 0.0273 to 0.0042 over 10 epochs (see `crack.ipynb`).
3. **Projection:** the depth map is scaled by `1 + 0.06 x years` for 1, 5 and 10 years and shown as heatmaps and a growth graph.

## Tech stack
Python, PyTorch, OpenCV, Flask, SQLite, NumPy, Matplotlib, HTML/CSS

## Project structure
```
app.py                       Flask app and model inference
train_classifier.py          Trains the crack classifier
predict_test.py              Quick prediction test script
crack.ipynb                  Depth model training notebook
sdnet_classifier.pth         Trained classifier weights
sdnet_fast_depth_model.pth   Trained depth model weights
init_db.py                   Creates the SQLite tables
templates/  static/          Web pages and assets
```

## Dataset
Download SDNET2018 from the official Utah State University page (https://digitalcommons.usu.edu/all_datasets/48/) and place the `SDNET2018/` folder in the project root to retrain the models. It is not included in this repo because of its size.

## Limitations
- The depth output is a crack-intensity estimate, not measured depth, because the training targets come from edge detection.
- The 1/5/10-year projection uses a fixed assumed growth rate (6% per year). It is illustrative, not a trained forecast.
- This is a learning project and not a substitute for a professional structural inspection.
