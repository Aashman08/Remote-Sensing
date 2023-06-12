#  Remote Sensing Project: Differentiating Healthy and Unhealthy Vegetation using NDVI

### Description:
This remote sensing project aimed to distinguish between healthy and unhealthy vegetation by utilizing the NDVI (Normalized Difference Vegetation Index) calculation. NDVI is a widely used index in remote sensing that provides valuable insights into the health and vigor of vegetation based on the absorption and reflection of radiation.

### Objective:
The primary objective of this project was to develop a method for identifying and classifying healthy and unhealthy vegetation areas using NDVI. By leveraging image data and applying the NDVI calculation, I could effectively detect the vegetation's health status and monitor changes over time.

### Methodology:

Data Collection:
Captured images using a drone based system built from scratch equiped with infra-red and a normal RGB camera

Preprocessing: The acquired imagery undergoes preprocessing steps, extarcting only relevant band data. More advanced system can be put to use such as radiometric calibration, atmospheric correction, and geometric alignment, to remove noise and improve data quality.

NDVI Calculation: The NDVI is computed by analyzing the Near-Infrared (NIR) and Red bands of the acquired imagery. The formula for NDVI is (NIR - Red) / (NIR + Red), where NIR represents the Near-Infrared band and Red represents the Red band.

Visualization:
Created a false color image to show differnece and quantity of vegetation in a given area. 

Findings and Conclusion:
Through the implementation of the proposed methodology, this project successfully differentiates healthy and unhealthy vegetation using NDVI. The calculated NDVI values serve as indicators of vegetation health, where higher values typically correspond to healthier vegetation and lower values represent unhealthy or stressed vegetation.

By visualizing the classified areas, patterns of unhealthy vegetation, such as drought-affected regions or areas affected by pests or diseases, can be identified. This information is valuable for land management, precision agriculture, and environmental monitoring.

This project not only provides a practical application of remote sensing and NDVI analysis but also offers a foundation for further research in vegetation health monitoring and the development of automated systems for large-scale vegetation analysis. Further, this project was completed in under $1000 and can be used as an alternative to commercialy available services for farms and small coorporation willing to invest in their own systems.
