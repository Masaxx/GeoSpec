class SatelliteDataAPI:
    def get_sentinel2_data(self, bbox, date_range):
        # Mock Sentinel-2 response (real API would need credentials)
        return {
            "status": "success",
            "message": "Satellite imagery fetched (demo mode)",
            "imagery": {
                "url": "https://picsum.photos/id/1015/800/600",  # placeholder image
                "bbox": bbox,
                "date_range": date_range,
                "bands": ["B2", "B3", "B4", "B8"],
                "resolution": "10m"
            }
        }