cmake_minimum_required(VERSION 3.10)
project(DodgeTheMagma)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(SFML 2.5 COMPONENTS graphics window system REQUIRED)

# 🔧 Thêm dòng này nè
include_directories(${CMAKE_SOURCE_DIR}/include)

file(GLOB SOURCES src/*.cpp)
add_executable(DodgeTheMagma ${SOURCES})

target_link_libraries(DodgeTheMagma sfml-graphics sfml-window sfml-system)
