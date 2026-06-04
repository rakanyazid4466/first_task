# First Task: URDF & Robot Modeling

This repository contains my deliverables for Week 1, focusing on URDF fundamentals, Xacro properties, and creating a custom 4-wheeled robot model.

## Project Description
I created a custom 4-wheeled robot model by setting up a lightweight, modular file structure. Instead of keeping everything in one file, I isolated the dimensions and physical constants into a dedicated properties file, allowing the primary robot description file to dynamically pull those parameters. 

The project consists of three core files:
* **`properties.xacro`**: Defines all the scalable robot configurations, dimensions, and mass parameters.
* **`robot.urdf.xacro`**: Contains the physical links, continuous wheel joints, and structural geometry of the 4-wheeled design.
* **`display.launch.py`**: The launch script configured to parse and execute the model.

### What I Learned
* **URDF Fundamentals:** Understanding the structural relationships between links, joints, and physical geometry in a robot description format.
* **Modular Xacro Design:** Separating constants and configurations into an isolated properties file to ensure clean, scalable code.
* **Extension-Based Visualization:** Utilizing the VS Code URDF Visualizer extension to instantly parse, render, and visually debug the robot configuration directly inside the development environment.

---

## How to View the Model

### File Structure
```text
first_task/
├── README.md
└── custom_robot_description/
    ├── CMakeLists.txt
    ├── package.xml
    ├── display.launch.py
    ├── properties.xacro
    └── robot.urdf.xacro