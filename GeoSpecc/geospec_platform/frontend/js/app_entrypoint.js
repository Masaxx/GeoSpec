// ================================================
// js/app_entrypoint.js
// Main entry point for GeoSpec Platform
// Initializes everything when the page loads
// ================================================

document.addEventListener("DOMContentLoaded", () => {
    console.log("✅ GeoSpec Platform - Initializing...");

    // Initialize the Leaflet Map (Analysis tab)
    if (typeof initializeMap === "function") {
        initializeMap();
        console.log("🗺️ Map initialized");
    }

    // Initialize Charts (Results & Quick Results sidebar)
    if (typeof initializeChart === "function") {
        initializeChart();
        console.log("📊 Charts initialized");
    }

    // Initialize all UI controls, buttons, and tab navigation
    if (typeof initializeUI === "function") {
        initializeUI();
        console.log("🎛️ UI controls & navigation initialized");
    }

    // Optional: Show welcome message on first load
    setTimeout(() => {
        const welcomeShown = localStorage.getItem("welcomeShown");
        if (!welcomeShown) {
            showNotification("Welcome to GeoSpec!\n\n" +
                "This platform implements the full workflow from your research proposal:\n" +
                "• UAV Multispectral Orthophoto Generation\n" +
                "• Semantic Segmentation using U-Net (RGB + NIR)\n" +
                "• NDVI calculation & Post-processing\n" +
                "• Accuracy Assessment (IoU, Precision, Recall, F1)");
            
            localStorage.setItem("welcomeShown", "true");
        }
    }, 800);

    console.log("🚀 GeoSpec Platform fully loaded and ready!");
});
