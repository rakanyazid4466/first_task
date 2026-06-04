cmake_minimum_required(VERSION 3.8)
project(custom_robot_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch urdf DESTINATION share/${PROJECT_NAME})

if(IS_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/media")
  install(DIRECTORY media DESTINATION share/${PROJECT_NAME})
endif()

ament_package()