@app.route("/generate-orthophoto", methods=["POST"])
def generate_orthophoto():
    rgb = request.files["rgb"]
    nir = request.files.get("nir")
    ortho = orthophoto_processor.generate_orthophoto(rgb, nir)
    return jsonify({"status": "success", "orthophoto_shape": ortho.shape})

# /predict already exists – just make sure it calls the new predict_buildings