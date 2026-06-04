cmake_minimum_required(VERSION 3.8)
project(custom_robot_description)

find_package(ament_cmake REQUIRED)

# Install the flat files from your package directory
install(FILES
  CMakeLists.txt
  package.xml
  display.launch.py
  properties.xacro
  robot.urdf.xacro
  DESTINATION share/${PROJECT_NAME}
)

# Safely install urdf.rviz if it's sitting in this directory or the parent directory
if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/urdf.rviz")
    install(FILES urdf.rviz DESTINATION share/${PROJECT_NAME})
elseif(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/../urdf.rviz")
    install(FILES ../urdf.rviz DESTINATION share/${PROJECT_NAME})
endif()

ament_package()