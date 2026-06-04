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
All source code, package manifests, and launch files are organized cleanly within the following structure:

```text
first_task/
├── README.md
└── urdf.rviz
└── custom_robot_description/
    ├── CMakeLists.txt
    ├── package.xml
    ├── display.launch.py
    ├── properties.xacro
    └── robot.urdf.xacro
    

# Build and Execution Instructions

Follow the steps below to clean, compile, and run the robot visualization environment.

## 1. Clean and Compile the Workspace

Navigate to your ROS 2 workspace root directory, remove previous build artifacts, and compile the required package:

```bash
cd ~/workspaces
rm -rf build/ install/ log/
colcon build --packages-select custom_robot_description
```

## 2. Source the Environment

Overlay the newly built packages onto the current terminal session:

```bash
source install/setup.bash
```

## 3. Launch the Robot Description

Run the unified launch file to start the ROS 2 node graph and initialize the visualization environment:

```bash
ros2 launch custom_robot_description display.launch.py
```

## Expected Outcome

After executing the launch command:

* The `custom_robot_description` package will be loaded.
* Required ROS 2 nodes will be started automatically.
* The robot model will be published and visualized.
* The visualization environment (e.g., RViz) will open and display the robot configuration.

## Notes

* Ensure ROS 2 is properly installed and configured before running these commands.
* Verify that all package dependencies have been installed.
* If changes are made to the package source files, repeat the build process before launching.
