# 🛰️ CubeSat Real-Time Tracker & Attitude Visualizer

A **real-time CubeSat visualization system** that combines **orbital tracking (TLE + SGP4)** with **live attitude (IMU roll–pitch–yaw)** using **CesiumJS**, **Three.js**, and **MQTT**.

This project simulates a **ground-station → satellite → web-visualization pipeline**, suitable for CubeSat missions, research demos, and telemetry dashboards.

---

## 🚀 Features

### 🌍 Orbital Tracking
- Live orbit propagation using **SGP4** + **TLE**
- Smooth satellite trajectory with **1-orbit past & future trail**
- Ground coverage footprint visualization
- World, Satellite, and 2D map views

### 🧭 Attitude (Orientation) Visualization
- Real-time **roll / pitch / yaw** via MQTT
- Accurate **ENU → ECEF quaternion mapping**
- IMU-driven model rotation (not velocity-based)
- Axis-sign correction supported for real sensors

### 🛰️ 3D Visualization
- **CesiumJS** for Earth, orbit, and space context
- **GLB CubeSat model** with fallback
- Mini satellite POV window
- Lighting synchronized with Earth day/night

### 🔌 Telemetry Pipeline
- MQTT over WebSockets (HiveMQ public broker)
- Retained TLE publishing
- High-rate IMU streaming (10–20 Hz)
- Stateless browser clients (auto-recover)



