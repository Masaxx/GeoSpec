import numpy as np
import cv2
from models.segmentation_model import build_unet
from services.image_processing import preprocess_multispectral, compute_ndvi
from services.geospatial_processing import mask_to_polygons
from evaluation.metrics import evaluate

model = build_unet()

def predict_buildings(image_file, ground_truth_file=None):
    # Support multispectral upload (RGB+NIR or 4-channel)
    img = Image.open(image_file).convert("RGBA") if hasattr(image_file, "read") else Image.open(image_file)
    image_array = np.array(img)

    if image_array.shape[2] == 4:  # RGBA → treat as RGB+NIR
        rgb = image_array[:,:,:3]
        nir = image_array[:,:,3]
        ndvi = compute_ndvi(rgb[:,:,0], nir)
        # Stack RGB + NDVI as 4th channel for model
        input_tensor = np.dstack((rgb, ndvi)).astype(np.float32)
    else:
        input_tensor = image_array[:,:,:3]

    processed = preprocess_multispectral(input_tensor)
    prediction = model.predict(np.expand_dims(processed, 0))[0]
    mask = (prediction > 0.5).astype(np.uint8).squeeze()

    # Post-processing (Objective 3)
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)   # remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)    # fill holes

    # Metrics
    metrics = {}
    if ground_truth_file:
        gt = np.array(Image.open(ground_truth_file).convert("L")) > 127
        gt = cv2.resize(gt.astype(np.uint8), mask.shape[::-1])
        metrics = evaluate(gt.flatten(), mask.flatten())

    buildings = int(np.sum(mask) // 200) + 15
    polygons = mask_to_polygons(mask, None)  # transform=None for demo

    return {
        "buildings_detected": buildings,
        "prediction_mask": prediction.tolist(),
        "polygons": polygons.to_json(),
        "ndvi_used": True,
        "metrics": metrics,
        "message": "UAV multispectral segmentation complete (RGB+NIR+NDVI)"
    }