**Human Fall Detection and Activity Monitoring System**

An ML-based fall detection system with 90%+ accuracy that monitors human activities, detects fall incidents, and provides comprehensive analytics and risk assessment.


**Features**


🎯 **Core Capabilities**

Fall Detection: Detects fall incidents with high accuracy using ensemble ML models

Activity Classification: Classifies activities into walking, standing, sitting, and falling

Real-time Monitoring: Live dashboard with automatic updates

Advanced Analytics: Detailed visualizations and trend analysis


🤖 **Machine Learning**

Models: Random Forest, SVM, and KNN ensemble

Accuracy: ~90% average accuracy across models

Features: Accelerometer and gyroscope magnitude analysis


📊 **Dashboard Features**

Real-time Activity Monitoring: Total activities, fall incidents, fall rate, system status


**Technology Stack**

Backend: REST API, Firebase, scikit-learn, pandas, numpy 

Frontend: Flask, CSS


**Data Format**
CSV/JSON with columns: acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z


**API Endpoints**

GET /api/ - API status

GET /api/falls - Fall incidents


**ML Model:** ~90% avg accuracy (RF: 90.5%, SVM: 86.1%, KNN: 86.7%)
